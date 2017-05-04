# 2017.05.04 15:23:43 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/prb_windows/PrebattlesListWindow.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView
from gui.prb_control.entities.listener import IGlobalListener
from messenger.gui import events_dispatcher
from messenger.gui.Scaleform.view.lobby import MESSENGER_VIEW_ALIAS

class PrebattlesListWindow(AbstractWindowView, IGlobalListener):

    def __init__(self, name):
        super(PrebattlesListWindow, self).__init__()
        self._name = name
        self.isMinimising = False

    @property
    def chat(self):
        chat = None
        if MESSENGER_VIEW_ALIAS.CHANNEL_COMPONENT in self.components:
            chat = self.components[MESSENGER_VIEW_ALIAS.CHANNEL_COMPONENT]
        return chat

    def onWindowClose(self):
        self.destroy()

    def onWindowMinimize(self):
        self.isMinimising = False
        self.destroy()

    def _dispose(self):
        super(PrebattlesListWindow, self)._dispose()

    def _onRegisterFlashComponent(self, viewPy, alias):
        if alias == MESSENGER_VIEW_ALIAS.CHANNEL_COMPONENT:
            events_dispatcher.rqActivateLazyChannel(self._name, viewPy)

    def _onUnregisterFlashComponent(self, viewPy, alias):
        if alias == MESSENGER_VIEW_ALIAS.CHANNEL_COMPONENT:
            if self.isMinimising:
                events_dispatcher.rqDeactivateLazyChannel(self._name)
            else:
                events_dispatcher.rqExitFromLazyChannel(self._name)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\prb_windows\PrebattlesListWindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:43 Støední Evropa (letní èas)
