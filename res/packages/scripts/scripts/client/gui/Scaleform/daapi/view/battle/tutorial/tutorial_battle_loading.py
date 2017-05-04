# 2017.05.04 15:22:45 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/tutorial/tutorial_battle_loading.py
from gui.Scaleform.daapi.view.battle.shared.battle_loading import BattleLoading
from gui.Scaleform.daapi.view.meta.TutorialLoadingMeta import TutorialLoadingMeta

class TutorialBattleLoading(BattleLoading, TutorialLoadingMeta):

    def invalidateArenaInfo(self):
        super(TutorialBattleLoading, self).invalidateArenaInfo()
        arenaInfoData = {'mapName': self._battleCtx.getArenaTypeName(),
         'battleTypeLocaleStr': self._battleCtx.getArenaDescriptionString(isInBattle=False),
         'battleTypeFrameLabel': self._battleCtx.getArenaFrameLabel()}
        self.as_setTutorialArenaInfoS(arenaInfoData)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\battle\tutorial\tutorial_battle_loading.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:45 Støední Evropa (letní èas)
