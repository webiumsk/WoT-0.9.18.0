# 2017.05.04 15:25:56 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/GuardsmanAchievement.py
from abstract import ClassProgressAchievement
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract.mixins import Deprecated, NoProgressBar

class GuardsmanAchievement(Deprecated, NoProgressBar, ClassProgressAchievement):

    def __init__(self, dossier, value = None):
        ClassProgressAchievement.__init__(self, 'guardsman', _AB.HISTORICAL, dossier, value)

    def getNextLevelInfo(self):
        return ('winsLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.HISTORICAL, 'guardsman')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.HISTORICAL, 'weakVehiclesWins')
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\GuardsmanAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:25:56 Støední Evropa (letní èas)
