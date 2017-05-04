# 2017.05.04 15:25:58 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/MedalPoppelAchievement.py
from abstract import ClassProgressAchievement
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB

class MedalPoppelAchievement(ClassProgressAchievement):

    def __init__(self, dossier, value = None):
        super(MedalPoppelAchievement, self).__init__('medalPoppel', _AB.TOTAL, dossier, value)

    def getNextLevelInfo(self):
        return ('vehiclesLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, 'medalPoppel')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getRandomStats().getSpottedEnemiesCount() - dossier.getClanStats().getSpottedEnemiesCount() + dossier.getTeam7x7Stats().getSpottedEnemiesCount() + dossier.getFortBattlesStats().getSpottedEnemiesCount() + dossier.getFortSortiesStats().getSpottedEnemiesCount() + dossier.getGlobalMapStats().getSpottedEnemiesCount()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\MedalPoppelAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:25:58 Støední Evropa (letní èas)
