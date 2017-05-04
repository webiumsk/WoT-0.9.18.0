# 2017.05.04 15:22:08 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/prb_control/entities/e_sport/unit/public/actions_validator.py
from gui.prb_control.entities.base.actions_validator import ActionsValidatorComposite
from gui.prb_control.entities.base.unit.actions_validator import UnitActionsValidator, UnitLevelsValidator, CommanderValidator
from gui.prb_control.items import ValidationResult
from gui.prb_control.settings import UNIT_RESTRICTION

class ESportLevelsValidator(CommanderValidator):
    """
    ESport public levels validator
    """

    def _validate(self):
        stats = self._entity.getStats()
        levels = self._getInvalidLevels(stats)
        if stats.occupiedSlotsCount > 1 and stats.freeSlotsCount > 0 and len(levels):
            return ValidationResult(False, UNIT_RESTRICTION.INVALID_TOTAL_LEVEL, {'vehLevels': levels})
        return super(ESportLevelsValidator, self)._validate()

    def _getInvalidLevels(self, stats):
        rosterSettings = self._entity.getRosterSettings()
        maxLevel = rosterSettings.getMaxLevel()
        maxSlots = rosterSettings.getMaxSlots()
        maxTotalLevel = rosterSettings.getMaxTotalLevel()
        compensation = maxLevel * maxSlots - maxTotalLevel
        if compensation <= 0:
            return []
        levels = []
        for level in stats.levelsSeq:
            if not level:
                continue
            diff = maxLevel - level
            if diff:
                if level not in levels:
                    levels.append(level)
                if compensation > 0:
                    compensation -= diff
                else:
                    levels.sort()
                    return levels

        return []


class ESportSearchValidator(UnitLevelsValidator):
    """
    ESport search for players warning
    """

    def _validate(self):
        return ValidationResult(True, UNIT_RESTRICTION.NEED_PLAYERS_SEARCH)

    def _isEnabled(self):
        return not self._areVehiclesSelected(self._entity.getStats())


class ESportActionsValidator(UnitActionsValidator):
    """
    ESport actions validation class. Has additional warning checker.
    """

    def __init__(self, entity):
        super(ESportActionsValidator, self).__init__(entity)
        self.addWarning(ESportSearchValidator(entity))

    def _createLevelsValidator(self, entity):
        baseValidator = super(ESportActionsValidator, self)._createLevelsValidator(entity)
        return ActionsValidatorComposite(entity, validators=[ESportLevelsValidator(entity), baseValidator])
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\e_sport\unit\public\actions_validator.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:08 St�edn� Evropa (letn� �as)
