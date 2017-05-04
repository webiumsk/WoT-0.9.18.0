# 2017.05.04 15:27:13 Støední Evropa (letní èas)
# Embedded file name: scripts/client/messenger/proto/bw/limits.py
from constants import CHAT_MESSAGE_MAX_LENGTH, CHAT_MESSAGE_MAX_LENGTH_IN_BATTLE
from messenger.m_constants import MESSAGES_HISTORY_MAX_LEN
from messenger.proto.interfaces import IProtoLimits

class BattleLimits(IProtoLimits):

    def getMessageMaxLength(self):
        return CHAT_MESSAGE_MAX_LENGTH_IN_BATTLE

    def getHistoryMaxLength(self):
        return MESSAGES_HISTORY_MAX_LEN


class LobbyLimits(IProtoLimits):

    def getMessageMaxLength(self):
        return CHAT_MESSAGE_MAX_LENGTH

    def getHistoryMaxLength(self):
        return MESSAGES_HISTORY_MAX_LEN


class CHANNEL_LIMIT(object):
    NAME_MIN_LENGTH = 3
    NAME_MAX_LENGTH = 32
    PWD_MIN_LENGTH = 3
    PWD_MAX_LENGTH = 12
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\messenger\proto\bw\limits.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:13 Støední Evropa (letní èas)
