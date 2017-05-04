# 2017.05.04 15:22:10 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/prb_control/entities/fort/unit/actions_handler.py
from gui.prb_control.events_dispatcher import g_eventDispatcher
from gui.prb_control.entities.base.unit.actions_handler import UnitActionsHandler
from gui.prb_control.settings import FUNCTIONAL_FLAG

class FortActionsHandler(UnitActionsHandler):
    """
    Fort actions handler class
    """

    def showGUI(self):
        g_eventDispatcher.showFortWindow()

    def executeInit(self, ctx):
        prbType = self._entity.getEntityType()
        flags = self._entity.getFlags()
        g_eventDispatcher.loadFort(prbType)
        if flags.isInIdle():
            g_eventDispatcher.setUnitProgressInCarousel(prbType, True)
        return FUNCTIONAL_FLAG.LOAD_WINDOW

    def _canDoAutoSearch(self, unit, stats):
        return False
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\fort\unit\actions_handler.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:10 Støední Evropa (letní èas)
