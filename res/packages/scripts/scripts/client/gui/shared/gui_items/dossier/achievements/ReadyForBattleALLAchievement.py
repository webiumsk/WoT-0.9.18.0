# 2017.05.04 15:25:59 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/ReadyForBattleALLAchievement.py
from abstract import ClassProgressAchievement
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB

class ReadyForBattleALLAchievement(ClassProgressAchievement):

    def __init__(self, dossier, value = None):
        self.__isCurrentUserAchievement = dossier.isCurrentUser() if dossier is not None else False
        super(ReadyForBattleALLAchievement, self).__init__('readyForBattleALL', _AB.TOTAL, dossier, value)
        return

    def getNextLevelInfo(self):
        return ('questsLeft', self._lvlUpValue if self.__isCurrentUserAchievement else 0)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, 'readyForBattleALL')

    def _readCurrentProgressValue(self, dossier):
        return 0
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\ReadyForBattleALLAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:25:59 Støední Evropa (letní èas)
