# 2017.05.04 15:22:06 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/prb_control/entities/company/legacy/permissions.py
from constants import PREBATTLE_ROLE
from gui.prb_control import prb_getters
from gui.prb_control.entities.base.legacy.permissions import LegacyPermissions
from gui.prb_control.entities.base.limits import TotalMaxCount

class CompanyPermissions(LegacyPermissions):
    """
    Company permissions class
    """

    def canSendInvite(self):
        return super(CompanyPermissions, self).canSendInvite() and self._canAddPlayers()

    def canChangeDivision(self):
        return self._roles & PREBATTLE_ROLE.CHANGE_DIVISION != 0 and self._teamState.isNotReady()

    def canExitFromQueue(self):
        return self.isCreator(self._roles)

    @classmethod
    def isCreator(cls, roles):
        return roles == PREBATTLE_ROLE.COMPANY_CREATOR

    def _canAddPlayers(self):
        """
        Can new player be added to team according to max limit
        """
        clientPrb = prb_getters.getClientPrebattle()
        result = False
        if clientPrb is not None:
            settings = prb_getters.getPrebattleSettings(prebattle=clientPrb)
            rosters = prb_getters.getPrebattleRosters(prebattle=clientPrb)
            result, _ = TotalMaxCount().check(rosters, 1, settings.getTeamLimits(1))
        return result
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\company\legacy\permissions.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:06 Støední Evropa (letní èas)
