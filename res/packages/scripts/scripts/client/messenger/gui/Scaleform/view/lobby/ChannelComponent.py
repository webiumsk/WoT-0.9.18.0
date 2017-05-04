# 2017.05.04 15:27:07 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/messenger/gui/Scaleform/view/lobby/ChannelComponent.py
import weakref
import constants
from debug_utils import LOG_DEBUG
from messenger.gui import events_dispatcher
from messenger.gui.Scaleform.meta.ChannelComponentMeta import ChannelComponentMeta
from messenger.proto.bw_chat2.wrappers import UnitDataFactory

class ChannelComponent(ChannelComponentMeta):

    def __init__(self):
        super(ChannelComponent, self).__init__()
        self._controller = lambda : None

    def __del__(self):
        LOG_DEBUG('ChannelComponent deleted', self)

    def setController(self, controller):
        controller.activate()
        events_dispatcher.notifyCarousel(controller.getChannel().getClientID(), notify=False)
        self._controller = weakref.ref(controller)
        if self.flashObject:
            self.as_setJoinedS(controller.isJoined())

    def removeController(self):
        self._controller = lambda : None
        if self.flashObject:
            self.as_setJoinedS(False)

    def close(self):
        ctrl = self._controller()
        if ctrl:
            ctrl.exit()

    def minimize(self):
        ctrl = self._controller()
        if ctrl:
            ctrl.deactivate()

    def getMessageMaxLength(self):
        return round(constants.CHAT_MESSAGE_MAX_LENGTH / 2, 0)

    def onLinkClick(self, data):
        raise NotImplementedError('Shared battle results is not longer supported')

    def isJoined(self):
        isJoined = False
        if self._controller():
            isJoined = self._controller().isJoined()
        return isJoined

    def sendMessage(self, message):
        result = False
        if self._controller():
            result = self._controller().sendMessage(message)
        return result

    def getHistory(self):
        result = ''
        if self._controller():
            result = '\n'.join(self._controller().getHistory())
        return result

    def addNotification(self, text):
        factory = UnitDataFactory()
        message = factory.messageVO(factory.broadcastArgs(text))
        self._controller().addMessage(message, False)

    def getLastUnsentMessage(self):
        result = ''
        return result

    def setLastUnsentMessage(self, message):
        LOG_DEBUG('ChannelComponent setLastUnsentMessage ', message, self)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\messenger\gui\Scaleform\view\lobby\ChannelComponent.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:07 St�edn� Evropa (letn� �as)
