# 2017.05.04 15:25:58 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/MousebaneAchievement.py
from dossiers2.custom.cache import getCache as getDossiersCache
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SimpleProgressAchievement

class MousebaneAchievement(SimpleProgressAchievement):

    def __init__(self, dossier, value = None):
        super(MousebaneAchievement, self).__init__('mousebane', _AB.TOTAL, dossier, value)

    def getNextLevelInfo(self):
        return ('vehiclesLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getBlock('vehTypeFrags').get(getDossiersCache()['mausTypeCompDescr'], 0)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\MousebaneAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:25:59 Støední Evropa (letní èas)
