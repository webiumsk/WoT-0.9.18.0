# 2017.05.04 15:21:55 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/prb_control/settings.py
from UnitBase import UNIT_ERROR, UNIT_BROWSER_ERROR, LEADER_SLOT
from constants import PREBATTLE_TYPE, PREBATTLE_INVITE_STATE, QUEUE_TYPE
from prebattle_shared import SETTING_DEFAULTS, PrebattleSettings
from shared_utils import CONST_CONTAINER, BitmaskHelper
VEHICLE_MIN_LEVEL = 1
VEHICLE_MAX_LEVEL = 10
VEHICLE_DEF_LEVEL_RANGE = (VEHICLE_MIN_LEVEL, VEHICLE_MAX_LEVEL)
VEHICLE_LEVELS = range(VEHICLE_MIN_LEVEL, VEHICLE_MAX_LEVEL + 1)
TEAM_MAX_LIMIT = 150
INVITE_COMMENT_MAX_LENGTH = 400
UNIT_COMMENT_MAX_LENGTH = 240
CREATOR_SLOT_INDEX = LEADER_SLOT
CREATOR_ROSTER_SLOT_INDEXES = (0, 1)
UNIT_CLOSED_SLOTS_MASK = 255 - 0
UNIT_CLOSED_SLOT_COST = 1
AUTO_SEARCH_UNITS_ARG_TIME = 5
UNIT_MIN_RECOMMENDED_LEVEL = 40
SANDBOX_MAX_VEHICLE_LEVEL = 2
BATTLES_TO_SELECT_RANDOM_MIN_LIMIT = 10

class CTRL_ENTITY_TYPE(object):
    UNKNOWN = 0
    LEGACY = 1
    UNIT = 2
    PREQUEUE = 3


CTRL_ENTITY_TYPE_NAMES = dict([ (v, k) for k, v in CTRL_ENTITY_TYPE.__dict__.iteritems() if not k.startswith('_') ])

class FUNCTIONAL_FLAG(BitmaskHelper):
    UNDEFINED = 0
    SWITCH = 1
    EXIT = 2
    LOAD_PAGE = 4
    LOAD_WINDOW = 8
    LEGACY_INTRO = 16
    LEGACY_INIT = 32
    LEGACY = 64
    UNIT_INTRO = 128
    UNIT_BROWSER = 256
    UNIT = 512
    PRE_QUEUE_INTRO = 1024
    PRE_QUEUE = 2048
    E_SPORT = 4096
    FORT = 8192
    FALLOUT = 16384
    COMPANY = 32768
    TRAINING = 65536
    BATTLE_SESSION = 131072
    RANDOM = 262144
    EVENT = 524288
    SANDBOX = 1048576
    TUTORIAL = 2097152
    FORT2 = 4194304
    DEFAULT = 8388608
    LEGACY_BITMASK = LEGACY_INTRO | LEGACY
    UNIT_BITMASK = UNIT_INTRO | UNIT_BROWSER | UNIT
    PRE_QUEUE_BITMASK = PRE_QUEUE_INTRO | PRE_QUEUE
    MODES_BITMASK = E_SPORT | FORT | FALLOUT | COMPANY | TRAINING | BATTLE_SESSION | RANDOM | EVENT | SANDBOX | TUTORIAL | FORT2
    SET_GLOBAL_LISTENERS = LEGACY_BITMASK | UNIT_BITMASK | PRE_QUEUE_BITMASK
    RANGE = (UNDEFINED,
     SWITCH,
     EXIT,
     LOAD_PAGE,
     LOAD_WINDOW,
     LEGACY_INTRO,
     LEGACY_INIT,
     LEGACY,
     UNIT_INTRO,
     UNIT_BROWSER,
     UNIT,
     PRE_QUEUE_INTRO,
     PRE_QUEUE,
     E_SPORT,
     FORT,
     FALLOUT,
     COMPANY,
     TRAINING,
     BATTLE_SESSION,
     RANDOM,
     EVENT,
     SANDBOX,
     TUTORIAL,
     FORT2)


_FUNCTIONAL_FLAG_NAMES = dict([ (k, v) for k, v in FUNCTIONAL_FLAG.__dict__.iteritems() if v in FUNCTIONAL_FLAG.RANGE ])

def convertFlagsToNames(flags):
    result = []
    for name, bit in _FUNCTIONAL_FLAG_NAMES.iteritems():
        if flags & bit > 0:
            result.append(name)

    if not result:
        result.append('UNDEFINED')
    return result


IGNORED_UNIT_MGR_ERRORS = (UNIT_ERROR.OK, UNIT_ERROR.REMOVED_PLAYER, UNIT_ERROR.TIMEOUT)
ENTER_UNIT_MGR_ERRORS = (UNIT_ERROR.CANT_FIND_UNIT_MGR, UNIT_ERROR.NO_UNIT_MGR)
IGNORED_UNIT_BROWSER_ERRORS = (UNIT_BROWSER_ERROR.OK,
 UNIT_BROWSER_ERROR.UNSUBSCRIBED,
 UNIT_BROWSER_ERROR.ACCEPT_TIMEOUT,
 UNIT_BROWSER_ERROR.ACCEPT_CANCELED,
 UNIT_BROWSER_ERROR.SEARCH_CANCELED)
UNIT_ERRORS_TRANSLATE_AS_WARNINGS = (UNIT_ERROR.KICKED_PLAYER,
 UNIT_ERROR.KICKED_CANDIDATE,
 UNIT_ERROR.UNIT_ASSEMBLER_TIMEOUT,
 UNIT_ERROR.INVITE_REMOVED,
 UNIT_ERROR.INVITE_REMOVED,
 UNIT_ERROR.ALREADY_INVITED,
 UNIT_ERROR.WAITING_FOR_JOIN,
 UNIT_ERROR.CLAN_CHANGED,
 UNIT_ERROR.FORT_BATTLE_END,
 UNIT_ERROR.CANT_PICK_LEADER,
 UNIT_ERROR.NO_CLAN_MEMBERS)
UNIT_ERROR_NAMES = dict([ (v, k) for k, v in UNIT_ERROR.__dict__.iteritems() ])
UNIT_BROWSER_ERROR_NAMES = dict([ (v, k) for k, v in UNIT_BROWSER_ERROR.__dict__.iteritems() ])

class UNIT_NOTIFICATION_KEY(object):
    PLAYER_OFFLINE = 'playerOffline'
    PLAYER_ONLINE = 'playerOnline'
    PLAYER_ADDED = 'playerAdded'
    PLAYER_REMOVED = 'playerRemoved'
    GIVE_LEADERSHIP = 'giveLeadership'


class PREBATTLE_ACTION_NAME(object):
    UNDEFINED = ''
    RANDOM = 'random'
    TRAININGS_LIST = 'trainingsList'
    COMPANIES_LIST = 'companiesList'
    SPEC_BATTLES_LIST = 'specBattlesList'
    SQUAD = 'squad'
    EVENT_SQUAD = 'eventSquad'
    TOURNAMENT = 'tournament'
    CLAN = 'clan'
    E_SPORT = 'eSport'
    PUBLICS_LIST = 'publicsList'
    FORT = 'fort'
    FORT_BATTLES_LIST = 'fortBattlesList'
    SORTIES_LIST = 'sortiesList'
    BATTLE_TUTORIAL = 'tutorial'
    FALLOUT = 'fallout'
    FALLOUT_CLASSIC = 'falloutClassic'
    FALLOUT_MULTITEAM = 'falloutMultiTeam'
    SANDBOX = 'battleTeaching'
    FORT2 = 'fort2'
    STRONGHOLDS_BATTLES_LIST = 'strongholdsBattlesList'


class PREBATTLE_INIT_STEP:
    SETTING_RECEIVED = 1
    ROSTERS_RECEIVED = 2
    INITED = SETTING_RECEIVED | ROSTERS_RECEIVED


class SELECTOR_BATTLE_TYPES(object):
    UNIT = 'unit'
    HISTORICAL = 'historical'
    SORTIE = 'sortie'


class REQUEST_TYPE(object):
    CREATE, ASSIGN, JOIN, LEAVE, SET_TEAM_STATE, SET_PLAYER_STATE, SWAP_TEAMS, CHANGE_SETTINGS, CHANGE_OPENED, CHANGE_COMMENT, CHANGE_DIVISION, CHANGE_ARENA_VOIP, KICK, SEND_INVITE, PREBATTLES_LIST, LOCK, CLOSE_SLOT, SET_VEHICLE, SET_ROSTERS_SLOTS, AUTO_SEARCH, ACCEPT_SEARCH, DECLINE_SEARCH, BATTLE_QUEUE, CHANGE_UNIT_STATE, UNITS_LIST, UNITS_RECENTER, UNITS_REFRESH, UNITS_NAV_LEFT, UNITS_NAV_RIGHT, CHANGE_USER_STATUS, GIVE_LEADERSHIP, GET_ROSTER, SET_VEHICLE_LIST, CHANGE_FALLOUT_QUEUE_TYPE, QUEUE, DEQUEUE, SET_RESERVE, UPDATE_STRONGHOLD, UNASSIGN, UNSET_RESERVE = range(1, 41)


REQUEST_TYPE_NAMES = dict([ (v, k) for k, v in REQUEST_TYPE.__dict__.iteritems() ])

class PREQUEUE_SETTING_NAME(CONST_CONTAINER):
    BATTLE_ID = 'battleID'
    SELECTED_VEHICLE_ID = 'selectedVehicleID'
    PRICE_INDEX = 'priceIndex'


class PREBATTLE_SETTING_NAME(object):
    CREATOR = 'creator'
    IS_OPENED = 'isOpened'
    COMMENT = 'comment'
    ARENA_TYPE_ID = 'arenaTypeID'
    ROUND_LENGTH = 'roundLength'
    ARENA_VOIP_CHANNELS = 'arenaVoipChannels'
    CURRENT_USER_STATUS = 'currentUserStatus'
    DEFAULT_ROSTER = 'defaultRoster'
    VEHICLE_LOCK_MODE = 'vehicleLockMode'
    DIVISION = 'division'
    START_TIME = 'startTime'
    BATTLES_LIMIT = 'battlesLimit'
    WINS_LIMIT = 'winsLimit'
    EXTRA_DATA = 'extraData'
    LIMITS = 'limits'
    DESTROY_IF_CREATOR_OUT = 'destroyIfCreatorOut'


class PREBATTLE_RESTRICTION(object):
    UNDEFINED = ''
    LIMIT_MIN_COUNT = 'limit/minCount'
    LIMIT_MAX_COUNT = 'limit/maxCount'
    LIMIT_LEVEL = 'limits/level'
    LIMIT_TOTAL_LEVEL = 'limit/totalLevel'
    LIMIT_CLASSES = 'limits/classes'
    LIMIT_CLASS_LEVEL = 'limits/classLevel'
    LIMIT_VEHICLES = 'limits/vehicles'
    LIMIT_NATIONS = 'limits/nations'
    LIMIT_COMPONENTS = 'limits/components'
    LIMIT_AMMO = 'limits/ammo'
    LIMIT_SHELLS = 'limits/shells'
    LIMIT_TAGS = 'limits/tags'
    LIMIT_LIGHT_TANK = 'limits/classes/lightTank'
    LIMIT_MEDIUM_TANK = 'limits/classes/mediumTank'
    LIMIT_HEAVY_TANK = 'limits/classes/heavyTank'
    LIMIT_SPG = 'limits/classes/SPG'
    LIMIT_AT_SPG = 'limits/classes/AT-SPG'
    HAS_PLAYER_IN_BATTLE = 'player/inBattle'
    TEAM_IS_IN_QUEUE = 'team/inQueue'
    PREVIEW_VEHICLE_IS_PRESENT = 'previewVehicle/isPresent'
    VEHICLE_NOT_READY = 'vehicle/notReady'
    VEHICLE_NOT_PRESENT = 'vehicle/notPresent'
    VEHICLE_IN_BATTLE = 'vehicle/inBattle'
    VEHICLE_BROKEN = 'vehicle/broken'
    VEHICLE_GROUP_IS_NOT_READY = 'vehicle/group_is_not_ready'
    VEHICLE_GROUP_MIN = 'vehicle/group_min'
    VEHICLE_GROUP_REQUIRED = 'vehicle/group_required'
    VEHICLE_ROAMING = 'vehicle/roaming'
    VEHICLE_RENTALS_IS_OVER = 'vehicle/rentalsIsOver'
    VEHICLE_IGR_RENTALS_IS_OVER = 'vehicle/igrRentalsIsOver'
    VEHICLE_IN_PREMIUM_IGR_ONLY = 'vehicle/inPremiumIgrOnly'
    VEHICLE_NOT_SUPPORTED = 'vehicle/not_supported'
    VEHICLE_FALLOUT_ONLY = 'vehicle/fallout_only'
    VEHICLE_ROTATION_GROUP_LOCKED = 'vehicle/rotationGroupLocked'
    CREW_NOT_FULL = 'crew/notFull'
    FALLOUT_NOT_SELECTED = 'fallout/notSelected'
    SERVER_LIMITS = (LIMIT_MIN_COUNT,
     LIMIT_MAX_COUNT,
     LIMIT_LEVEL,
     LIMIT_TOTAL_LEVEL,
     LIMIT_CLASSES,
     LIMIT_CLASS_LEVEL,
     LIMIT_VEHICLES,
     LIMIT_NATIONS,
     LIMIT_COMPONENTS,
     LIMIT_AMMO,
     LIMIT_SHELLS,
     LIMIT_TAGS)
    VEHICLE_CLASS_LIMITS = (('lightTank', LIMIT_LIGHT_TANK),
     ('mediumTank', LIMIT_MEDIUM_TANK),
     ('heavyTank', LIMIT_HEAVY_TANK),
     ('SPG', LIMIT_SPG),
     ('AT-SPG', LIMIT_AT_SPG))
    VEHICLE_INVALID_STATES = (VEHICLE_NOT_READY,
     VEHICLE_NOT_PRESENT,
     VEHICLE_IN_BATTLE,
     VEHICLE_BROKEN,
     VEHICLE_ROAMING,
     VEHICLE_RENTALS_IS_OVER,
     VEHICLE_IGR_RENTALS_IS_OVER,
     VEHICLE_IN_PREMIUM_IGR_ONLY,
     VEHICLE_NOT_SUPPORTED,
     VEHICLE_FALLOUT_ONLY,
     CREW_NOT_FULL)

    @classmethod
    def getVehClassRestrictions(cls):
        return dict(((restriction, tag) for tag, restriction in cls.VEHICLE_CLASS_LIMITS))

    @classmethod
    def getVehClassTags(cls):
        return dict(((tag, restriction) for tag, restriction in cls.VEHICLE_CLASS_LIMITS))

    @classmethod
    def inVehClassLimit(cls, search):
        for tag, restriction in cls.VEHICLE_CLASS_LIMITS:
            if restriction == search:
                return True

        return False


class UNIT_RESTRICTION(object):
    UNDEFINED = 0
    NOT_READY_IN_SLOTS = 1
    MIN_SLOTS = 2
    ZERO_TOTAL_LEVEL = 3
    MIN_TOTAL_LEVEL = 4
    MAX_TOTAL_LEVEL = 5
    INVALID_TOTAL_LEVEL = 6
    NEED_PLAYERS_SEARCH = 7
    IS_IN_IDLE = 8
    IS_IN_ARENA = 9
    UNIT_IS_FULL = 10
    UNIT_IS_LOCKED = 11
    VEHICLE_NOT_SELECTED = 12
    VEHICLE_NOT_VALID = 13
    IS_IN_PRE_ARENA = 15
    NOT_IN_SLOT = 16
    VEHICLE_BROKEN = 17
    VEHICLE_CREW_NOT_FULL = 18
    VEHICLE_RENT_IS_OVER = 19
    VEHICLE_IS_IN_BATTLE = 20
    VEHICLE_NOT_VALID_FOR_EVENT = 21
    CURFEW = 22
    VEHICLE_WRONG_MODE = 23
    FALLOUT_NOT_ENOUGH_PLAYERS = 24
    FALLOUT_VEHICLE_LEVEL_REQUIRED = 25
    FALLOUT_VEHICLE_MIN = 26
    FALLOUT_VEHICLE_MAX = 27
    FALLOUT_VEHICLE_BROKEN = 28
    FORT_DISABLED = 29
    VEHICLE_INVALID_LEVEL = 30
    XP_PENALTY_VEHICLE_LEVELS = 31
    ROTATION_GROUP_LOCKED = 32
    COMMANDER_VEHICLE_NOT_SELECTED = 33
    UNIT_MAINTENANCE = 33
    UNIT_INACTIVE_PERIPHERY_UNDEF = 34
    UNIT_INACTIVE_PERIPHERY_SORTIE = 35
    UNIT_INACTIVE_PERIPHERY_BATTLE = 36
    SPG_IS_FORBIDDEN = 37


class PRE_QUEUE_RESTRICTION:
    LIMIT_LEVEL = 'limits/level'


class PREBATTLE_ROSTER(object):
    UNKNOWN = -1
    ASSIGNED = 0
    UNASSIGNED = 16
    ASSIGNED_IN_TEAM1 = ASSIGNED | 1
    UNASSIGNED_IN_TEAM1 = UNASSIGNED | 1
    ASSIGNED_IN_TEAM2 = ASSIGNED | 2
    UNASSIGNED_IN_TEAM2 = UNASSIGNED | 2
    ALL = (ASSIGNED_IN_TEAM1,
     UNASSIGNED_IN_TEAM1,
     ASSIGNED_IN_TEAM2,
     UNASSIGNED_IN_TEAM2)
    PREBATTLE_RANGES = {PREBATTLE_TYPE.TRAINING: ALL,
     PREBATTLE_TYPE.COMPANY: (ASSIGNED_IN_TEAM1, UNASSIGNED_IN_TEAM1),
     PREBATTLE_TYPE.TOURNAMENT: ALL,
     PREBATTLE_TYPE.CLAN: ALL}

    @classmethod
    def getRange(cls, pbType, team = None):
        result = ()
        if pbType in cls.PREBATTLE_RANGES:
            result = cls.PREBATTLE_RANGES[pbType]
            if team is not None:
                result = filter(lambda r: r & team, result)
        return result


_PREBATTLE_DEFAULT_SETTINGS = SETTING_DEFAULTS
_PREBATTLE_DEFAULT_SETTINGS.update({'limits': {0: {},
            1: {},
            2: {}}})

def makePrebattleSettings(settings = None):
    if not settings:
        settings = _PREBATTLE_DEFAULT_SETTINGS
    return PrebattleSettings(settings)


class FUNCTIONAL_ORDER(object):
    ENTRY = (CTRL_ENTITY_TYPE.PREQUEUE, CTRL_ENTITY_TYPE.LEGACY, CTRL_ENTITY_TYPE.UNIT)
    ACTION = (CTRL_ENTITY_TYPE.UNIT, CTRL_ENTITY_TYPE.PREQUEUE, CTRL_ENTITY_TYPE.LEGACY)
    EXIT_FROM_QUEUE = (CTRL_ENTITY_TYPE.LEGACY, CTRL_ENTITY_TYPE.PREQUEUE, CTRL_ENTITY_TYPE.UNIT)
    BEFORE_GENERAL_CHECKING = (CTRL_ENTITY_TYPE.PREQUEUE,)
    AFTER_GENERAL_CHECKING = (CTRL_ENTITY_TYPE.UNIT, CTRL_ENTITY_TYPE.LEGACY)


class PRB_INVITE_STATE(CONST_CONTAINER):
    ERROR = -1
    PENDING = 0
    ACCEPTED = 1
    DECLINED = 2
    REVOKED = 3
    EXPIRED = 4
    OLD_MAPPING = {PREBATTLE_INVITE_STATE.ACTIVE: PENDING,
     PREBATTLE_INVITE_STATE.ACCEPTED: ACCEPTED,
     PREBATTLE_INVITE_STATE.DECLINED: DECLINED,
     PREBATTLE_INVITE_STATE.EXPIRED: EXPIRED}

    @classmethod
    def getFromOldState(cls, invite):
        return cls.OLD_MAPPING.get(invite.state, cls.ERROR)

    @classmethod
    def getFromNewState(cls, invite):
        if invite.isExpired():
            return cls.EXPIRED
        return invite.state


class PREBATTLE_PLAYERS_COMPARATORS:
    REGULAR = 1
    OBSERVERS_TO_BOTTOM = 2
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\settings.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:55 St�edn� Evropa (letn� �as)