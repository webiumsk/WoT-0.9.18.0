# 2017.05.04 15:26:00 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/StrategicOperationsAchievement.py
from abstract import ClassProgressAchievement
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract.mixins import Deprecated, NoProgressBar

class StrategicOperationsAchievement(Deprecated, NoProgressBar, ClassProgressAchievement):

    def __init__(self, dossier, value = None):
        super(StrategicOperationsAchievement, self).__init__('strategicOperations', _AB.RATED_7X7, dossier, value)

    def getNextLevelInfo(self):
        return ('winsLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.RATED_7X7, 'strategicOperations')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getTotalStats().getWinsCount()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\StrategicOperationsAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:00 Støední Evropa (letní èas)
