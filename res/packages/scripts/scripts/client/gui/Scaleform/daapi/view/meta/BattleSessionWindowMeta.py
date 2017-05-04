# 2017.05.04 15:24:18 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleSessionWindowMeta.py
from gui.Scaleform.daapi.view.lobby.prb_windows.PrebattleWindow import PrebattleWindow

class BattleSessionWindowMeta(PrebattleWindow):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends PrebattleWindow
    """

    def requestToAssignMember(self, accId):
        self._printOverrideError('requestToAssignMember')

    def requestToUnassignMember(self, accId):
        self._printOverrideError('requestToUnassignMember')

    def canMoveToAssigned(self):
        self._printOverrideError('canMoveToAssigned')

    def canMoveToUnassigned(self):
        self._printOverrideError('canMoveToUnassigned')

    def as_setStartTimeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setStartTime(value)

    def as_setTotalPlayersCountS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setTotalPlayersCount(value)

    def as_setInfoS(self, wins, map, firstTeam, secondTeam, count, description, comment):
        if self._isDAAPIInited():
            return self.flashObject.as_setInfo(wins, map, firstTeam, secondTeam, count, description, comment)

    def as_setNationsLimitsS(self, nations):
        """
        :param nations: Represented by DataProvider (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setNationsLimits(nations)

    def as_setClassesLimitsS(self, vehicleLevels, classesLimitsAreIdentical):
        if self._isDAAPIInited():
            return self.flashObject.as_setClassesLimits(vehicleLevels, classesLimitsAreIdentical)

    def as_setCommonLimitsS(self, teamLevel, maxPlayers):
        if self._isDAAPIInited():
            return self.flashObject.as_setCommonLimits(teamLevel, maxPlayers)

    def as_setPlayersCountTextS(self, playersCountText):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayersCountText(playersCountText)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BattleSessionWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:18 Støední Evropa (letní èas)
