# 2017.05.04 15:21:11 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/battle_control/controllers/feedback_events.py
from BattleFeedbackCommon import BATTLE_EVENT_TYPE as _BET, NONE_SHELL_TYPE
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as _FET
from constants import ATTACK_REASON, ATTACK_REASONS, SHELL_TYPES_LIST

def _unpackDamage(packedData):
    return _DamageExtra(*_BET.unpackDamage(packedData))


def _unpackCrits(packedData):
    return _CritsExtra(*_BET.unpackCrits(packedData))


def _unpackInteger(packedData):
    return packedData


_BATTLE_EVENT_TO_PLAYER_FEEDBACK_EVENT = {_BET.KILL: _FET.PLAYER_KILLED_ENEMY,
 _BET.DAMAGE: _FET.PLAYER_DAMAGED_HP_ENEMY,
 _BET.CRIT: _FET.PLAYER_DAMAGED_DEVICE_ENEMY,
 _BET.SPOTTED: _FET.PLAYER_SPOTTED_ENEMY,
 _BET.RADIO_ASSIST: _FET.PLAYER_ASSIST_TO_KILL_ENEMY,
 _BET.TRACK_ASSIST: _FET.PLAYER_ASSIST_TO_KILL_ENEMY,
 _BET.STUN_ASSIST: _FET.PLAYER_ASSIST_TO_STUN_ENEMY,
 _BET.BASE_CAPTURE_POINTS: _FET.PLAYER_CAPTURED_BASE,
 _BET.BASE_CAPTURE_DROPPED: _FET.PLAYER_DROPPED_CAPTURE,
 _BET.TANKING: _FET.PLAYER_USED_ARMOR,
 _BET.RECEIVED_DAMAGE: _FET.ENEMY_DAMAGED_HP_PLAYER,
 _BET.RECEIVED_CRIT: _FET.ENEMY_DAMAGED_DEVICE_PLAYER}
_PLAYER_FEEDBACK_EXTRA_DATA_CONVERTERS = {_FET.PLAYER_DAMAGED_HP_ENEMY: _unpackDamage,
 _FET.PLAYER_ASSIST_TO_KILL_ENEMY: _unpackDamage,
 _FET.PLAYER_CAPTURED_BASE: _unpackInteger,
 _FET.PLAYER_DROPPED_CAPTURE: _unpackInteger,
 _FET.PLAYER_USED_ARMOR: _unpackDamage,
 _FET.PLAYER_DAMAGED_DEVICE_ENEMY: _unpackCrits,
 _FET.ENEMY_DAMAGED_HP_PLAYER: _unpackDamage,
 _FET.ENEMY_DAMAGED_DEVICE_PLAYER: _unpackCrits,
 _FET.PLAYER_ASSIST_TO_STUN_ENEMY: _unpackDamage}

def _getShellType(shellTypeID):
    """
    Returns shell type (see SHELL_TYPES) or None if shellTypeID == _BET.NONE_SHELL_TYPE.
    :param shellTypeID: int, shell type index
    """
    if shellTypeID == NONE_SHELL_TYPE:
        return None
    else:
        return SHELL_TYPES_LIST[shellTypeID]


class _DamageExtra(object):
    __slots__ = ('__damage', '__attackReasonID', '__isBurst', '__shellType', '__isShellGold')

    def __init__(self, damage = 0, attackReasonID = 0, isBurst = False, shellTypeID = NONE_SHELL_TYPE, shellIsGold = False):
        super(_DamageExtra, self).__init__()
        self.__damage = damage
        self.__attackReasonID = attackReasonID
        self.__isBurst = bool(isBurst)
        self.__shellType = _getShellType(shellTypeID)
        self.__isShellGold = bool(shellIsGold)

    def getDamage(self):
        """
        Returns damage.
        """
        return self.__damage

    def getAttackReasonID(self):
        """
        Return attack reason ID. For details please see ATTACK_REASONS.
        """
        return self.__attackReasonID

    def getShellType(self):
        """
        Returns shell type (see SHELL_TYPES enum) or None, if shell type is not defined.
        """
        return self.__shellType

    def isBurst(self):
        return self.__isBurst

    def isShellGold(self):
        return self.__isShellGold

    def isFire(self):
        return self.isAttackReason(ATTACK_REASON.FIRE)

    def isRam(self):
        return self.isAttackReason(ATTACK_REASON.RAM)

    def isShot(self):
        return self.isAttackReason(ATTACK_REASON.SHOT)

    def isWorldCollision(self):
        return self.isAttackReason(ATTACK_REASON.WORLD_COLLISION)

    def isAttackReason(self, attackReason):
        return ATTACK_REASONS[self.__attackReasonID] == attackReason


class _CritsExtra(object):
    __slots__ = ('__critsCount', '__shellType', '__isShellGold', '__attackReasonID')

    def __init__(self, critsCount = 0, attackReasonID = 0, shellTypeID = NONE_SHELL_TYPE, shellIsGold = False):
        super(_CritsExtra, self).__init__()
        self.__critsCount = critsCount
        self.__attackReasonID = attackReasonID
        self.__shellType = _getShellType(shellTypeID)
        self.__isShellGold = bool(shellIsGold)

    def getCritsCount(self):
        """
        Returns count of damaged modules and tankmans.
        """
        return self.__critsCount

    def getShellType(self):
        """
        Returns shell type (see SHELL_TYPES enum) or None, if shell type is not defined.
        """
        return self.__shellType

    def isShellGold(self):
        return self.__isShellGold

    def isFire(self):
        return self.isAttackReason(ATTACK_REASON.FIRE)

    def isRam(self):
        return self.isAttackReason(ATTACK_REASON.RAM)

    def isShot(self):
        return self.isAttackReason(ATTACK_REASON.SHOT)

    def isWorldCollision(self):
        return self.isAttackReason(ATTACK_REASON.WORLD_COLLISION)

    def isAttackReason(self, attackReason):
        return ATTACK_REASONS[self.__attackReasonID] == attackReason


class _FeedbackEvent(object):
    __slots__ = ('__eventType',)

    def __init__(self, feedbackEventType):
        super(_FeedbackEvent, self).__init__()
        self.__eventType = feedbackEventType

    def getType(self):
        """
        Returns type of feedback event. For details see FEEDBACK_EVENT_ID.
        """
        return self.__eventType

    @staticmethod
    def fromDict(summaryData):
        raise NotImplementedError


class PlayerFeedbackEvent(_FeedbackEvent):
    __slots__ = ('__battleEventType', '__targetID', '__count', '__extra', '__attackReasonID', '__isBurst')

    def __init__(self, feedbackEventType, eventType, targetID, extra, count):
        """
        """
        super(PlayerFeedbackEvent, self).__init__(feedbackEventType)
        self.__battleEventType = eventType
        self.__targetID = targetID
        self.__count = count
        self.__extra = extra

    @staticmethod
    def fromDict(battleEventData):
        battleEventType = battleEventData['eventType']
        if battleEventType in _BATTLE_EVENT_TO_PLAYER_FEEDBACK_EVENT:
            feedbackEventType = _BATTLE_EVENT_TO_PLAYER_FEEDBACK_EVENT[battleEventType]
            if feedbackEventType in _PLAYER_FEEDBACK_EXTRA_DATA_CONVERTERS:
                converter = _PLAYER_FEEDBACK_EXTRA_DATA_CONVERTERS[feedbackEventType]
                extra = converter(battleEventData['details'])
            else:
                extra = None
            return PlayerFeedbackEvent(feedbackEventType, battleEventData['eventType'], battleEventData['targetID'], extra, battleEventData['count'])
        else:
            return

    def getBattleEventType(self):
        """
        Returns type of battle event. For details see BATTLE_EVENT_TYPE.
        """
        return self.__battleEventType

    def getTargetID(self):
        """
        Returns target vehicle ID.
        """
        return self.__targetID

    def getExtra(self):
        """
        Returns an extra that depends on event type. For details see
        PLAYER_FEEDBACK_EXTRA_DATA_CONVERTERS.
        """
        return self.__extra

    def getCount(self):
        """
        Returns count of events aggregated on the server side.
        """
        return self.__count


class BattleSummaryFeedbackEvent(_FeedbackEvent):
    __slots__ = ('__damage', '__trackAssistDamage', '__radioAssistDamage', '__blockedDamage', '__stunAssist')

    def __init__(self, damage, trackAssist, radioAssist, tankings, stunAssist):
        super(BattleSummaryFeedbackEvent, self).__init__(_FET.DAMAGE_LOG_SUMMARY)
        self.__damage = damage
        self.__trackAssistDamage = trackAssist
        self.__radioAssistDamage = radioAssist
        self.__blockedDamage = tankings
        self.__stunAssist = stunAssist

    @staticmethod
    def fromDict(summaryData):
        return BattleSummaryFeedbackEvent(damage=summaryData['damage'], trackAssist=summaryData['trackAssist'], radioAssist=summaryData['radioAssist'], tankings=summaryData['tankings'], stunAssist=summaryData['stunAssist'])

    def getTotalDamage(self):
        return self.__damage

    def getTotalAssistDamage(self):
        return self.__trackAssistDamage + self.__radioAssistDamage

    def getTotalBlockedDamage(self):
        return self.__blockedDamage

    def getTotalStunDamage(self):
        return self.__stunAssist


class PostmortemSummaryEvent(_FeedbackEvent):
    __slots__ = ('__killerID', '__deathReasonID')

    def __init__(self, lastKillerID, lastDeathReasonID):
        super(PostmortemSummaryEvent, self).__init__(_FET.POSTMORTEM_SUMMARY)
        self.__killerID = lastKillerID
        self.__deathReasonID = lastDeathReasonID

    @staticmethod
    def fromDict(summaryData):
        return PostmortemSummaryEvent(lastKillerID=summaryData['lastKillerID'], lastDeathReasonID=summaryData['lastDeathReasonID'])

    def getKillerID(self):
        return self.__killerID

    def getDeathReasonID(self):
        return self.__deathReasonID
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\battle_control\controllers\feedback_events.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:12 St�edn� Evropa (letn� �as)
