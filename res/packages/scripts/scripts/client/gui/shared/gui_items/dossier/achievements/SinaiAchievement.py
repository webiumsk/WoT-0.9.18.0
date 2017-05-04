# 2017.05.04 15:26:00 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/SinaiAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SimpleProgressAchievement

class SinaiAchievement(SimpleProgressAchievement):

    def __init__(self, dossier, value = None):
        super(SinaiAchievement, self).__init__('sinai', _AB.TOTAL, dossier, value)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, 'fragsSinai')
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\SinaiAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:00 Støední Evropa (letní èas)
