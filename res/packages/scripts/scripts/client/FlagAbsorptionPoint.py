# 2017.05.04 15:19:59 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/FlagAbsorptionPoint.py
import BigWorld
from Math import Vector3
from debug_utils import LOG_DEBUG
from CTFManager import _CTFCheckPoint, _CTFPointFlag, _UDOAttributeChecker

class FlagAbsorptionPoint(BigWorld.UserDataObject, _CTFCheckPoint, _CTFPointFlag, _UDOAttributeChecker):
    _FRIEND_OR_NEUTRAL = True
    _ENEMY = False
    _TEAM_PARAMS = {_FRIEND_OR_NEUTRAL: ('greenFlagModel', 4278255360L),
     _ENEMY: ('redFlagModel', 4294901760L)}
    _OVER_TERRAIN_HEIGHT = 0.5

    def __init__(self):
        BigWorld.UserDataObject.__init__(self)
        _UDOAttributeChecker.__init__(self)
        self.checkAttribute('radiusModel')
        self.checkAttribute('greenFlagModel')
        self.checkAttribute('redFlagModel')
        LOG_DEBUG('FlagAbsorptionPoint ', self.position, self.radius, self.team)
        _CTFCheckPoint.__init__(self, self.radiusModel)
        player = BigWorld.player()
        if player is not None:
            teamParams = self._TEAM_PARAMS[self.team in (0, player.team)]
        else:
            teamParams = self._TEAM_PARAMS[0]
        flagModelName = getattr(self, teamParams[0], None)
        color = teamParams[1]
        _CTFPointFlag.__init__(self, flagModelName, self.position)
        if self.__isVisibleForCurrentArena():
            self._createTerrainSelectedArea(self.position, self.radius * 2.0, self._OVER_TERRAIN_HEIGHT, color)
            self._createFlag(self.applyOverlay > 0)
        return

    def __del__(self):
        if self.isAttrCheckFailed:
            return
        _CTFCheckPoint.__del__(self)
        _CTFPointFlag.__del__(self)

    def __isVisibleForCurrentArena(self):
        player = BigWorld.player()
        if player is not None:
            arenaType = player.arena.arenaType
            if hasattr(arenaType, 'flagAbsorptionPoints'):
                flagAbsorptionPoints = arenaType.flagAbsorptionPoints
                for pt in flagAbsorptionPoints:
                    if 'guid' not in pt:
                        continue
                    if pt['guid'] == self.guid:
                        return True

        return False
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\FlagAbsorptionPoint.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:19:59 St�edn� Evropa (letn� �as)
