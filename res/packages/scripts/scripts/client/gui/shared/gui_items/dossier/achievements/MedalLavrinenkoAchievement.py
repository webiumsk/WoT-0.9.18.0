# 2017.05.04 15:25:58 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/MedalLavrinenkoAchievement.py
from abstract import ClassProgressAchievement
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB

class MedalLavrinenkoAchievement(ClassProgressAchievement):

    def __init__(self, dossier, value = None):
        super(MedalLavrinenkoAchievement, self).__init__('medalLavrinenko', _AB.TOTAL, dossier, value)

    def getNextLevelInfo(self):
        return ('dropPointsLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, 'medalLavrinenko')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getRandomStats().getDroppedCapturePoints() - dossier.getClanStats().getDroppedCapturePoints() + dossier.getTeam7x7Stats().getDroppedCapturePoints() + dossier.getFortBattlesStats().getDroppedCapturePoints() + dossier.getFortSortiesStats().getDroppedCapturePoints() + dossier.getGlobalMapStats().getDroppedCapturePoints()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\MedalLavrinenkoAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:25:58 Støední Evropa (letní èas)
