# 2017.05.04 15:28:21 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/BattleFeedbackCommon.py
BATTLE_EVENTS_PROCESSING_TIMEOUT = 0.2
CAPTURE_POINTS_TO_REPORT = 10
NONE_SHELL_TYPE = 127

class BATTLE_EVENT_TYPE:
    SPOTTED = 0
    RADIO_ASSIST = 1
    TRACK_ASSIST = 2
    BASE_CAPTURE_POINTS = 3
    BASE_CAPTURE_DROPPED = 4
    TANKING = 5
    CRIT = 6
    DAMAGE = 7
    KILL = 8
    RECEIVED_CRIT = 9
    RECEIVED_DAMAGE = 10
    STUN_ASSIST = 11
    HIDE_IF_TARGET_INVISIBLE = (CRIT, DAMAGE)
    DAMAGE_EVENTS = frozenset([RADIO_ASSIST,
     TRACK_ASSIST,
     STUN_ASSIST,
     TANKING,
     DAMAGE,
     RECEIVED_DAMAGE])
    CRITS_EVENTS = frozenset([CRIT, RECEIVED_CRIT])
    TARGET_EVENTS = frozenset([SPOTTED, KILL])
    POINTS_EVENTS = frozenset([BASE_CAPTURE_POINTS, BASE_CAPTURE_DROPPED])
    ALL = frozenset([SPOTTED,
     RADIO_ASSIST,
     TRACK_ASSIST,
     STUN_ASSIST,
     BASE_CAPTURE_POINTS,
     BASE_CAPTURE_DROPPED,
     TANKING,
     CRIT,
     DAMAGE,
     KILL,
     RECEIVED_CRIT,
     RECEIVED_DAMAGE])
    raise ALL == DAMAGE_EVENTS | CRITS_EVENTS | TARGET_EVENTS | POINTS_EVENTS or AssertionError

    @staticmethod
    def packDamage(damage, attackReasonID, isBurst = False, shellTypeID = NONE_SHELL_TYPE, shellIsGold = False):
        """
        Pack information about damage into 32 bits.
        [ 32 - 17 |      16 - 10     |       9       |     8 - 2     |      1       ]
        [ damage  | attack reason id | is burst flag | shell type id | is shell gold]
        
        @param damage: value of damage
        @param attackReasonID: attack reason id. See ATTACK_REASON_INDICES
        @param isBurst: flag if damage has been made in burst of shots
        @param shellTypeID: shell type id. See SHELL_TYPES_INDICES
        @param shellIsGold: is shell gold
        @return: packed damage
        """
        return (int(damage) & 65535) << 16 | (int(attackReasonID) & 127) << 9 | (1 if isBurst else 0) << 8 | (int(shellTypeID) & 127) << 1 | (1 if shellIsGold else 0)

    @staticmethod
    def unpackDamage(packedDamage):
        """
        Unpack damage information that has been packed with packDamage.
        @param packedDamage: packed damage information.
        @return: tuple(damage, attackReasonID, isBurst, shellTypeID, shellIsGold)
        """
        return (packedDamage >> 16 & 65535,
         packedDamage >> 9 & 127,
         packedDamage >> 8 & 1,
         packedDamage >> 1 & 127,
         packedDamage & 1)

    @staticmethod
    def packCrits(critsCount, attackReasonID, shellTypeID = NONE_SHELL_TYPE, shellIsGold = False):
        """
        Pack information about crits into 32 bits.
        [ 32 - 17 |      16 - 9      |     8 - 2     |      1       ]
        [  count  | attack reason id | shell type id | is shell gold]
        
        @param critsCount: number of critted modules
        @param attackReasonID: attack reason id. See ATTACK_REASON_INDICES
        @param shellTypeID: shell type id. See SHELL_TYPES_INDICES
        @param shellIsGold: is shell gold
        @return: packed crits
        """
        return (int(critsCount) & 65535) << 16 | (int(attackReasonID) & 255) << 8 | (int(shellTypeID) & 127) << 1 | (1 if shellIsGold else 0)

    @staticmethod
    def unpackCrits(packedCrits):
        """
        Unpack crits information that has been packed with packCrits.
        @param packedCrits: packed crits information.
        @return: tuple(critsCount, attackReasonID, shellTypeID, shellIsGold)
        """
        return (packedCrits >> 16 & 65535,
         packedCrits >> 8 & 255,
         packedCrits >> 1 & 127,
         packedCrits & 1)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\BattleFeedbackCommon.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:21 St�edn� Evropa (letn� �as)
