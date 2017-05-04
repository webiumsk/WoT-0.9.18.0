# 2017.05.04 15:22:07 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/prb_control/entities/event/squad/actions_validator.py
from gui.prb_control.entities.base.squad.actions_validator import SquadActionsValidator, SquadVehiclesValidator

class _EventBattleVehiclesValidator(SquadVehiclesValidator):
    """
    Event battle squad vehicles validation
    """

    def _isValidMode(self, vehicle):
        return vehicle.isEvent


class EventBattleSquadActionsValidator(SquadActionsValidator):
    """
    Event battle squad actions validation class
    """

    def _createVehiclesValidator(self, entity):
        return _EventBattleVehiclesValidator(entity)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\event\squad\actions_validator.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:07 Støední Evropa (letní èas)
