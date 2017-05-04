# 2017.05.04 15:21:13 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/battle_control/controllers/msgs_ctrl.py
import weakref
import BattleReplay
import BigWorld
import Event
from ReplayEvents import g_replayEvents
from constants import ATTACK_REASON_INDICES as _AR_INDICES
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.battle_control.controllers.interfaces import IBattleController

class _ENTITY_TYPE(object):
    UNKNOWN = 'unknown'
    SELF = 'self'
    ALLY = 'ally'
    ENEMY = 'enemy'
    SUICIDE = 'suicide'


_ATTACK_REASON_CODE = {_AR_INDICES['shot']: 'DEATH_FROM_SHOT',
 _AR_INDICES['fire']: 'DEATH_FROM_SHOT',
 _AR_INDICES['ramming']: 'DEATH_FROM_RAMMING',
 _AR_INDICES['world_collision']: 'DEATH_FROM_WORLD_COLLISION',
 _AR_INDICES['death_zone']: 'DEATH_FROM_DEATH_ZONE',
 _AR_INDICES['drowning']: 'DEATH_FROM_DROWNING',
 _AR_INDICES['gas_attack']: 'DEATH_FROM_GAS_ATTACK',
 _AR_INDICES['overturn']: 'DEATH_FROM_OVERTURN'}
_PLAYER_KILL_ENEMY_SOUND = 'enemy_killed_by_player'
_PLAYER_KILL_ALLY_SOUND = 'ally_killed_by_player'
_ALLY_KILLED_SOUND = 'ally_killed_by_enemy'

class BattleMessagesController(IBattleController):
    __slots__ = ('__battleCtx', '__eManager', '_buffer', '_isUIPopulated', 'onShowVehicleMessageByCode', 'onShowVehicleMessageByKey', 'onShowVehicleErrorByKey', 'onShowPlayerMessageByCode', 'onShowPlayerMessageByKey', '__weakref__')

    def __init__(self, setup):
        self.__battleCtx = weakref.proxy(setup.battleCtx)
        self.__eManager = Event.EventManager()
        self.onShowVehicleMessageByCode = Event.Event(self.__eManager)
        self.onShowVehicleMessageByKey = Event.Event(self.__eManager)
        self.onShowVehicleErrorByKey = Event.Event(self.__eManager)
        self.onShowPlayerMessageByCode = Event.Event(self.__eManager)
        self.onShowPlayerMessageByKey = Event.Event(self.__eManager)
        self._buffer = []
        self._isUIPopulated = False

    def getControllerID(self):
        return BATTLE_CTRL_ID.MESSAGES

    def startControl(self):
        pass

    def stopControl(self):
        self.__eManager.clear()
        self.__battleCtx = None
        return

    def showVehicleKilledMessage(self, avatar, targetID, attackerID, equipmentID, reason):
        """
        This message will be called for every client (from Arena), without any exceptions.
        @param avatar: instance of client/Avatar
        @param targetID: the killed vehicle
        @param attackerID: killer's vehicle ID
        @param equipmentID: equipment ID (for example, a consumable)
        @param reason: see ATTACK_REASON in constants
        """
        try:
            playerVehicleID = avatar.playerVehicleID
        except AttributeError:
            return

        isMyVehicle = targetID == playerVehicleID
        if isMyVehicle:
            return
        elif targetID == attackerID and self.__battleCtx.isObserver(targetID):
            return
        else:
            if not avatar.isVehicleAlive:
                if avatar.isObserver() and targetID == avatar.observedVehicleID:
                    return
                if targetID == avatar.inputHandler.ctrl.curVehicleID:
                    return
            code, postfix, sound, soundExt = self.__getKillInfo(avatar, targetID, attackerID, equipmentID, reason)
            if sound is not None:
                avatar.soundNotifications.play(sound)
            if soundExt is not None:
                avatar.soundNotifications.play(soundExt)
            self.onShowPlayerMessageByCode(code, postfix, targetID, attackerID, equipmentID)
            return

    def showVehicleDamageInfo(self, avatar, code, targetID, entityID, extra, equipmentID):
        """
        This message always will be called for player's vehicle of vehicle we are
        watching for.
        @param avatar: instance of client/Avatar
        @param code:
        @param targetID: the killed vehicle
        @param entityID: killer's vehicle ID
        @param extra: vehicle extra
        @param equipmentID: equipment ID (for example, a consumable)
        """
        code, postfix = self.__getDamageInfo(avatar, code, entityID, targetID)
        self.onShowPlayerMessageByCode(code, postfix, targetID, entityID, equipmentID)
        self.onShowVehicleMessageByCode(code, postfix, entityID, extra, equipmentID)

    def showVehicleMessage(self, key, args = None):
        self.onShowVehicleMessageByKey(key, args, None)
        return

    def showVehicleError(self, key, args = None):
        self.onShowVehicleErrorByKey(key, args, None)
        return

    def showAllyHitMessage(self, vehicleID = None):
        self.onShowPlayerMessageByKey('ALLY_HIT', {'entity': self.__battleCtx.getPlayerFullName(vID=vehicleID)}, (('entity', vehicleID),))

    def __getEntityString(self, avatar, entityID):
        if entityID == avatar.playerVehicleID:
            return _ENTITY_TYPE.SELF
        elif self.__battleCtx.isAlly(entityID):
            return _ENTITY_TYPE.ALLY
        elif self.__battleCtx.isEnemy(entityID):
            return _ENTITY_TYPE.ENEMY
        else:
            return _ENTITY_TYPE.UNKNOWN

    def __getDamageInfo(self, avatar, code, entityID, targetID):
        target = self.__getEntityString(avatar, targetID)
        if not entityID or entityID == targetID:
            postfix = '%s_%s' % (target.upper(), _ENTITY_TYPE.SUICIDE.upper())
        else:
            entity = self.__getEntityString(avatar, entityID)
            postfix = '%s_%s' % (entity.upper(), target.upper())
        return (code, postfix)

    def __getKillInfo(self, avatar, targetID, attackerID, equipmentID, reason):
        attacker = self.__getEntityString(avatar, attackerID)
        target = _ENTITY_TYPE.SUICIDE
        if targetID != attackerID:
            target = self.__getEntityString(avatar, targetID)
        code = _ATTACK_REASON_CODE.get(reason)
        sound = None
        soundExt = None
        if attackerID == BigWorld.player().playerVehicleID:
            if target == _ENTITY_TYPE.ENEMY:
                sound = _PLAYER_KILL_ENEMY_SOUND
            elif target == _ENTITY_TYPE.ALLY:
                sound = _PLAYER_KILL_ALLY_SOUND
                soundExt = _ALLY_KILLED_SOUND
        elif target == _ENTITY_TYPE.ALLY or target == _ENTITY_TYPE.SUICIDE and attacker == _ENTITY_TYPE.ALLY:
            soundExt = _ALLY_KILLED_SOUND
        return (code,
         '%s_%s' % (attacker.upper(), target.upper()),
         sound,
         soundExt)

    def onUIPopulated(self):
        self._isUIPopulated = True
        for args in self._buffer:
            self.onShowVehicleMessageByKey(*args)


class BattleMessagesPlayer(BattleMessagesController):

    def startControl(self):
        super(BattleMessagesPlayer, self).startControl()
        g_replayEvents.onWatcherNotify += self.__onWatcherNotify

    def stopControl(self):
        g_replayEvents.onWatcherNotify -= self.__onWatcherNotify
        super(BattleMessagesPlayer, self).stopControl()

    def showVehicleKilledMessage(self, avatar, targetID, attackerID, equipmentID, reason):
        if BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            return
        super(BattleMessagesPlayer, self).showVehicleKilledMessage(avatar, targetID, attackerID, equipmentID, reason)

    def showVehicleDamageInfo(self, avatar, code, targetID, entityID, extra, equipmentID):
        if BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            return
        super(BattleMessagesPlayer, self).showVehicleDamageInfo(avatar, code, targetID, entityID, extra, equipmentID)

    def showVehicleMessage(self, key, args = None):
        if BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            return
        super(BattleMessagesPlayer, self).showVehicleMessage(key, args)

    def showVehicleError(self, key, args = None):
        if BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            return
        super(BattleMessagesPlayer, self).showVehicleError(key, args)

    def showAllyHitMessage(self, vehicleID = None):
        if BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            return
        super(BattleMessagesPlayer, self).showAllyHitMessage(vehicleID)

    def showInfoMessage(self, key, withBuffer = False, args = None):
        if withBuffer and not self._isUIPopulated:
            self._buffer.append((key, args))
        else:
            super(BattleMessagesPlayer, self).showVehicleMessage(key, args)

    def __onWatcherNotify(self, message, args):
        self.showInfoMessage(message, withBuffer=True, args=args)


def createBattleMessagesCtrl(setup):
    if setup.isReplayPlaying:
        ctrl = BattleMessagesPlayer(setup)
    else:
        ctrl = BattleMessagesController(setup)
    return ctrl
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\battle_control\controllers\msgs_ctrl.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:13 St�edn� Evropa (letn� �as)
