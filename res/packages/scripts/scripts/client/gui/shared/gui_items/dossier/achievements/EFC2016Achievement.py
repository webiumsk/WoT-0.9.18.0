# 2017.05.04 15:25:56 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/EFC2016Achievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SeriesAchievement
from abstract.mixins import Quest

class EFC2016Achievement(Quest, SeriesAchievement):

    def __init__(self, dossier, value = None):
        SeriesAchievement.__init__(self, 'EFC2016', _AB.SINGLE, dossier, value)

    def _getCounterRecordNames(self):
        return ((_AB.TOTAL, 'EFC2016WinSeries'), (_AB.TOTAL, 'maxEFC2016WinSeries'))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\EFC2016Achievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:25:56 Støední Evropa (letní èas)
