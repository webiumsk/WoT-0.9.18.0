# 2017.05.04 15:25:56 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/FightingReconnaissanceAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SimpleProgressAchievement

class FightingReconnaissanceAchievement(SimpleProgressAchievement):

    def __init__(self, dossier, value = None):
        super(FightingReconnaissanceAchievement, self).__init__('fightingReconnaissanceMedal', _AB.TEAM_7X7, dossier, value)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, 'fightingReconnaissance')
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\FightingReconnaissanceAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:25:56 St�edn� Evropa (letn� �as)
