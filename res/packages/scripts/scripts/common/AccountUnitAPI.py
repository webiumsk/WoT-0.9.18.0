# 2017.05.04 15:28:18 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/AccountUnitAPI.py
import constants
from constants import PREBATTLE_TYPE
from UnitBase import UNIT_SLOT, CLIENT_UNIT_CMD, INV_ID_CLEAR_VEHICLE
from unit_roster_config import UnitRosterSlot
from debug_utils import *

class UNIT_API:
    NONE = 0
    CLIENT = 1
    WGSH = 2


def getUnitApiID(serverRequestID):
    return serverRequestID >> 32


def getOriginalRequestID(serverRequestID):
    return serverRequestID & 4294967295L


class AccountUnitAPI:

    def create(self, requestID, prebattleType, eventQueueType):
        raise 0 or AssertionError

    def join(self, requestID, unitMgrID, slotIdx):
        raise 0 or AssertionError

    def doCmd(self, requestID, unitMgrID, cmdID, param32, param64, paramString):
        raise 0 or AssertionError

    def setRosterSlots(self, requestID, unitMgrID, rosterSlotKeys, rosterSlotValues):
        raise 0 or AssertionError

    def sendInvites(self, requestID, accountsToInvite, comment):
        raise 0 or AssertionError

    def createEx(self, requestID, prebattleType, param32, param64, paramStr, paramPython):
        raise 0 or AssertionError

    def joinEx(self, requestID, unitMgrID, *args):
        raise 0 or AssertionError


class UnitClientAPI(object):

    def _callAPI(self, methodName, *args):
        raise 0 or AssertionError

    def getUnitMgrID(self):
        return 0

    def _callUnitAPI(self, methodName, *args):
        unitMgrID = self.getUnitMgrID()
        return self._callAPI(methodName, unitMgrID, *args)

    def _doCreate(self, prebattleType, int32Arg = 0):
        return self._callAPI('create', prebattleType, int32Arg)

    def _doUnitCmd(self, cmd, uint64Arg = 0, int32Arg = 0, strArg = ''):
        self._callUnitAPI('doCmd', cmd, uint64Arg, int32Arg, strArg)

    def create(self):
        return self._doCreate(PREBATTLE_TYPE.UNIT)

    def createSquad(self):
        return self._doCreate(PREBATTLE_TYPE.SQUAD)

    def createFalloutSquad(self, queueType):
        return self._doCreate(PREBATTLE_TYPE.FALLOUT, queueType)

    def createEventSquad(self):
        return self._doCreate(PREBATTLE_TYPE.EVENT)

    def join(self, unitMgrID, slotIdx = UNIT_SLOT.ANY):
        self._callAPI('join', unitMgrID, slotIdx)

    def invite(self, accountsToInvite, comment):
        return self._callUnitAPI('sendInvites', accountsToInvite, comment)

    def setAllRosterSlots(self, *args):
        return self._callUnitAPI('setRosterSlots', *args)

    def leave(self):
        return self._doUnitCmd(CLIENT_UNIT_CMD.LEAVE_UNIT)

    def setVehicle(self, vehInvID = INV_ID_CLEAR_VEHICLE, setReady = False):
        return self._doUnitCmd(CLIENT_UNIT_CMD.SET_UNIT_VEHICLE, vehInvID, int(setReady))

    def setVehicleType(self, vehTypeCompDescr = INV_ID_CLEAR_VEHICLE, vehLevel = 0):
        return self._doUnitCmd(CLIENT_UNIT_CMD.SET_UNIT_VEHICLE_TYPE, vehTypeCompDescr, vehLevel)

    def setMember(self, vehInvID, slotIdx = UNIT_SLOT.ANY):
        return self._doUnitCmd(CLIENT_UNIT_CMD.SET_UNIT_MEMBER, vehInvID, slotIdx)

    def fit(self, playerID, slotIdx = UNIT_SLOT.ANY):
        return self._doUnitCmd(CLIENT_UNIT_CMD.FIT_UNIT_MEMBER, playerID, slotIdx)

    def unfit(self, playerID):
        return self._doUnitCmd(CLIENT_UNIT_CMD.FIT_UNIT_MEMBER, playerID, UNIT_SLOT.REMOVE)

    def assign(self, playerID, slotIdx):
        return self._doUnitCmd(CLIENT_UNIT_CMD.ASSIGN_UNIT_MEMBER, playerID, slotIdx)

    def unassign(self, playerID):
        return self._doUnitCmd(CLIENT_UNIT_CMD.ASSIGN_UNIT_MEMBER, playerID, UNIT_SLOT.REMOVE)

    def reassign(self, playerID, slotIdx):
        return self._doUnitCmd(CLIENT_UNIT_CMD.REASSIGN_UNIT_MEMBER, playerID, slotIdx)

    def kick(self, playerID):
        return self._doUnitCmd(CLIENT_UNIT_CMD.KICK_UNIT_PLAYER, playerID)

    def setReady(self, isReady = True, resetVehicle = False):
        return self._doUnitCmd(CLIENT_UNIT_CMD.SET_UNIT_MEMBER_READY, int(isReady), int(resetVehicle))

    def setRosterSlot(self, rosterSlotIdx, vehTypeID = None, nationNames = [], levels = (1, 8), vehClassNames = []):
        LOG_DEBUG('setRosterSlot: slot=%s, vehTypeID=%s, nationNames=%s, levels=%s, vehClassNames=%s' % (rosterSlotIdx,
         vehTypeID,
         repr(nationNames),
         repr(levels),
         repr(vehClassNames)))
        rSlot = UnitRosterSlot(vehTypeID, nationNames, levels, vehClassNames)
        return self._doUnitCmd(CLIENT_UNIT_CMD.SET_ROSTER_SLOT, 0, rosterSlotIdx, rSlot.pack())

    def lockUnit(self, isLocked = True):
        return self._doUnitCmd(CLIENT_UNIT_CMD.LOCK_UNIT, int(isLocked))

    def closeSlot(self, slotIdx, isClosed = True):
        return self._doUnitCmd(CLIENT_UNIT_CMD.CLOSE_UNIT_SLOT, int(isClosed), slotIdx)

    def openUnit(self, isOpen = True):
        return self._doUnitCmd(CLIENT_UNIT_CMD.OPEN_UNIT, int(isOpen))

    def setDevMode(self, isDevMode = True):
        if constants.IS_DEVELOPMENT:
            return self._doUnitCmd(CLIENT_UNIT_CMD.SET_UNIT_DEV_MODE, int(isDevMode))

    def startBattle(self, vehInvID = 0, gameplaysMask = None, arenaTypeID = 0):
        if gameplaysMask is not None:
            self.setGameplaysMask(gameplaysMask)
        if arenaTypeID != 0:
            self.setArenaType(arenaTypeID)
        return self._doUnitCmd(CLIENT_UNIT_CMD.START_UNIT_BATTLE, vehInvID)

    def stopBattle(self):
        return self._doUnitCmd(CLIENT_UNIT_CMD.STOP_UNIT_BATTLE)

    def startAutoSearch(self):
        return self._doUnitCmd(CLIENT_UNIT_CMD.START_AUTO_SEARCH)

    def stopAutoSearch(self):
        return self._doUnitCmd(CLIENT_UNIT_CMD.STOP_AUTO_SEARCH)

    def setComment(self, strComment):
        return self._doUnitCmd(CLIENT_UNIT_CMD.SET_UNIT_COMMENT, 0, 0, strComment)

    def giveLeadership(self, memberDBID):
        return self._doUnitCmd(CLIENT_UNIT_CMD.GIVE_LEADERSHIP, memberDBID)

    def setGameplaysMask(self, gameplaysMask):
        return self._doUnitCmd(CLIENT_UNIT_CMD.SET_GAMEPLAYS_MASK, gameplaysMask)

    def setArenaType(self, arenaTypeID):
        return self._doUnitCmd(CLIENT_UNIT_CMD.SET_ARENA_TYPE, arenaTypeID)

    def setRatedBattle(self, isRatedBattle = True):
        return self._doUnitCmd(CLIENT_UNIT_CMD.SET_RATED_BATTLE, int(isRatedBattle))

    def changeSortieDivision(self, division):
        return self._doUnitCmd(CLIENT_UNIT_CMD.CHANGE_SORTIE_DIVISION, division)

    def setVehicleList(self, vehicleList):
        return self._doUnitCmd(CLIENT_UNIT_CMD.SET_VEHICLE_LIST, 0, 0, ','.join(map(str, vehicleList)))

    def changeFalloutType(self, newQueueType):
        return self._doUnitCmd(CLIENT_UNIT_CMD.CHANGE_FALLOUT_TYPE, newQueueType)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\AccountUnitAPI.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:18 St�edn� Evropa (letn� �as)
