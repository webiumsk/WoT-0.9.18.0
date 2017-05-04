# 2017.05.04 15:22:15 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/prb_control/entities/training/legacy/actions_validator.py
from gui.prb_control.entities.base.actions_validator import ActionsValidatorComposite, BaseActionsValidator
from gui.prb_control.entities.base.legacy.actions_validator import LegacyVehicleValid
from gui.prb_control.events_dispatcher import g_eventDispatcher
from gui.prb_control.items import ValidationResult

class TrainingIsLoaded(BaseActionsValidator):
    """
    Is training view loaded
    """

    def _validate(self):
        if g_eventDispatcher.isTrainingLoaded():
            return ValidationResult(False)
        return super(TrainingIsLoaded, self)._validate()


class TrainingIntroActionsValidator(ActionsValidatorComposite):
    """
    Training intro actions validation class
    """

    def __init__(self, entity):
        validators = [TrainingIsLoaded(entity)]
        super(TrainingIntroActionsValidator, self).__init__(entity, validators)


class TrainingActionsValidator(TrainingIntroActionsValidator):
    """
    Training actions validation class
    """

    def __init__(self, entity):
        super(TrainingActionsValidator, self).__init__(entity)
        self.addValidator(LegacyVehicleValid(entity))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\training\legacy\actions_validator.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:15 Støední Evropa (letní èas)
