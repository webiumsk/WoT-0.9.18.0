# 2017.05.04 15:23:44 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/prb_windows/SquadActionButtonStateVO.py
from gui.Scaleform.daapi.view.lobby.rally.ActionButtonStateVO import ActionButtonStateVO
from gui.Scaleform.locale.CYBERSPORT import CYBERSPORT
from gui.prb_control.settings import UNIT_RESTRICTION
from gui.shared.formatters.ranges import toRomanRangeString
from helpers import int2roman, dependency
from skeletons.gui.game_control import IFalloutController
_VALID_RESTRICTIONS = (UNIT_RESTRICTION.COMMANDER_VEHICLE_NOT_SELECTED, UNIT_RESTRICTION.FALLOUT_NOT_ENOUGH_PLAYERS)

class SquadActionButtonStateVO(ActionButtonStateVO):
    falloutCtrl = dependency.descriptor(IFalloutController)

    def _isEnabled(self, isValid, restriction):
        return isValid or restriction in _VALID_RESTRICTIONS

    def _getLabel(self):
        if self._playerInfo.isReady:
            label = CYBERSPORT.WINDOW_UNIT_NOTREADY
        else:
            label = CYBERSPORT.WINDOW_UNIT_READY
        return label

    def _getArenaStateStr(self):
        return (CYBERSPORT.WINDOW_UNIT_MESSAGE_SQUADINBATTLE, {})

    def _getReadyValidInSlotStateStr(self):
        return (CYBERSPORT.WINDOW_UNIT_MESSAGE_GETNOTREADY, {})

    def _getIdleStateStr(self):
        return (CYBERSPORT.SQUADWINDOW_WAITINGFORBATTLE, {})

    def _getFalloutVehLevelStr(self):
        config = self.falloutCtrl.getConfig()
        requiredLevelStr = int2roman(config.vehicleLevelRequired)
        return (CYBERSPORT.WINDOW_UNIT_MESSAGE_FALLOUTLEVEL, {'level': requiredLevelStr})

    def _getFalloutVehMinStr(self):
        config = self.falloutCtrl.getConfig()
        allowedLevelsList = list(config.allowedLevels)
        if len(allowedLevelsList) > 1:
            return (CYBERSPORT.WINDOW_UNIT_MESSAGE_FALLOUTMIN_LEVELRANGE, {'level': toRomanRangeString(allowedLevelsList, 1)})
        else:
            return (CYBERSPORT.WINDOW_UNIT_MESSAGE_FALLOUTMIN_REQUIREDLEVEL, {'level': int2roman(config.vehicleLevelRequired)})

    def _getFalloutVehBrokenStr(self):
        return ('#cyberSport:window/unit/message/falloutGroupNotReady', {})
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\prb_windows\SquadActionButtonStateVO.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:44 St�edn� Evropa (letn� �as)
