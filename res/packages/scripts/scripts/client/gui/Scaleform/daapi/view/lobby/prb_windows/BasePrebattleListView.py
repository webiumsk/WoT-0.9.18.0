# 2017.05.04 15:23:41 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/prb_windows/BasePrebattleListView.py
from gui.Scaleform.daapi.view.meta.BasePrebattleListViewMeta import BasePrebattleListViewMeta
from messenger.gui import events_dispatcher
from messenger.gui.Scaleform.view.lobby import MESSENGER_VIEW_ALIAS

class BasePrebattleListView(BasePrebattleListViewMeta):

    def __init__(self, name):
        super(BasePrebattleListView, self).__init__()
        self._searchDP = None
        self._name = name
        return

    @property
    def chat(self):
        chat = None
        if MESSENGER_VIEW_ALIAS.CHANNEL_COMPONENT in self.components:
            chat = self.components[MESSENGER_VIEW_ALIAS.CHANNEL_COMPONENT]
        return chat

    def _onRegisterFlashComponent(self, viewPy, alias):
        if alias == MESSENGER_VIEW_ALIAS.CHANNEL_COMPONENT:
            events_dispatcher.rqActivateLazyChannel(self._name, viewPy)

    def _onUnregisterFlashComponent(self, viewPy, alias):
        if alias == MESSENGER_VIEW_ALIAS.CHANNEL_COMPONENT:
            if self.isMinimising:
                events_dispatcher.rqDeactivateLazyChannel(self._name)
            else:
                events_dispatcher.rqExitFromLazyChannel(self._name)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\prb_windows\BasePrebattleListView.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:41 Støední Evropa (letní èas)
