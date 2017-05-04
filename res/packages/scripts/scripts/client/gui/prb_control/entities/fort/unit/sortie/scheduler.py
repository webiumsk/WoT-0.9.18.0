# 2017.05.04 15:22:11 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/prb_control/entities/fort/unit/sortie/scheduler.py
from gui.prb_control.events_dispatcher import g_eventDispatcher
from gui.prb_control.entities.base.unit.scheduler import UnitScheduler
from gui.shared.fortifications.fort_listener import FortListener

class SortiesScheduler(UnitScheduler, FortListener):

    def __init__(self, entity):
        super(SortiesScheduler, self).__init__(entity)
        self.__sortiesHoursCtrl = None
        return

    def onClientStateChanged(self, state):
        super(SortiesScheduler, self).onClientStateChanged(state)
        self.__registerCurfewController()

    def init(self):
        self.__registerCurfewController()
        self.startFortListening()
        super(SortiesScheduler, self).init()

    def fini(self):
        self.stopFortListening()
        if self.__sortiesHoursCtrl:
            self.__sortiesHoursCtrl.onStatusChanged -= self.__updateCurfew
            self.__sortiesHoursCtrl = None
        super(SortiesScheduler, self).fini()
        return

    def __registerCurfewController(self):
        from gui.shared.ClanCache import g_clanCache
        if not self.__sortiesHoursCtrl:
            provider = g_clanCache.fortProvider
            self.__sortiesHoursCtrl = provider.getController().getSortiesCurfewCtrl()
            if self.__sortiesHoursCtrl:
                self.__sortiesHoursCtrl.onStatusChanged += self.__updateCurfew
                self.__updateCurfew()

    def __updateCurfew(self):
        g_eventDispatcher.updateUI()
        for listener in self._entity.getListenersIterator():
            listener.onUnitCurfewChanged()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\fort\unit\sortie\scheduler.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:11 St�edn� Evropa (letn� �as)
