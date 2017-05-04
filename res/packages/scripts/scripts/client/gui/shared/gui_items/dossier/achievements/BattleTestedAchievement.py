# 2017.05.04 15:25:55 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/BattleTestedAchievement.py
from abstract import ClassProgressAchievement
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB

class BattleTestedAchievement(ClassProgressAchievement):

    def __init__(self, dossier, value = None):
        super(BattleTestedAchievement, self).__init__('battleTested', _AB.TEAM_7X7, dossier, value)

    def getNextLevelInfo(self):
        return ('achievesLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, 'battleTested')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, 'awardCount')
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\BattleTestedAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:25:55 Støední Evropa (letní èas)
