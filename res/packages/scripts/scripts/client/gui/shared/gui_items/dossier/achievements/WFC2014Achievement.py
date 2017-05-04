# 2017.05.04 15:26:01 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/WFC2014Achievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SeriesAchievement
from abstract.mixins import Quest

class WFC2014Achievement(Quest, SeriesAchievement):

    def __init__(self, dossier, value = None):
        SeriesAchievement.__init__(self, 'WFC2014', _AB.SINGLE, dossier, value)

    def _getCounterRecordNames(self):
        return ((_AB.TOTAL, 'WFC2014WinSeries'), (_AB.TOTAL, 'maxWFC2014WinSeries'))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\WFC2014Achievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:01 Støední Evropa (letní èas)
