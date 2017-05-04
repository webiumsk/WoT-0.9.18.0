# 2017.05.04 15:27:11 Støední Evropa (letní èas)
# Embedded file name: scripts/client/messenger/proto/shared_messages.py
from messenger.proto.interfaces import IChatMessage

class ACTION_MESSAGE_TYPE(object):
    PLAYER = 0
    WARNING = 1
    ERROR = 2


class ClientActionMessage(IChatMessage):

    def __init__(self, msg = None, type_ = ACTION_MESSAGE_TYPE.PLAYER):
        super(ClientActionMessage, self).__init__()
        self.__message = msg
        self.__type = type_

    def setMessage(self, msg):
        self.__message = msg

    def getMessage(self):
        return self.__message

    def getType(self):
        return self.__type
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\messenger\proto\shared_messages.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:11 Støední Evropa (letní èas)
