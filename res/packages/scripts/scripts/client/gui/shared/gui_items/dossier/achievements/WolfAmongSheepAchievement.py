# 2017.05.04 15:26:01 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/WolfAmongSheepAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SimpleProgressAchievement

class WolfAmongSheepAchievement(SimpleProgressAchievement):

    def __init__(self, dossier, value = None):
        super(WolfAmongSheepAchievement, self).__init__('wolfAmongSheepMedal', _AB.TEAM_7X7, dossier, value)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, 'wolfAmongSheep')
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\WolfAmongSheepAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:01 Støední Evropa (letní èas)
