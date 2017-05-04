# 2017.05.04 15:27:23 Støední Evropa (letní èas)
# Embedded file name: scripts/client/messenger/proto/xmpp/xmpp_limits.py
from messenger.proto.interfaces import IUserSearchLimits, IProtoLimits
from messenger.proto.xmpp.xmpp_constants import USER_SEARCH_LIMITS, MESSAGE_LIMIT

class FindUserSearchLimits(IUserSearchLimits):

    def getMaxResultSize(self):
        return USER_SEARCH_LIMITS.FIND_USERS_BY_NAME_MAX_RESULT_SIZE

    def getRequestCooldown(self):
        return USER_SEARCH_LIMITS.FIND_USERS_BY_NAME_REQUEST_COOLDOWN_SEC


class MessageLimits(IProtoLimits):

    def getMessageMaxLength(self):
        return MESSAGE_LIMIT.MESSAGE_MAX_SIZE

    def getBroadcastCoolDown(self):
        return MESSAGE_LIMIT.COOLDOWN

    def getHistoryMaxLength(self):
        return MESSAGE_LIMIT.HISTORY_MAX_LEN
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\messenger\proto\xmpp\xmpp_limits.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:23 Støední Evropa (letní èas)
