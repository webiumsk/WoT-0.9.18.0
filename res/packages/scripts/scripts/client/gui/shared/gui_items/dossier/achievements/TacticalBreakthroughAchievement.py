# 2017.05.04 15:26:00 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/TacticalBreakthroughAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SeriesAchievement

class TacticalBreakthroughAchievement(SeriesAchievement):

    def __init__(self, dossier, value = None):
        super(TacticalBreakthroughAchievement, self).__init__('tacticalBreakthrough', _AB.SINGLE, dossier, value)

    def _getCounterRecordNames(self):
        return ((_AB.TEAM_7X7, 'tacticalBreakthroughSeries'), (_AB.TEAM_7X7, 'maxTacticalBreakthroughSeries'))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\TacticalBreakthroughAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:00 Støední Evropa (letní èas)
