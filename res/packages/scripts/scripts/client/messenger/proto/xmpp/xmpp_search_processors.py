# 2017.05.04 15:27:24 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/messenger/proto/xmpp/xmpp_search_processors.py
from debug_utils import LOG_WARNING
from messenger import g_settings
from messenger.m_constants import PROTO_TYPE, CLIENT_ACTION_ID, CLIENT_ERROR_ID, USER_TAG
from messenger.proto import proto_getter
from messenger.proto.search_processor import SearchProcessor
from messenger.proto.shared_errors import ClientActionError, ChatCoolDownError
from messenger.proto.xmpp import xmpp_limits as limits
from messenger.proto.xmpp.entities import XMPPUserEntity
from messenger.proto.xmpp.errors import createServerActionIQError, createServerIQError
from messenger.proto.xmpp.gloox_constants import GLOOX_EVENT, IQ_TYPE
from messenger.proto.xmpp.xmpp_constants import CHANNEL_LIMIT
from messenger.proto.xmpp.gloox_wrapper import ClientEventsHandler
from messenger.proto.xmpp.XmppCooldownManager import XmppCooldownManager
from messenger.proto.xmpp.extensions.search import ChannelSearchQuery, ChannelsListHandler, NicknamePrefixSearchQuery, NicknamePrefixSearchHandler
from messenger.ext import checkAccountName
from messenger.storage import storage_getter

class SearchChannelsProcessor(SearchProcessor, ClientEventsHandler):

    def __init__(self, service):
        super(SearchChannelsProcessor, self).__init__()
        self.__sentRequestID = None
        self.__service = service
        self.proto.client.registerHandler(GLOOX_EVENT.IQ, self.__onIQReceived)
        return

    def __del__(self):
        super(SearchChannelsProcessor, self).__init__()
        self.proto.client.unregisterHandler(GLOOX_EVENT.IQ, self.__onIQReceived)

    @proto_getter(PROTO_TYPE.XMPP)
    def proto(self):
        return None

    def find(self, token, **kwargs):
        client = self.proto.client
        if client.isConnected():
            query = ChannelSearchQuery(token, to=self.__service, count=self.getSearchResultLimit())
            self._lastRequestID = client.sendIQ(query)
        else:
            error = ClientActionError(CLIENT_ACTION_ID.SEARCH_USER_ROOM, CLIENT_ERROR_ID.NOT_CONNECTED)
            self._onSearchFailed(error.getMessage())

    def getSearchResultLimit(self):
        return CHANNEL_LIMIT.MAX_SEARCH_RESULTS

    def __onIQReceived(self, iqID, iqType, pyGlooxTag):
        if self._lastRequestID != iqID:
            return
        if iqType == IQ_TYPE.ERROR:
            error = createServerActionIQError(CLIENT_ACTION_ID.SEARCH_USER_ROOM, pyGlooxTag)
            if error:
                reason = error.getMessage()
            else:
                reason = ''
                LOG_WARNING('Search error is not resolved on the client', pyGlooxTag.getXml())
            self._onSearchFailed(reason)
        else:
            result = ChannelsListHandler().handleTag(pyGlooxTag)
            self._onSearchTokenComplete(iqID, list(result)[:self.getSearchResultLimit()])


class SearchUserRoomsProcessor(SearchChannelsProcessor):

    def __init__(self):
        super(SearchUserRoomsProcessor, self).__init__(g_settings.server.XMPP.userRoomsService)


class SearchUsersProcessor(SearchProcessor, ClientEventsHandler):
    """ Search users by name using the XMPP
    """

    def __init__(self):
        super(SearchUsersProcessor, self).__init__()
        self.__sentRequestID = None
        self.__limits = limits.FindUserSearchLimits()
        self.__cooldown = XmppCooldownManager(self.__limits.getRequestCooldown())
        self.proto.client.registerHandler(GLOOX_EVENT.IQ, self.__onIQReceived)
        return

    def __del__(self):
        super(SearchUsersProcessor, self).__init__()
        self.proto.client.unregisterHandler(GLOOX_EVENT.IQ, self.__onIQReceived)

    @proto_getter(PROTO_TYPE.XMPP)
    def proto(self):
        return None

    @storage_getter('users')
    def usersStorage(self):
        return None

    def find(self, token, **kwargs):
        """
        Process find request
        :param token: search token (username prefix)
        :param kwargs: args
        :return: None
        """
        error = self.__checkCooldown(CLIENT_ACTION_ID.FIND_USERS_BY_PREFIX)
        if error:
            self._onSearchFailed(error.getMessage())
            return
        token = token.strip()
        isCorrect, reason = checkAccountName(token)
        if not isCorrect:
            self._onSearchFailed(reason)
            return
        client = self.proto.client
        if client.isConnected():
            query = NicknamePrefixSearchQuery(token, limit=self.getSearchResultLimit())
            self._lastRequestID = client.sendIQ(query)
            self.__cooldown.process(CLIENT_ACTION_ID.FIND_USERS_BY_PREFIX)
        else:
            error = ClientActionError(CLIENT_ACTION_ID.FIND_USERS_BY_PREFIX, CLIENT_ERROR_ID.NOT_CONNECTED)
            self._onSearchFailed(error.getMessage())

    def getSearchCoolDown(self):
        """
        Get cooldown between requests
        :return: cooldown in seconds
        """
        return self.__limits.getRequestCooldown()

    def getSearchResultLimit(self):
        """
        Get limit for search query size
        :return: limit for search query size
        """
        return self.__limits.getMaxResultSize()

    def __onIQReceived(self, iqID, iqType, pyGlooxTag):
        """
        Process iq response form xmpp server
        :param iqID: iq id sequence number
        :param iqType: iq type (get/set)
        :param pyGlooxTag: xmpp parser wrapper
        :return: None
        """
        if self._lastRequestID != iqID:
            return
        if iqType == IQ_TYPE.ERROR:
            error = createServerIQError(pyGlooxTag)
            if error:
                reason = error.getMessage()
            else:
                reason = ''
                LOG_WARNING('Search error is not resolved on the client', pyGlooxTag.getXml())
            self._onSearchFailed(reason)
        else:
            users = self.__OnSuccesResponse(pyGlooxTag)
            self._onSearchTokenComplete(iqID, users)

    def __OnSuccesResponse(self, pyGlooxTag):
        """
        Parse response object, and return user list
        :param pyGlooxTag: xmpp parser wrapper
        :return:
        """
        result = NicknamePrefixSearchHandler().handleTag(pyGlooxTag)
        users = []
        for userInfo in result:
            user = self.usersStorage.getUser(userInfo.dbId)
            if user:
                userInfo = user
            else:
                userInfo = XMPPUserEntity(userInfo.dbId, name=userInfo.nickname, clanInfo=userInfo.clanInfo)
                userInfo.addTags((USER_TAG.SEARCH, USER_TAG.TEMP))
                self.usersStorage.addUser(userInfo)
            users.append(userInfo)

        return users

    def __checkCooldown(self, actionID):
        """
        Check if cooldown was set for action
        :param actionID: action id
        :return: None, if cooldown was not set, else return ChatCoolDownError object
        """
        error = None
        if self.__cooldown.isInProcess(actionID):
            error = ChatCoolDownError(actionID, self.__cooldown.getDefaultCoolDown())
        return error
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\messenger\proto\xmpp\xmpp_search_processors.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:24 St�edn� Evropa (letn� �as)
