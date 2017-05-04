# 2017.05.04 15:27:22 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/messenger/proto/xmpp/xmpp_clan_listener.py
import BigWorld
from PlayerEvents import g_playerEvents
from debug_utils import LOG_ERROR, LOG_DEBUG
from gui.shared.utils import getPlayerDatabaseID
from messenger import g_settings
from messenger.m_constants import GAME_ONLINE_STATUS, USER_TAG
from messenger.proto.entities import ClanInfo
from messenger.proto.events import g_messengerEvents
from messenger.proto.xmpp import entities
from messenger.proto.xmpp.entities import XMPPUserEntity
from messenger.proto.xmpp.find_criteria import XmppClanChannelCriteria
from messenger.proto.xmpp.gloox_wrapper import ClientHolder
from messenger.proto.xmpp.xmpp_constants import XMPP_MUC_CHANNEL_TYPE
from messenger.storage import storage_getter

class XmppClanListener(ClientHolder):
    """Look for clan info and join to clan channel if we're in clan
    """
    __slots__ = ('__channelCriteria', '__clanChannel', '__clanDBID', '__clanAbbrev')

    def __init__(self):
        self.__channelCriteria = XmppClanChannelCriteria()
        self.__clanChannel = None
        self.__clanDBID = 0
        self.__clanAbbrev = ''
        return

    @storage_getter('users')
    def usersStorage(self):
        """Gets users storage instance
        :return: users storage instance
        :rtype: UsersStorage
        """
        return None

    @storage_getter('playerCtx')
    def playerCtx(self):
        """Gets player context instance
        :return: player context instance
        :rtype: PlayerCtxStorage
        """
        return None

    @storage_getter('channels')
    def channelsStorage(self):
        """Gets channel storage instance
        :return: channel storage instance
        :rtype: ChannelsStorage
        """
        return None

    def registerHandlers(self):
        """Adds listeners to channels shared events.
        """
        cEvents = g_messengerEvents.channels
        cEvents.onChannelInited += self.__ce_onChannelInited
        cEvents.onChannelDestroyed += self.__ce_onChannelDestroyed
        g_playerEvents.onClanMembersListChanged += self.__pe_onClanMembersListChanged
        self.playerCtx.onClanInfoChanged += self.__pc_onClanInfoChanged

    def unregisterHandlers(self):
        """Removes listeners from channels shared events.
        """
        cEvents = g_messengerEvents.channels
        cEvents.onChannelInited -= self.__ce_onChannelInited
        cEvents.onChannelDestroyed -= self.__ce_onChannelDestroyed
        g_playerEvents.onClanMembersListChanged -= self.__pe_onClanMembersListChanged
        self.playerCtx.onClanInfoChanged -= self.__pc_onClanInfoChanged

    def clear(self):
        """Clears current clan channel if it's exist.
        """
        if self.__clanChannel is not None:
            self.__clanChannel.onMembersListChanged -= self.__ce_onMembersListChanged
            self.__clanChannel.clear()
            self.__clanChannel = None
            self.__clanDBID = 0
            self.__clanAbbrev = ''
            for user in self.usersStorage.getClanMembersIterator():
                user.update(gosBit=-GAME_ONLINE_STATUS.IN_CLAN_CHAT)

        return

    def __addClanChannelToStorage(self):
        """Manually create clan channel entity and add it to the channel storage
        """
        if self.client().isConnected():
            clanChannelConfig = g_settings.server.XMPP.getChannelByType(XMPP_MUC_CHANNEL_TYPE.CLANS)
            if clanChannelConfig:
                clanChannelEntity = entities.XmppClanChannelEntity(self.__clanDBID, self.__clanAbbrev)
                if self.channelsStorage.addChannel(clanChannelEntity):
                    g_messengerEvents.channels.onChannelInited(clanChannelEntity)

    def __removeClanChannel(self):
        """Fire event for channel controller close clan channel
        """
        g_messengerEvents.channels.onChannelDestroyed(self.__clanChannel)

    def __initClanChannel(self, channel):
        """Initialize clan channel
        :param channel: channel name
        :type channel: XmppClanChannelEntity
        """
        if self.__clanChannel is not None:
            LOG_ERROR('Clan channel is defined', self.__clanChannel, channel)
            return
        else:
            self.__clanChannel = channel
            self.__clanChannel.onMembersListChanged += self.__ce_onMembersListChanged
            self.__refreshClanMembers()
            return

    def __refreshClanMembers(self):
        """Refresh clan members and update their status
        """
        getter = self.__clanChannel.getMember
        events = g_messengerEvents.users
        changed = False
        for user in self.usersStorage.getClanMembersIterator():
            dbID = user.getID()
            isOnline = user.getGOS() & GAME_ONLINE_STATUS.IN_CLAN_CHAT > 0
            member = getter(dbID)
            if member is not None:
                if not isOnline:
                    user.update(gosBit=GAME_ONLINE_STATUS.IN_CLAN_CHAT)
                    events.onUserStatusUpdated(user)
                    changed = True
            elif isOnline:
                user.update(gosBit=-GAME_ONLINE_STATUS.IN_CLAN_CHAT)
                events.onUserStatusUpdated(user)
                changed = True

        if changed:
            events.onClanMembersListChanged()
        return

    def __ce_onChannelInited(self, channel):
        """ Listener for event _ChannelsSharedEvents.onClanInfoChanged.
        :param channel: channel entity
        :type channel: XmppClanListener
        """
        if self.__channelCriteria.filter(channel):
            self.__initClanChannel(channel)

    def __ce_onChannelDestroyed(self, channel):
        """ Listener for event _ChannelsSharedEvents.onChannelDestroyed.
        :param channel: channel entity
        :type channel: XmppClanListener
        """
        if self.__channelCriteria.filter(channel):
            self.clear()

    def __ce_onMembersListChanged(self):
        """Listener for event _ChannelEvents.onMembersListChanged.
        """
        self.__refreshClanMembers()

    def __pe_onClanMembersListChanged(self):
        """Listener for event _PlayerEvents.onClanMembersListChanged.
        """
        clanMembers = getattr(BigWorld.player(), 'clanMembers', {})
        LOG_DEBUG('setClanMembersList', clanMembers)
        clanAbbrev = self.playerCtx.getClanAbbrev()
        clanDBID = self.playerCtx.getClanDbID()
        members = []
        if self.__clanChannel is not None:
            getter = self.__clanChannel.getMember
        else:

            def getter(dbID):
                return None

        playerID = getPlayerDatabaseID()
        for dbID, (name, roleFlags) in clanMembers.iteritems():
            if getter(dbID) is None:
                gos = GAME_ONLINE_STATUS.UNDEFINED
            else:
                gos = GAME_ONLINE_STATUS.ONLINE
            if playerID == dbID:
                user = XMPPUserEntity(dbID, name=name, clanInfo=ClanInfo(clanDBID, clanAbbrev, roleFlags))
            else:
                user = XMPPUserEntity(dbID, name=name, clanInfo=ClanInfo(clanDBID, clanAbbrev, roleFlags), gos=gos, tags={USER_TAG.CLAN_MEMBER})
            members.append(user)

        self.usersStorage.setClanMembersList(members)
        return

    def __pc_onClanInfoChanged(self):
        """Listener for event UpdateManager.stats.clanInfo.
        """
        self.__clanAbbrev = self.playerCtx.getClanAbbrev()
        self.__clanDBID = self.playerCtx.getClanDbID()
        if self.__clanAbbrev and self.__clanDBID:
            self.__checkForJoin()
        else:
            self.__checkForLeave()
        userClanInfo = ClanInfo(dbID=self.__clanDBID, abbrev=self.__clanAbbrev)
        for user in self.usersStorage.getClanMembersIterator():
            user.update(clanInfo=userClanInfo)

        g_messengerEvents.users.onClanMembersListChanged()

    def __checkForJoin(self):
        """Try for join to clan channel
        """
        if self.__clanChannel is None and self.__clanDBID != 0 and self.__clanAbbrev != '':
            self.__addClanChannelToStorage()
        return

    def __checkForLeave(self):
        """Try to leave from clan channel
        """
        if self.__clanChannel is not None:
            self.__removeClanChannel()
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\messenger\proto\xmpp\xmpp_clan_listener.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:23 St�edn� Evropa (letn� �as)
