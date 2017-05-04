# 2017.05.04 15:25:57 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/InvincibleAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SeriesAchievement

class InvincibleAchievement(SeriesAchievement):

    def __init__(self, dossier, value = None):
        super(InvincibleAchievement, self).__init__('invincible', _AB.SINGLE, dossier, value)

    def _getCounterRecordNames(self):
        return ((_AB.TOTAL, 'invincibleSeries'), (_AB.TOTAL, 'maxInvincibleSeries'))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\InvincibleAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:25:57 Støední Evropa (letní èas)
