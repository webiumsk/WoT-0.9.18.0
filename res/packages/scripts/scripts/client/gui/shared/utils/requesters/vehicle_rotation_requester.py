# 2017.05.04 15:26:30 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/utils/requesters/vehicle_rotation_requester.py
import BigWorld
from adisp import async
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester

class VehicleRotationRequester(AbstractSyncDataRequester):

    def getBattlesCount(self, groupNum):
        battlesCount = self._groupLocks['groupBattles']
        groupIdx = max(0, groupNum - 1)
        if len(battlesCount) > groupIdx:
            return battlesCount[groupIdx]
        return -1

    def isGroupLocked(self, groupNum):
        if groupNum == 0:
            return False
        groupsLocks = self._groupLocks['isGroupLocked']
        groupIdx = max(0, groupNum - 1)
        if len(groupsLocks) > groupIdx:
            return groupsLocks[groupIdx]
        return False

    def getGroupNum(self, vehIntCD):
        return self.getCacheValue('vehiclesGroupMapping', {}).get(vehIntCD, 0)

    def isInfinite(self, groupNum):
        return self.getBattlesCount(groupNum) == -1

    @property
    def _groupLocks(self):
        return self.getCacheValue('groupLocks', {'groupBattles': [],
         'isGroupLocked': []})

    @async
    def _requestCache(self, callback):
        BigWorld.player().vehicleRotation.getCache(lambda resID, value: self._response(resID, value, callback))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\utils\requesters\vehicle_rotation_requester.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:30 St�edn� Evropa (letn� �as)
