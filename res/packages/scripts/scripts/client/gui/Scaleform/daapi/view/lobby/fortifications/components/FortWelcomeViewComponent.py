# 2017.05.04 15:23:29 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/fortifications/components/FortWelcomeViewComponent.py
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.meta.FortWelcomeViewMeta import FortWelcomeViewMeta
from gui.Scaleform.daapi.view.lobby.fortifications.fort_utils.FortViewHelper import FortViewHelper
from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE

class FortWelcomeViewComponent(FortWelcomeViewMeta, FortViewHelper):

    def __init__(self):
        super(FortWelcomeViewComponent, self).__init__()

    def _onRegisterFlashComponent(self, viewPy, alias):
        if alias == VIEW_ALIAS.FORT_WELCOME_INFO:
            viewPy.setMyClan(True)

    def onViewReady(self):
        g_eventBus.handleEvent(events.FortEvent(events.FortEvent.VIEW_LOADED), scope=EVENT_BUS_SCOPE.FORT)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\fortifications\components\FortWelcomeViewComponent.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:29 Støední Evropa (letní èas)
