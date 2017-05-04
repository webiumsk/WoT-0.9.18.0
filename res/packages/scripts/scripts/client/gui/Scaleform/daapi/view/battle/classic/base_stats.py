# 2017.05.04 15:22:25 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/classic/base_stats.py
from gui.Scaleform.daapi.view.meta.StatsBaseMeta import StatsBaseMeta
from gui.shared import events, EVENT_BUS_SCOPE
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class StatsBase(StatsBaseMeta):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def acceptSquad(self, playerID):
        self.sessionProvider.invitations.accept(long(playerID))

    def addToSquad(self, playerID):
        self.sessionProvider.invitations.send(long(playerID))

    def _populate(self):
        self.addListener(events.GameEvent.SHOW_CURSOR, self.__handleShowCursor, EVENT_BUS_SCOPE.GLOBAL)
        self.addListener(events.GameEvent.HIDE_CURSOR, self.__handleHideCursor, EVENT_BUS_SCOPE.GLOBAL)
        super(StatsBase, self)._populate()

    def _dispose(self):
        self.__invitations = None
        self.removeListener(events.GameEvent.SHOW_CURSOR, self.__handleShowCursor, EVENT_BUS_SCOPE.GLOBAL)
        self.removeListener(events.GameEvent.HIDE_CURSOR, self.__handleHideCursor, EVENT_BUS_SCOPE.GLOBAL)
        super(StatsBase, self)._dispose()
        return

    def __handleShowCursor(self, _):
        self.as_setIsIntaractiveS(True)

    def __handleHideCursor(self, _):
        self.as_setIsIntaractiveS(False)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\battle\classic\base_stats.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:25 Støední Evropa (letní èas)
