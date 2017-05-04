# 2017.05.04 15:25:56 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/DeathTrackAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SeriesAchievement
from abstract.mixins import Quest
from abstract.mixins import NoProgressBar

class DeathTrackAchievement(NoProgressBar, Quest, SeriesAchievement):

    def __init__(self, dossier, value = None):
        SeriesAchievement.__init__(self, 'deathTrack', _AB.SINGLE, dossier, value)

    def _getCounterRecordNames(self):
        return ((_AB.TOTAL, 'deathTrackWinSeries'), (_AB.TOTAL, 'maxDeathTrackWinSeries'))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\DeathTrackAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:25:56 Støední Evropa (letní èas)
