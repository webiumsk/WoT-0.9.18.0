# 2017.05.04 15:25:58 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/MedalKnispelAchievement.py
from abstract import ClassProgressAchievement
from debug_utils import LOG_DEBUG
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB

class MedalKnispelAchievement(ClassProgressAchievement):

    def __init__(self, dossier, value = None):
        super(MedalKnispelAchievement, self).__init__('medalKnispel', _AB.TOTAL, dossier, value)

    def getNextLevelInfo(self):
        return ('damageLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, 'medalKnispel')

    def _readCurrentProgressValue(self, dossier):
        random = dossier.getRandomStats()
        clans = dossier.getClanStats()
        fortBattles = dossier.getFortBattlesStats()
        fortSorties = dossier.getFortSortiesStats()
        globalMap = dossier.getGlobalMapStats()
        return random.getDamageDealt() + random.getDamageReceived() - (clans.getDamageDealt() + clans.getDamageReceived()) + dossier.getTeam7x7Stats().getDamageDealt() + dossier.getTeam7x7Stats().getDamageReceived() + fortBattles.getDamageDealt() + fortBattles.getDamageReceived() + fortSorties.getDamageDealt() + fortSorties.getDamageReceived() + globalMap.getDamageDealt() + globalMap.getDamageReceived()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\MedalKnispelAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:25:58 St�edn� Evropa (letn� �as)
