# 2017.05.04 15:26:01 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/VictoryMarchClubAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SeriesAchievement
from abstract.mixins import Deprecated, NoProgressBar

class VictoryMarchClubAchievement(Deprecated, NoProgressBar, SeriesAchievement):

    def __init__(self, dossier, value = None):
        super(VictoryMarchClubAchievement, self).__init__('victoryMarch', _AB.SINGLE_7X7, dossier, value)

    def _getCounterRecordNames(self):
        return ((_AB.RATED_7X7, 'victoryMarchSeries'), (_AB.RATED_7X7, 'maxVictoryMarchSeries'))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\VictoryMarchClubAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:01 Støední Evropa (letní èas)
