# 2017.05.04 15:25:57 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/KampferAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import ClassProgressAchievement
from abstract.mixins import Fortification

class KampferAchievement(Fortification, ClassProgressAchievement):

    def __init__(self, dossier, value = None):
        ClassProgressAchievement.__init__(self, 'kampfer', _AB.FORT, dossier, value)

    def getNextLevelInfo(self):
        return ('winsLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.FORT, 'kampfer')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.FORT, 'wins')
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\KampferAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:25:57 Støední Evropa (letní èas)
