# 2017.05.04 15:22:01 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/prb_control/entities/base/squad/permissions.py
from gui.prb_control.entities.base.unit.permissions import UnitPermissions

class SquadPermissions(UnitPermissions):
    """
    Squad permission class
    """

    def canChangeLeadership(self):
        return True

    def canStealLeadership(self):
        return False

    def canExitFromQueue(self):
        return self.isCommander(self._roles)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\base\squad\permissions.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:01 Støední Evropa (letní èas)
