# 2017.05.04 15:25:55 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/AimerAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SeriesAchievement
from abstract.mixins import NoProgressBar

class AimerAchievement(NoProgressBar, SeriesAchievement):

    def __init__(self, dossier, value = None):
        SeriesAchievement.__init__(self, 'aimer', _AB.SINGLE, dossier, value)

    def _getCounterRecordNames(self):
        return ((_AB.TOTAL, 'maxAimerSeries'), (_AB.TOTAL, 'maxAimerSeries'))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\AimerAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:25:55 St�edn� Evropa (letn� �as)
