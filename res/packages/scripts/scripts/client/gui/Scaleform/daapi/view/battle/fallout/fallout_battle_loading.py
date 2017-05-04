# 2017.05.04 15:22:27 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/fallout/fallout_battle_loading.py
from gui.Scaleform.daapi.view.battle.shared.battle_loading import BattleLoading
from gui.Scaleform.daapi.view.fallout_info_panel_helper import getHelpTextAsDicts
from gui.Scaleform.locale.RES_ICONS import RES_ICONS

class FalloutMultiTeamBattleLoading(BattleLoading):

    def getIsFalloutMode(self):
        return True

    def _setTipsInfo(self):
        arenaDP = self._battleCtx.getArenaDP()
        if self._arenaVisitor.hasResourcePoints():
            bgUrl = RES_ICONS.MAPS_ICONS_EVENTINFOPANEL_FALLOUTRESOURCEPOINTSEVENT
        elif self._arenaVisitor.hasFlags():
            bgUrl = RES_ICONS.MAPS_ICONS_EVENTINFOPANEL_FALLOUTFLAGSEVENT
        else:
            bgUrl = ''
        self.as_setEventInfoPanelDataS({'bgUrl': bgUrl,
         'items': getHelpTextAsDicts(self._arenaVisitor)})
        self.as_setVisualTipInfoS(self.__makeVisualTipVO(arenaDP))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\battle\fallout\fallout_battle_loading.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:27 Støední Evropa (letní èas)
