# 2017.05.04 15:22:05 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/prb_control/entities/battle_session/legacy/permissions.py
from gui.prb_control import prb_getters
from gui.prb_control.entities.base.legacy.permissions import LegacyPermissions
from gui.prb_control.entities.base.limits import TeamNoPlayersInBattle, MaxCount

class BattleSessionPermissions(LegacyPermissions):
    """
    Battle session's permissions class
    """

    def canSendInvite(self):
        return super(BattleSessionPermissions, self).canSendInvite() and self._canAddPlayers()

    def canExitFromQueue(self):
        return self.isCreator(self._roles)

    @classmethod
    def isCreator(cls, roles):
        return False

    def canAssignToTeam(self, team = 1):
        result = super(BattleSessionPermissions, self).canAssignToTeam(team)
        if not result:
            return False
        else:
            clientPrb = prb_getters.getClientPrebattle()
            result = False
            if clientPrb is not None:
                settings = prb_getters.getPrebattleSettings(prebattle=clientPrb)
                rosters = prb_getters.getPrebattleRosters(prebattle=clientPrb)
                prbType = prb_getters.getPrebattleType(clientPrb, settings)
                result, _ = TeamNoPlayersInBattle(prbType).check(rosters, team, settings.getTeamLimits(team))
            return result

    def _canAddPlayers(self):
        """
        Can new player be added to team according to max limit
        """
        clientPrb = prb_getters.getClientPrebattle()
        result = False
        if clientPrb is not None:
            settings = prb_getters.getPrebattleSettings(prebattle=clientPrb)
            rosters = prb_getters.getPrebattleRosters(prebattle=clientPrb)
            result, _ = MaxCount().check(rosters, 1, settings.getTeamLimits(1))
        return result
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\battle_session\legacy\permissions.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:05 St�edn� Evropa (letn� �as)
