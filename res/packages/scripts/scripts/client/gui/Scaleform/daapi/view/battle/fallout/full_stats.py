# 2017.05.04 15:22:28 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/fallout/full_stats.py
from gui.Scaleform.daapi.view.meta.FCStatsMeta import FCStatsMeta
from gui.Scaleform.daapi.view.meta.FMStatsMeta import FMStatsMeta
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class FalloutClassicFullStats(FCStatsMeta):
    pass


class FalloutMultiTeamFullStats(FMStatsMeta):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def _populate(self):
        super(FalloutMultiTeamFullStats, self)._populate()
        self.as_setSubTypeS(self.sessionProvider.getArenaDP().getMultiTeamsType())
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\battle\fallout\full_stats.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:28 Støední Evropa (letní èas)
