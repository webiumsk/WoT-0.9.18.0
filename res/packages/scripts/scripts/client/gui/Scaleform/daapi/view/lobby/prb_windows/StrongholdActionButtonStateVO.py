# 2017.05.04 15:23:45 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/prb_windows/StrongholdActionButtonStateVO.py
from gui.Scaleform.daapi.view.lobby.rally.ActionButtonStateVO import ActionButtonStateVO
from gui.prb_control.settings import UNIT_RESTRICTION
from gui.Scaleform.locale.CYBERSPORT import CYBERSPORT
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS

class StrongholdActionButtonStateVO(ActionButtonStateVO):

    def __init__(self, unitEntity):
        data = unitEntity.getStrongholdData()
        self.__isFirstBattle = data.isFirstBattle() if data else None
        self.__isSortie = data.isSortie() if data else None
        result = unitEntity.canPlayerDoAction()
        self.__unitIsValid, self.__restrictionType = result.isValid, result.restriction
        super(StrongholdActionButtonStateVO, self).__init__(unitEntity)
        return

    def _getArenaStateStr(self):
        return (TOOLTIPS.STRONGHOLDS_TIMER_SQUADINBATTLE, {})

    def _getLabel(self):
        label = CYBERSPORT.WINDOW_UNIT_READY
        isFirstStrongholdBattle = self.__isFirstBattle and not self.__isSortie
        if self._playerInfo.isCommander() and not isFirstStrongholdBattle:
            label = CYBERSPORT.WINDOW_UNIT_FIGHT
        if self._playerInfo.isReady and self.__restrictionType != UNIT_RESTRICTION.IS_IN_IDLE:
            label = CYBERSPORT.WINDOW_UNIT_NOTREADY
        return label
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\prb_windows\StrongholdActionButtonStateVO.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:45 St�edn� Evropa (letn� �as)
