# 2017.05.04 15:27:01 Støední Evropa (letní èas)
# Embedded file name: scripts/client/messenger/gui/Scaleform/channels/xmpp/factories.py
from messenger.gui.Scaleform.channels.xmpp import lobby_controllers
from messenger.gui.interfaces import IControllerFactory
from messenger.proto.xmpp import find_criteria
from messenger.proto.xmpp.gloox_constants import MESSAGE_TYPE
from messenger.storage import storage_getter

class LobbyControllersFactory(IControllerFactory):

    @storage_getter('channels')
    def channelsStorage(self):
        return None

    def init(self):
        controllers = []
        channels = self.channelsStorage.getChannelsByCriteria(find_criteria.XMPPChannelFindCriteria())
        for channel in channels:
            controller = self.factory(channel)
            if controller is not None:
                controllers.append(controller)

        return controllers

    def factory(self, channel):
        controller = None
        msgType = channel.getMessageType()
        if msgType == MESSAGE_TYPE.CHAT:
            controller = lobby_controllers.ChatSessionController(channel)
        elif msgType == MESSAGE_TYPE.GROUPCHAT:
            if channel.isLazy():
                controller = lobby_controllers.LazyUserRoomController(channel)
            elif channel.isClan():
                controller = lobby_controllers.ClanUserRoomController(channel)
            else:
                controller = lobby_controllers.UserRoomController(channel)
        return controller
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\messenger\gui\Scaleform\channels\xmpp\factories.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:01 Støední Evropa (letní èas)
