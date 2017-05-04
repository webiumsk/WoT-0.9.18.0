# 2017.05.04 15:22:12 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/prb_control/entities/sandbox/pre_queue/actions_validator.py
from CurrentVehicle import g_currentVehicle
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator, ActionsValidatorComposite
from gui.prb_control.entities.base.pre_queue.actions_validator import PreQueueActionsValidator
from gui.prb_control.items import ValidationResult
from gui.prb_control.settings import SANDBOX_MAX_VEHICLE_LEVEL, PRE_QUEUE_RESTRICTION

class SandboxVehicleValidator(BaseActionsValidator):
    """
    Sandbox vehicle validation
    """

    def _validate(self):
        vehicle = g_currentVehicle.item
        if vehicle.level > SANDBOX_MAX_VEHICLE_LEVEL or vehicle.isOnlyForEventBattles:
            return ValidationResult(False, PRE_QUEUE_RESTRICTION.LIMIT_LEVEL, {'levels': range(1, SANDBOX_MAX_VEHICLE_LEVEL + 1)})
        return super(SandboxVehicleValidator, self)._validate()


class SandboxActionsValidator(PreQueueActionsValidator):
    """
    Sandbox actions validation class
    """

    def __init__(self, entity):
        super(SandboxActionsValidator, self).__init__(entity)
        self.addValidator(SandboxVehicleValidator(entity))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\sandbox\pre_queue\actions_validator.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:12 St�edn� Evropa (letn� �as)
