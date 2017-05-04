# 2017.05.04 15:22:00 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/prb_control/entities/base/squad/actions_validator.py
from CurrentVehicle import g_currentVehicle
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator
from gui.prb_control.entities.base.unit.actions_validator import UnitActionsValidator, UnitVehiclesValidator
from gui.prb_control.items import ValidationResult, unit_items
from gui.prb_control.settings import UNIT_RESTRICTION
from helpers import dependency
from shared_utils import findFirst
from skeletons.gui.server_events import IEventsCache

class SquadBalanceValidator(BaseActionsValidator):
    """
    Validation for squad levels balance.
    """
    eventsCache = dependency.descriptor(IEventsCache)

    def _validate(self):
        _, unit = self._entity.getUnit()
        levels = unit.getSelectedVehicleLevels()
        distance = levels[-1] - levels[0] if len(levels) else 0
        unitHasPenalty = distance in self.eventsCache.getSquadPenaltyLevelDistance()
        if unitHasPenalty:
            return ValidationResult(True, UNIT_RESTRICTION.XP_PENALTY_VEHICLE_LEVELS)
        return super(SquadBalanceValidator, self)._validate()

    def _isEnabled(self):
        return self.eventsCache.isSquadXpFactorsEnabled()


class SquadVehiclesValidator(UnitVehiclesValidator):
    """
    Validation for squad selected vehicles.
    """

    def _getVehiclesInfo(self):
        vInfos = super(SquadVehiclesValidator, self)._getVehiclesInfo()
        if not findFirst(lambda v: not v.isEmpty(), vInfos, False):
            if g_currentVehicle.isPresent():
                vehicle = g_currentVehicle.item
                vInfos = (unit_items.VehicleInfo(vehicle.invID, vehicle.intCD, vehicle.level),)
        return vInfos


class SquadActionsValidator(UnitActionsValidator):
    """
    Squad actions validation class.
    """

    def __init__(self, entity):
        super(SquadActionsValidator, self).__init__(entity)
        self.addWarning(SquadBalanceValidator(entity))

    def _createVehiclesValidator(self, entity):
        return SquadVehiclesValidator(entity)

    def _createSlotsValidator(self, entity):
        return BaseActionsValidator(entity)

    def _createLevelsValidator(self, entity):
        return BaseActionsValidator(entity)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\base\squad\actions_validator.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:00 St�edn� Evropa (letn� �as)
