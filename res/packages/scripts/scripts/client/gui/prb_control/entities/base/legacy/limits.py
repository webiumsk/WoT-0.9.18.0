# 2017.05.04 15:21:58 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/prb_control/entities/base/legacy/limits.py
from gui.prb_control.entities.base.limits import LimitsCollection, VehicleIsValid, TeamIsValid

class LegacyLimits(LimitsCollection):
    """
    Class for legacy entities limits.
    """

    def __init__(self, entity):
        super(LegacyLimits, self).__init__(entity, (VehicleIsValid(),), (TeamIsValid(),))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\base\legacy\limits.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:59 Støední Evropa (letní èas)
