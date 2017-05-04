# 2017.05.04 15:28:27 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/constants.py
import math
try:
    import BigWorld
    if BigWorld.component in ('web', 'Unknown'):
        raise Exception
except:
    IS_CLIENT = False
    IS_CELLAPP = False
    IS_BASEAPP = False
    IS_WEB = True
    IS_BOT = False
else:
    IS_CLIENT = BigWorld.component == 'client'
    IS_BOT = BigWorld.component == 'bot'
    IS_CELLAPP = BigWorld.component == 'cell'
    IS_BASEAPP = BigWorld.component in ('base', 'service')
    IS_WEB = False

CURRENT_REALM = 'EU'
DEFAULT_LANGUAGE = 'ru'
AUTH_REALM = 'RU'
IS_DEVELOPMENT = CURRENT_REALM == 'DEV'
IS_CHINA = CURRENT_REALM == 'CN'
IS_KOREA = CURRENT_REALM == 'KR'
IS_SINGAPORE = CURRENT_REALM == 'ASIA'
IS_SANDBOX = CURRENT_REALM == 'SB'
IS_QUALIFIERS_ENABLED = False
if CURRENT_REALM == 'NA':
    DEFAULT_LANGUAGE = 'en'
    AUTH_REALM = 'NA'
elif CURRENT_REALM == 'EU':
    DEFAULT_LANGUAGE = 'en'
    AUTH_REALM = 'EU'
elif CURRENT_REALM == 'ASIA':
    DEFAULT_LANGUAGE = 'en'
    AUTH_REALM = 'ASIA'
elif CURRENT_REALM == 'CN':
    DEFAULT_LANGUAGE = 'cn'
    AUTH_REALM = 'CN'
    IS_RENTALS_ENABLED = True
elif CURRENT_REALM == 'KR':
    DEFAULT_LANGUAGE = 'ko'
    AUTH_REALM = 'KR'
elif CURRENT_REALM == 'CT':
    AUTH_REALM = 'CT'
elif CURRENT_REALM in ('RU', 'ST', 'QA', 'DEV', 'SB'):
    pass
else:
    raise False or AssertionError
SPECIAL_OL_FILTER = IS_KOREA or IS_SINGAPORE
IS_RENTALS_ENABLED = IS_CHINA
if not sum([IS_CHINA, IS_KOREA, IS_SINGAPORE]) <= 1:
    raise AssertionError
    IS_SHOW_SERVER_STATS = not IS_CHINA
    IS_CAT_LOADED = False
    IS_TUTORIAL_ENABLED = True
    LEAKS_DETECTOR_MAX_EXECUTION_TIME = 2.0
    IS_IGR_ENABLED = IS_KOREA or IS_CHINA
    SERVER_TICK_LENGTH = 0.1
    SHELL_TRAJECTORY_EPSILON_CLIENT = 0.03
    SHELL_TRAJECTORY_EPSILON_SERVER = 0.1
    ARENA_TYPE_XML_PATH = 'scripts/arena_defs/'
    ITEM_DEFS_PATH = 'scripts/item_defs/'
    VOICE_CHAT_INIT_TIMEOUT = 10
    MAX_OPENED_ANOTHER_DOSSIERS = 4
    ENABLE_DEBUG_DYNAMICS_INFO = False
    if IS_CLIENT:
        import ResMgr
        IS_CLIENT_BUILD = not ResMgr.isFile('version.xml')
    else:
        IS_CLIENT_BUILD = False
    HAS_DEV_RESOURCES = IS_DEVELOPMENT and not IS_CLIENT_BUILD

    class SPT_MATKIND:
        SOLID = 71
        LEAVES = 72


    class DESTRUCTIBLE_MATKIND:
        MIN = 71
        MAX = 100
        NORMAL_MIN = 73
        NORMAL_MAX = 86
        DAMAGED_MIN = 87
        DAMAGED_MAX = 100


    class DOSSIER_TYPE:
        ACCOUNT = 1
        VEHICLE = 2
        TANKMAN = 4
        FORTIFIED_REGIONS = 8
        RATED7X7 = 16
        CLUB = 32
        CLAN = 64


    ARENA_GAMEPLAY_NAMES = ('ctf', 'domination', 'assault', 'nations', 'ctf2', 'domination2', 'assault2', 'fallout', 'fallout2', 'fallout3', 'fallout4', 'fallout5', 'fallout6', 'sandbox')
    ARENA_GAMEPLAY_IDS = dict(((value, index) for index, value in enumerate(ARENA_GAMEPLAY_NAMES)))

    class ARENA_GUI_TYPE:
        UNKNOWN = 0
        RANDOM = 1
        TRAINING = 2
        COMPANY = 3
        TUTORIAL = 4
        CYBERSPORT = 5
        FALLOUT = 6
        EVENT_BATTLES = 7
        SORTIE = 8
        FORT_BATTLE = 9
        RATED_CYBERSPORT = 10
        RATED_SANDBOX = 11
        SANDBOX = 12
        FALLOUT_CLASSIC = 13
        FALLOUT_MULTITEAM = 14
        SORTIE_2 = 15
        FORT_BATTLE_2 = 16
        RANGE = (UNKNOWN,
         RANDOM,
         TRAINING,
         COMPANY,
         TUTORIAL,
         CYBERSPORT,
         FALLOUT,
         EVENT_BATTLES,
         SORTIE,
         FORT_BATTLE,
         RATED_CYBERSPORT,
         RATED_SANDBOX,
         SANDBOX,
         FALLOUT_CLASSIC,
         FALLOUT_MULTITEAM,
         SORTIE_2,
         FORT_BATTLE_2)
        SANDBOX_RANGE = (SANDBOX, RATED_SANDBOX)
        FALLOUT_RANGE = (FALLOUT_CLASSIC, FALLOUT_MULTITEAM)


    class ARENA_GUI_TYPE_LABEL:
        LABELS = {ARENA_GUI_TYPE.UNKNOWN: 'special',
         ARENA_GUI_TYPE.RANDOM: 'random',
         ARENA_GUI_TYPE.TRAINING: 'training',
         ARENA_GUI_TYPE.COMPANY: 'team',
         ARENA_GUI_TYPE.TUTORIAL: 'tutorial',
         ARENA_GUI_TYPE.CYBERSPORT: 'team7x7',
         ARENA_GUI_TYPE.EVENT_BATTLES: 'event',
         ARENA_GUI_TYPE.SORTIE: 'fortifications',
         ARENA_GUI_TYPE.FORT_BATTLE: 'fortifications',
         ARENA_GUI_TYPE.RATED_CYBERSPORT: 'team7x7',
         ARENA_GUI_TYPE.RATED_SANDBOX: 'ratedsandbox',
         ARENA_GUI_TYPE.SANDBOX: 'sandbox',
         ARENA_GUI_TYPE.FALLOUT_CLASSIC: 'fallout_classic',
         ARENA_GUI_TYPE.FALLOUT_MULTITEAM: 'fallout_multiteam',
         ARENA_GUI_TYPE.SORTIE_2: 'fortifications',
         ARENA_GUI_TYPE.FORT_BATTLE_2: 'fortifications'}


    class ARENA_BONUS_TYPE:
        UNKNOWN = 0
        REGULAR = 1
        TRAINING = 2
        COMPANY = 3
        TOURNAMENT = 4
        CLAN = 5
        TUTORIAL = 6
        CYBERSPORT = 7
        EVENT_BATTLES = 9
        SORTIE = 10
        FORT_BATTLE = 11
        RATED_CYBERSPORT = 12
        GLOBAL_MAP = 13
        TOURNAMENT_REGULAR = 14
        TOURNAMENT_CLAN = 15
        RATED_SANDBOX = 16
        SANDBOX = 17
        FALLOUT_CLASSIC = 18
        FALLOUT_MULTITEAM = 19
        SORTIE_2 = 20
        FORT_BATTLE_2 = 21
        RANGE = (UNKNOWN,
         REGULAR,
         TRAINING,
         COMPANY,
         TOURNAMENT,
         CLAN,
         TUTORIAL,
         CYBERSPORT,
         EVENT_BATTLES,
         SORTIE,
         FORT_BATTLE,
         RATED_CYBERSPORT,
         GLOBAL_MAP,
         TOURNAMENT_REGULAR,
         TOURNAMENT_CLAN,
         RATED_SANDBOX,
         SANDBOX,
         FALLOUT_CLASSIC,
         FALLOUT_MULTITEAM,
         SORTIE_2,
         FORT_BATTLE_2)
        SANDBOX_RANGE = (RATED_SANDBOX, SANDBOX)
        FALLOUT_RANGE = (FALLOUT_CLASSIC, FALLOUT_MULTITEAM)
        EXTERNAL_RANGE = (SORTIE,
         FORT_BATTLE,
         SORTIE_2,
         FORT_BATTLE_2,
         GLOBAL_MAP,
         TOURNAMENT,
         TOURNAMENT_CLAN,
         TOURNAMENT_REGULAR)


    class ARENA_BONUS_MASK:
        TYPE_BITS = dict(((name, 2 ** id) for id, name in enumerate(ARENA_BONUS_TYPE.RANGE[1:])))
        ANY = 2147483647

        @staticmethod
        def mask(*args):
            return reduce(lambda v, x: v | x, [ ARENA_BONUS_MASK.TYPE_BITS[arg] for arg in args ])

        @staticmethod
        def exclude(*args):
            return reduce(lambda v, x: v & ~x, [ ARENA_BONUS_MASK.TYPE_BITS[arg] for arg in args ], ARENA_BONUS_MASK.ANY)


    class ARENA_PERIOD:
        IDLE = 0
        WAITING = 1
        PREBATTLE = 2
        BATTLE = 3
        AFTERBATTLE = 4


    class ARENA_UPDATE:
        VEHICLE_LIST = 1
        VEHICLE_ADDED = 2
        PERIOD = 3
        STATISTICS = 4
        VEHICLE_STATISTICS = 5
        VEHICLE_KILLED = 6
        AVATAR_READY = 7
        BASE_POINTS = 8
        BASE_CAPTURED = 9
        TEAM_KILLER = 10
        VEHICLE_UPDATED = 11
        COMBAT_EQUIPMENT_USED = 12
        RESPAWN_AVAILABLE_VEHICLES = 13
        RESPAWN_COOLDOWNS = 14
        RESPAWN_RANDOM_VEHICLE = 15
        FLAG_TEAMS = 16
        FLAG_STATE_CHANGED = 17
        RESPAWN_RESURRECTED = 18
        INTERACTIVE_STATS = 19
        DISAPPEAR_BEFORE_RESPAWN = 20
        RESOURCE_POINT_STATE_CHANGED = 21
        OWN_VEHICLE_INSIDE_RP = 22
        OWN_VEHICLE_LOCKED_FOR_RP = 23
        SYNC_OBJECTS = 24
        SYNC_OBJECTS_DIFF = 25
        VIEW_POINTS = 26
        FOG_OF_WAR = 27


    class ARENA_SYNC_OBJECTS:
        PLAYER_GROUP = 1
        RESPAWN = 2
        PLAYER_RANK = 3


    ARENA_SYNC_OBJECT_NAMES = dict([ (v, k) for k, v in ARENA_SYNC_OBJECTS.__dict__.iteritems() if not k.startswith('_') ])

    class JOIN_FAILURE:
        TIME_OUT = 1
        NOT_FOUND = 2
        ACCOUNT_LOCK = 3
        WRONG_VEHICLE = 4
        TEAM_IS_FULL = 5
        WRONG_ARGS = 6
        WRONG_ARENA_STATE = 8
        CANNOT_CREATE = 9
        PRIVACY = 10
        WRONG_ACCOUNT_TYPE = 11
        COOLDOWN = 12
        FORBIDDEN_IN_THIS_REGION = 13
        EVENT_DISABLED = 14
        WRONG_PERIPHERY_ID = 15


    JOIN_FAILURE_NAMES = dict([ (v, k) for k, v in JOIN_FAILURE.__dict__.iteritems() if not k.startswith('_') ])

    class KICK_REASON:
        ARENA_CREATION_FAILURE = 1
        AVATAR_CREATION_FAILURE = 2
        VEHICLE_CREATION_FAILURE = 3
        PREBATTLE_CREATION_FAILURE = 4
        BASEAPP_CRASH = 5
        CELLAPP_CRASH = 6
        UNKNOWN_FAILURE = 7
        FINISHED = 8
        CREATOR_LEFT = 9
        PLAYERKICK = 10
        TIMEOUT = 11


    KICK_REASON_NAMES = dict([ (v, k) for k, v in KICK_REASON.__dict__.iteritems() if not k.startswith('_') ])

    class FINISH_REASON:
        UNKNOWN = 0
        EXTERMINATION = 1
        BASE = 2
        TIMEOUT = 3
        FAILURE = 4
        TECHNICAL = 5
        WIN_POINTS_CAP = 6
        WIN_POINTS = 7


    class ARENA_EXT_MSG:
        UNKNOWN = 0
        ACCEPTED = 1
        CREATED = 2
        STARTED = 3
        FINISHED = 4
        FAILED = 5
        PLAYER_JOINED = 6
        PLAYER_LEFT = 7
        ALL_JOINED = STARTED


    class PREBATTLE_TYPE:
        NONE = 0
        SQUAD = 1
        TRAINING = 2
        COMPANY = 3
        TOURNAMENT = 4
        CLAN = 5
        UNIT = 6
        SORTIE = 7
        FORT_BATTLE = 8
        CLUBS = 9
        FALLOUT = 10
        EVENT = 11
        EXTERNAL = 12
        FORT_COMMON = 13
        E_SPORT_COMMON = 14
        RANGE = (SQUAD,
         TRAINING,
         COMPANY,
         TOURNAMENT,
         CLAN,
         UNIT,
         SORTIE,
         FORT_BATTLE,
         CLUBS,
         FALLOUT,
         EVENT,
         EXTERNAL,
         FORT_COMMON,
         E_SPORT_COMMON)
        LEGACY_PREBATTLES = (TRAINING,
         COMPANY,
         TOURNAMENT,
         CLAN)
        SQUAD_PREBATTLES = (SQUAD, FALLOUT, EVENT)
        UNIT_MGR_PREBATTLES = (UNIT,
         SORTIE,
         FORT_BATTLE,
         SQUAD,
         CLUBS,
         CLAN,
         FALLOUT,
         EVENT,
         EXTERNAL,
         FORT_COMMON,
         E_SPORT_COMMON)
        CREATE_FROM_CLIENT = (UNIT,
         SQUAD,
         FALLOUT,
         EVENT)
        CREATE_FROM_WEB = (UNIT, SQUAD, EXTERNAL)
        CREATE_EX_FROM_SERVER = (SQUAD,
         CLAN,
         CLUBS,
         SORTIE,
         FORT_BATTLE)
        CREATE_EX_FROM_WEB = (SQUAD,
         CLAN,
         CLUBS,
         SORTIE,
         FORT_BATTLE)


    PREBATTLE_TYPE_NAMES = dict([ (v, k) for k, v in PREBATTLE_TYPE.__dict__.iteritems() if not k.startswith('_') ])

    class ASSEMBLED_PREBATTLE_TYPE:
        NONE = 0
        ASSEMBLED = 1
        DYN_FALLOUT = 2


    class PREBATTLE_START_TYPE:
        DIRECT = 1
        SQUAD = 2
        COMPANY = 3
        RANGE = (DIRECT, SQUAD, COMPANY)


    class PREBATTLE_ROLE:
        TEAM_READY_1 = 1
        TEAM_READY_2 = 2
        ASSIGNMENT_1 = 4
        ASSIGNMENT_2 = 8
        ASSIGNMENT_1_2 = 16
        SEE_1 = 32
        SEE_2 = 64
        KICK_1 = 512
        KICK_2 = 1024
        CHANGE_ARENA = 2048
        CHANGE_COMMENT = 4096
        OPEN_CLOSE = 8192
        INVITE = 16384
        CHANGE_ARENA_VOIP = 32768
        CHANGE_DIVISION = 65536
        CHANGE_GAMEPLAYSMASK = 131072
        TRAINING_DEFAULT = SEE_1 | SEE_2
        TRAINING_CREATOR = TRAINING_DEFAULT | TEAM_READY_1 | TEAM_READY_2 | ASSIGNMENT_1 | ASSIGNMENT_2 | ASSIGNMENT_1_2 | KICK_1 | KICK_2 | CHANGE_ARENA | CHANGE_COMMENT | OPEN_CLOSE | INVITE | CHANGE_ARENA_VOIP
        SQUAD_DEFAULT = SEE_1
        SQUAD_CREATOR = SQUAD_DEFAULT | TEAM_READY_1 | KICK_1 | INVITE | CHANGE_GAMEPLAYSMASK
        COMPANY_DEFAULT = SEE_1
        COMPANY_CREATOR = COMPANY_DEFAULT | TEAM_READY_1 | ASSIGNMENT_1 | KICK_1 | CHANGE_COMMENT | OPEN_CLOSE | INVITE | CHANGE_DIVISION


    class PREBATTLE_STATE:
        IDLE = 0
        IN_QUEUE = 1
        IN_BATTLE = 2


    class PREBATTLE_TEAM_STATE:
        NOT_READY = 1
        READY = 2
        LOCKED = 3


    class PREBATTLE_ACCOUNT_STATE:
        UNKNOWN = 0
        NOT_READY = 1
        AFK = 2 | NOT_READY
        READY = 4
        IN_BATTLE = 8
        OFFLINE = 16
        MAIN_STATE_MASK = NOT_READY | AFK | READY | IN_BATTLE


    PREBATTLE_COMMENT_MAX_LENGTH = 400
    PREBATTLE_MAX_OBSERVERS_IN_TEAM = 5
    OBSERVERS_BONUS_TYPES = (ARENA_BONUS_TYPE.TRAINING,
     ARENA_BONUS_TYPE.TOURNAMENT,
     ARENA_BONUS_TYPE.TOURNAMENT_CLAN,
     ARENA_BONUS_TYPE.TOURNAMENT_REGULAR)

    class PREBATTLE_ERRORS:
        ROSTER_LIMIT = 'ROSTER_LIMIT'
        INVALID_VEHICLE = 'INVALID_VEHICLE'
        OBSERVERS_LIMIT = 'OBSERVERS_LIMIT'
        PLAYERS_LIMIT = 'PLAYERS_LIMIT'


    class PREBATTLE_UPDATE:
        ROSTER = 1
        PLAYER_ADDED = 2
        PLAYER_REMOVED = 3
        PLAYER_STATE = 4
        PLAYER_ROSTER = 5
        TEAM_STATES = 6
        SETTINGS = 7
        SETTING = 8
        KICKED_FROM_QUEUE = 9
        PROPERTIES = 10
        PROPERTY = 11


    class PREBATTLE_CACHE_KEY:
        TYPE = 1
        IS_OPENED = 2
        STATE = 3
        IS_FULL = 4
        PLAYER_COUNT = 5
        CREATOR = 6
        CREATE_TIME = 7
        START_TIME = 8
        COMMENT = 9
        DESCRIPTION = 10
        ARENA_TYPE_ID = 11
        ROUND_LENGTH = 12
        CREATOR_CLAN_DB_ID = 14
        CREATOR_CLAN_ABBREV = 15
        DIVISION = 16
        CREATOR_IGR_TYPE = 17
        CREATOR_DB_ID = 18


    class PREBATTLE_COMPANY_DIVISION:
        JUNIOR = 1
        MIDDLE = 2
        CHAMPION = 3
        ABSOLUTE = 4
        RANGE = (JUNIOR,
         MIDDLE,
         CHAMPION,
         ABSOLUTE)


    PREBATTLE_COMPANY_DIVISION_NAMES = dict([ (v, k) for k, v in PREBATTLE_COMPANY_DIVISION.__dict__.iteritems() if not k.startswith('_') and k != 'RANGE' ])

    class PREBATTLE_INVITE_STATE:
        ACTIVE = 1
        ACCEPTED = 2
        DECLINED = 3
        EXPIRED = 4


    UNIT_COMMENT_MAX_LENGTH = 400
    UNIT_MAX_SEND_INVITES = 100

    class UNIT_FINDER:
        RESULTSET_SIZE = 20


    class ACCOUNT_TYPE2:
        FIRST_FLAG = 1
        LAST_FLAG = 16384
        ACCOUNT_TYPE_DEFAULT = 16777216

        @staticmethod
        def getPrimaryGroup(type):
            return type >> 24 & 255

        @staticmethod
        def getSecondaryGroup(type):
            return type >> 16 & 255

        @staticmethod
        def getFlags(type):
            return type & 65535

        @staticmethod
        def getAttrs(cache, type):
            attrsDct = cache['primary'].get(ACCOUNT_TYPE2.getPrimaryGroup(type), None)
            raise attrsDct is not None or AssertionError
            attrsPrimaryGroup = attrsDct['attributes']
            attrsDct = cache['secondary'].get(ACCOUNT_TYPE2.getSecondaryGroup(type), None)
            attrsSecondaryGroup = attrsDct and attrsDct['attributes'] or 0
            return attrsPrimaryGroup | attrsSecondaryGroup

        @staticmethod
        def makeAccountType(primary, secondary, flags):
            return (primary & 255) << 24 | (secondary & 255) << 16 | flags & 65535


    class ACCOUNT_FLAGS:
        ALPHA = 1
        CBETA = 2
        OBETA = 4


    class ACCOUNT_ATTR:
        RANDOM_BATTLES = 1
        CLAN = 4
        MERCENARY = 8
        RATING = 16
        USER_INFO = 32
        STATISTICS = 64
        ARENA_CHANGE = 128
        CHAT_ADMIN = 256
        ADMIN = 512
        ROAMING = 1024
        DAILY_MULTIPLIED_XP = 2048
        PAYMENTS = 4096
        OUT_OF_SESSION_WALLET = 8192
        EXCLUDED_FROM_FAIRPLAY = 16384
        DAILY_BONUS_1 = 2097152
        DAILY_BONUS_2 = 4194304
        ALPHA = 536870912
        CBETA = 1073741824
        OBETA = 2147483648L
        PREMIUM = 4294967296L
        AOGAS = 8589934592L
        TUTORIAL_COMPLETED = 17179869184L
        IGR_BASE = 34359738368L
        IGR_PREMIUM = 68719476736L


    class RESTRICTION_TYPE:
        NONE = 0
        BAN = 1
        CHAT_BAN = 3
        CLAN = 5
        RANGE = (BAN, CHAT_BAN, CLAN)


    class RESTRICTION_SOURCE:
        UNKNOWN = 0
        SERVER = 1
        CLIENT = 2
        BACKYARD = 3
        MIGRATOR = 4


    SPA_RESTR_NAME_TO_RESTR_TYPE = {'game': RESTRICTION_TYPE.BAN,
     'chat': RESTRICTION_TYPE.CHAT_BAN,
     'clan': RESTRICTION_TYPE.CLAN}
    RESTR_TYPE_TO_SPA_NAME = dict(((x[1], x[0]) for x in SPA_RESTR_NAME_TO_RESTR_TYPE.iteritems()))

    class CLAN_MEMBER_FLAGS(object):
        LEADER = 1
        VICE_LEADER = 2
        RECRUITER = 4
        TREASURER = 8
        DIPLOMAT = 16
        COMMANDER = 32
        PRIVATE = 64
        RECRUIT = 128
        STAFF = 256
        JUNIOR = 512
        RESERVIST = 1024
        MAY_CHANGE_SETTINGS = LEADER | VICE_LEADER
        MAY_EDIT_RECRUIT_PROFILE = LEADER | VICE_LEADER | STAFF | RECRUITER
        MAY_CHANGE_ROLE = LEADER | VICE_LEADER | STAFF | COMMANDER
        MAY_CHANGE_COMMANDER = LEADER
        MAY_HANDLE_INVITES = LEADER | VICE_LEADER | STAFF | RECRUITER
        MAY_INVITE = LEADER | VICE_LEADER | STAFF | RECRUITER
        MAY_REMOVE_MEMBERS = LEADER | VICE_LEADER | STAFF
        MAY_REMOVE_CLAN = LEADER
        MAY_EXCHANGE_MONEY = LEADER | VICE_LEADER | STAFF | COMMANDER | DIPLOMAT | TREASURER | RECRUITER | JUNIOR | PRIVATE


    class AIMING_MODE:
        SHOOTING = 1
        TARGET_LOCK = 16
        USER_DISABLED = 256


    class VEHICLE_SETTING:
        CURRENT_SHELLS = 0
        NEXT_SHELLS = 1
        AUTOROTATION_ENABLED = 2
        SIEGE_MODE_ENABLED = 3
        ACTIVATE_EQUIPMENT = 16
        RELOAD_PARTIAL_CLIP = 17


    class VEHICLE_TTC_ASPECTS:
        DEFAULT = 0
        WHEN_MOVING = 1
        WHEN_STILL = 2
        WHEN_SIEGE = 3
        RANGE = (DEFAULT,
         WHEN_MOVING,
         WHEN_STILL,
         WHEN_SIEGE)


    class VEHICLE_MISC_STATUS:
        OTHER_VEHICLE_DAMAGED_DEVICES_VISIBLE = 0
        IS_OBSERVED_BY_ENEMY = 1
        LOADER_INTUITION_WAS_USED = 2
        VEHICLE_IS_OVERTURNED = 3
        VEHICLE_DROWN_WARNING = 4
        IN_DEATH_ZONE = 5
        HORN_BANNED = 6
        DESTROYED_DEVICE_IS_REPAIRING = 7
        SIEGE_MODE_STATE_CHANGED = 9


    class EQUIPMENT_STAGES:
        NOT_RUNNING = 0
        DEPLOYING = 1
        UNAVAILABLE = 2
        READY = 3
        PREPARING = 4
        ACTIVE = 5
        COOLDOWN = 6
        EXHAUSTED = 255

        @classmethod
        def toString(cls, value):
            return {0: 'notrunning',
             cls.DEPLOYING: 'deploying',
             cls.UNAVAILABLE: 'unavailable',
             cls.READY: 'ready',
             cls.PREPARING: 'preparing',
             cls.ACTIVE: 'active',
             cls.COOLDOWN: 'cooldown',
             cls.EXHAUSTED: 'exhausted'}.get(value)


    class DEVELOPMENT_INFO:
        ATTACK_RESULT = 1
        FIRE_RESULT = 2
        BONUSES = 3
        VISIBILITY = 4
        VEHICLE_ATTRS = 5
        NAVIGATION_RESULT = 6
        NAVIGATION_PATH = 7
        ENABLE_SENDING_VEH_ATTRS_TO_CLIENT = False


    class AMMOBAY_DESTRUCTION_MODE:
        POWDER_BURN_OFF = 0
        POWDER_EXPLOSION = 1
        HE_DETONATION = 2


    class SPECIAL_VEHICLE_HEALTH:
        DESTR_BY_FALL_RAMMING = -2
        FUEL_EXPLODED = -3
        AMMO_BAY_DESTROYED = -5
        TURRET_DETACHED = -13

        @staticmethod
        def IS_DESTR_BY_FALL_RAMMING(health):
            return health < 0 and health | SPECIAL_VEHICLE_HEALTH.DESTR_BY_FALL_RAMMING == SPECIAL_VEHICLE_HEALTH.DESTR_BY_FALL_RAMMING

        @staticmethod
        def IS_FUEL_EXPLODED(health):
            return health < 0 and health | SPECIAL_VEHICLE_HEALTH.FUEL_EXPLODED == SPECIAL_VEHICLE_HEALTH.FUEL_EXPLODED

        @staticmethod
        def IS_AMMO_BAY_DESTROYED(health):
            return health < 0 and health | SPECIAL_VEHICLE_HEALTH.AMMO_BAY_DESTROYED == SPECIAL_VEHICLE_HEALTH.AMMO_BAY_DESTROYED

        @staticmethod
        def IS_TURRET_DETACHED(health):
            return health < 0 and health | SPECIAL_VEHICLE_HEALTH.TURRET_DETACHED == SPECIAL_VEHICLE_HEALTH.TURRET_DETACHED


    class AOI:
        ENABLE_MANUAL_RULES = True
        VEHICLE_CIRCULAR_AOI_RADIUS = 565.0
        CIRCULAR_AOI_HYSTERESIS_MARGIN = 5.0


    class ATTACK_REASON(object):
        SHOT = 'shot'
        FIRE = 'fire'
        RAM = 'ramming'
        WORLD_COLLISION = 'world_collision'
        DEATH_ZONE = 'death_zone'
        DROWNING = 'drowning'
        GAS_ATTACK = 'gas_attack'
        OVERTURN = 'overturn'

        @classmethod
        def getIndex(cls, attackReason):
            return ATTACK_REASON_INDICES[attackReason]


    ATTACK_REASONS = (ATTACK_REASON.SHOT,
     ATTACK_REASON.FIRE,
     ATTACK_REASON.RAM,
     ATTACK_REASON.WORLD_COLLISION,
     ATTACK_REASON.DEATH_ZONE,
     ATTACK_REASON.DROWNING,
     ATTACK_REASON.GAS_ATTACK,
     ATTACK_REASON.OVERTURN)
    ATTACK_REASON_INDICES = dict(((value, index) for index, value in enumerate(ATTACK_REASONS)))
    DEATH_REASON_ALIVE = -1

    class VEHICLE_HIT_EFFECT:
        INTERMEDIATE_RICOCHET = 0
        FINAL_RICOCHET = 1
        ARMOR_NOT_PIERCED = 2
        ARMOR_PIERCED_NO_DAMAGE = 3
        ARMOR_PIERCED = 4
        CRITICAL_HIT = 5
        MAX_CODE = CRITICAL_HIT
        RICOCHETS = (INTERMEDIATE_RICOCHET, FINAL_RICOCHET)


    class VEHICLE_HIT_FLAGS:
        VEHICLE_KILLED = 1
        VEHICLE_WAS_DEAD_BEFORE_ATTACK = 2
        FIRE_STARTED = 4
        RICOCHET = 8
        MATERIAL_WITH_POSITIVE_DF_PIERCED_BY_PROJECTILE = 16
        MATERIAL_WITH_POSITIVE_DF_NOT_PIERCED_BY_PROJECTILE = 32
        ARMOR_WITH_ZERO_DF_PIERCED_BY_PROJECTILE = 64
        ARMOR_WITH_ZERO_DF_NOT_PIERCED_BY_PROJECTILE = 128
        DEVICE_PIERCED_BY_PROJECTILE = 256
        DEVICE_NOT_PIERCED_BY_PROJECTILE = 512
        DEVICE_DAMAGED_BY_PROJECTILE = 1024
        CHASSIS_DAMAGED_BY_PROJECTILE = 2048
        GUN_DAMAGED_BY_PROJECTILE = 4096
        MATERIAL_WITH_POSITIVE_DF_PIERCED_BY_EXPLOSION = 8192
        ARMOR_WITH_ZERO_DF_PIERCED_BY_EXPLOSION = 16384
        DEVICE_PIERCED_BY_EXPLOSION = 32768
        DEVICE_DAMAGED_BY_EXPLOSION = 65536
        CHASSIS_DAMAGED_BY_EXPLOSION = 131072
        GUN_DAMAGED_BY_EXPLOSION = 262144
        CHASSIS_DAMAGED_BY_RAMMING = 524288
        ATTACK_IS_DIRECT_PROJECTILE = 1048576
        ATTACK_IS_EXTERNAL_EXPLOSION = 2097152
        STUN_STARTED = 4194304
        IS_ANY_DAMAGE_MASK = MATERIAL_WITH_POSITIVE_DF_PIERCED_BY_PROJECTILE | MATERIAL_WITH_POSITIVE_DF_PIERCED_BY_EXPLOSION | DEVICE_PIERCED_BY_PROJECTILE | DEVICE_PIERCED_BY_EXPLOSION
        IS_ANY_PIERCING_MASK = IS_ANY_DAMAGE_MASK | ARMOR_WITH_ZERO_DF_PIERCED_BY_PROJECTILE | ARMOR_WITH_ZERO_DF_PIERCED_BY_EXPLOSION


    DAMAGE_INFO_CODES = ('DEVICE_CRITICAL', 'DEVICE_DESTROYED', 'TANKMAN_HIT', 'FIRE', 'DEVICE_CRITICAL_AT_SHOT', 'DEVICE_DESTROYED_AT_SHOT', 'DEVICE_CRITICAL_AT_RAMMING', 'DEVICE_DESTROYED_AT_RAMMING', 'DEVICE_STARTED_FIRE_AT_SHOT', 'DEVICE_STARTED_FIRE_AT_RAMMING', 'TANKMAN_HIT_AT_SHOT', 'DEATH_FROM_DEVICE_EXPLOSION_AT_SHOT', 'DEVICE_CRITICAL_AT_FIRE', 'DEVICE_DESTROYED_AT_FIRE', 'DEVICE_CRITICAL_AT_WORLD_COLLISION', 'DEVICE_DESTROYED_AT_WORLD_COLLISION', 'DEVICE_CRITICAL_AT_DROWNING', 'DEVICE_DESTROYED_AT_DROWNING', 'DEVICE_REPAIRED_TO_CRITICAL', 'DEVICE_REPAIRED', 'TANKMAN_HIT_AT_WORLD_COLLISION', 'TANKMAN_HIT_AT_DROWNING', 'TANKMAN_RESTORED', 'DEATH_FROM_DEVICE_EXPLOSION_AT_FIRE', 'ENGINE_CRITICAL_AT_UNLIMITED_RPM', 'ENGINE_DESTROYED_AT_UNLIMITED_RPM', 'DEATH_FROM_SHOT', 'DEATH_FROM_INACTIVE_CREW_AT_SHOT', 'DEATH_FROM_RAMMING', 'DEATH_FROM_FIRE', 'DEATH_FROM_INACTIVE_CREW', 'DEATH_FROM_DROWNING', 'DEATH_FROM_WORLD_COLLISION', 'DEATH_FROM_INACTIVE_CREW_AT_WORLD_COLLISION', 'DEATH_FROM_DEATH_ZONE', 'DEATH_FROM_GAS_ATTACK', 'DEATH_FROM_OVERTURN', 'FIRE_STOPPED')

    class IGR_TYPE:
        NONE = 0
        BASE = 1
        PREMIUM = 2
        RANGE = (BASE, PREMIUM)


    class EVENT_TYPE:
        ACTION = 1
        BATTLE_QUEST = 2
        TOKEN_QUEST = 3
        FORT_QUEST = 5
        PERSONAL_QUEST = 6
        REF_SYSTEM_QUEST = 7
        POTAPOV_QUEST = 8
        GROUP = 9
        CLUBS_QUEST = 10
        TUTORIAL = 11
        MOTIVE_QUEST = 12
        NAME_TO_TYPE = {'battleQuest': BATTLE_QUEST,
         'tokenQuest': TOKEN_QUEST,
         'fortQuest': FORT_QUEST,
         'personalQuest': PERSONAL_QUEST,
         'refSystemQuest': REF_SYSTEM_QUEST,
         'potapovQuest': POTAPOV_QUEST,
         'clubsQuest': CLUBS_QUEST,
         'group': GROUP,
         'tutorial': TUTORIAL,
         'motiveQuest': MOTIVE_QUEST}
        TYPE_TO_NAME = dict(zip(NAME_TO_TYPE.values(), NAME_TO_TYPE.keys()))
        QUEST_RANGE = (BATTLE_QUEST,
         TOKEN_QUEST,
         FORT_QUEST,
         PERSONAL_QUEST,
         REF_SYSTEM_QUEST,
         POTAPOV_QUEST,
         CLUBS_QUEST,
         GROUP,
         MOTIVE_QUEST)
        LIKE_BATTLE_QUESTS = (BATTLE_QUEST,
         FORT_QUEST,
         PERSONAL_QUEST,
         POTAPOV_QUEST,
         CLUBS_QUEST,
         MOTIVE_QUEST)
        LIKE_TOKEN_QUESTS = (TOKEN_QUEST, REF_SYSTEM_QUEST)
        ONE_BONUS_QUEST = (TOKEN_QUEST, REF_SYSTEM_QUEST, POTAPOV_QUEST)
        QUEST_WITH_DYNAMIC_CLIENT_DATA = (FORT_QUEST, PERSONAL_QUEST)
        SHARED_QUESTS = (POTAPOV_QUEST, CLUBS_QUEST, MOTIVE_QUEST)


    DAMAGE_INFO_INDICES = dict(((x[1], x[0]) for x in enumerate(DAMAGE_INFO_CODES)))
    CLIENT_INACTIVITY_TIMEOUT = 40

    class CHAT_LOG:
        NONE = 0
        MESSAGES = 1
        ACTIONS = 2


    CHAT_MESSAGE_MAX_LENGTH = 1024
    CHAT_MESSAGE_MAX_LENGTH_IN_BATTLE = 140

    class PROMO_CUTOUT:
        OFF = 0
        ON = 1


    VEHICLE_CLASSES = ('lightTank', 'mediumTank', 'heavyTank', 'SPG', 'AT-SPG')
    VEHICLE_CLASS_INDICES = dict(((x[1], x[0]) for x in enumerate(VEHICLE_CLASSES)))
    MIN_VEHICLE_LEVEL = 1
    MAX_VEHICLE_LEVEL = 10

    class TEAMS_IN_ARENA:
        MAX_TEAMS = 40
        MIN_TEAMS = 2
        ANY_TEAM = 0


    class QUEUE_TYPE:
        UNKNOWN = 0
        RANDOMS = 1
        COMPANIES = 2
        VOLUNTEERS = 3
        SANDBOX = 4
        UNITS = 5
        EVENT_BATTLES = 7
        UNIT_ASSEMBLER = 8
        TUTORIAL = 9
        SORTIE = 10
        FORT_BATTLE = 11
        CLUBS = 12
        SPEC_BATTLE = 13
        FALLOUT_CLASSIC = 14
        FALLOUT_MULTITEAM = 15
        EXTERNAL_UNITS = 16
        FALLOUT = (FALLOUT_CLASSIC, FALLOUT_MULTITEAM)
        ALL = (RANDOMS,
         COMPANIES,
         VOLUNTEERS,
         SANDBOX,
         UNITS,
         EVENT_BATTLES,
         UNIT_ASSEMBLER,
         TUTORIAL,
         SORTIE,
         CLUBS,
         FORT_BATTLE,
         SPEC_BATTLE,
         FALLOUT,
         FALLOUT_CLASSIC,
         FALLOUT_MULTITEAM,
         EXTERNAL_UNITS)


    class UNIT_ASSEMBLER_FLAG:
        IGNORE_RATING = 1
        ONLY_NEW_TEAM = 2
        KICK_AFTER_BATTLE = 4
        ASSEMBLE_NEW_UNITS = 8
        ALL = (IGNORE_RATING,
         ONLY_NEW_TEAM,
         KICK_AFTER_BATTLE,
         ASSEMBLE_NEW_UNITS)

        @staticmethod
        def isFlagSet(flag):
            flags = BigWorld.baseAppData.get('unitAssemblerFlags', 0)
            return bool(flags & flag)


    QUEUE_TYPE_NAMES = dict([ (v, k) for k, v in QUEUE_TYPE.__dict__.iteritems() if not k.startswith('_') ])
    USER_ACTIVE_CHANNELS_LIMIT = 100

    class INVOICE_EMITTER:
        PAYMENT_SYSTEM = 1
        BACKYARD = 2
        COMMUNITY = 3
        PORTAL = 4
        DEVELOPMENT = 5
        CN_GIFT = 6
        CN_BUY = 7
        ACTION_APPLIER = 9
        WG = 10
        WGCW = 11
        PSS = 12
        NEGATIVE = (BACKYARD,
         COMMUNITY,
         PORTAL,
         DEVELOPMENT,
         CN_GIFT,
         CN_BUY,
         WG,
         WGCW,
         PSS)
        RANGE = (PAYMENT_SYSTEM,
         BACKYARD,
         COMMUNITY,
         PORTAL,
         DEVELOPMENT,
         CN_GIFT,
         CN_BUY,
         ACTION_APPLIER,
         WG,
         WGCW,
         PSS)


    class INVOICE_ASSET:
        GOLD = 1
        CREDITS = 2
        PREMIUM = 3
        DATA = 4
        FREE_XP = 5
        FORT_RESOURCE = 6


    CHANNEL_SEARCH_RESULTS_LIMIT = 50
    USER_SEARCH_RESULTS_LIMIT = 50

    class USER_SEARCH_MODE:
        ALL = 0
        ONLINE = 1
        OFFLINE = 2


    class AOGAS_TIME:
        REDUCED_GAIN = 10200
        NO_GAIN = 17400
        RESET = 18000


    USE_SERVER_BAD_WORDS_FILTER = IS_CHINA

    class SERVER_BAD_WORDS_FILTER_MODE:
        ACCOUNT = 1
        CHANNEL = 2


    CURRENT_SERVER_BAD_WORDS_FILTER_MODE = SERVER_BAD_WORDS_FILTER_MODE.CHANNEL

    class CREDENTIALS_RESTRICTION:
        BASIC = 0
        CHINESE = 1
        KOREA = 3


    CREDENTIALS_RESTRICTION_SET = IS_CHINA and CREDENTIALS_RESTRICTION.CHINESE
elif IS_KOREA:
    CREDENTIALS_RESTRICTION_SET = CREDENTIALS_RESTRICTION.KOREA
else:
    CREDENTIALS_RESTRICTION_SET = CREDENTIALS_RESTRICTION.BASIC

class AUTO_MAINTENANCE_TYPE:
    REPAIR = 1
    LOAD_AMMO = 2
    EQUIP = 3


class AUTO_MAINTENANCE_RESULT:
    OK = 0
    NOT_ENOUGH_ASSETS = 1
    NOT_PERFORMED = 2
    DISABLED_OPTION = 3
    NO_WALLET_SESSION = 4


class REQUEST_COOLDOWN:
    PLAYER_DOSSIER = 1.0
    PLAYER_CLAN_INFO = 1.0
    PLAYER_GLOBAL_RATING = 1.0
    PLAYERS_GLOBAL_RATING = 1.0
    PREBATTLE_CREATION = 4.0
    PREBATTLE_NOT_READY = 2.0
    PREBATTLE_TEAM_NOT_READY = 1.0
    PREBATTLE_JOIN = 1.0
    PREBATTLE_INVITES = 8.0
    REQUEST_CHAT_TOKEN = 10.0
    REQUEST_WEB_TOKEN = 4.0
    REQUEST_TOKEN = 10.0
    UNIT_CHANGE_FLAGS = 4.0
    UNIT_SET_READY = 2.0
    UNIT_BROWSER_REFRESH = 4.0
    CALL_FORT_METHOD = 0.5
    SUBSCRIBE = 0.5
    GET_ENEMY_CLAN_CARD = 0.5
    GET_FORT_SORTIE_DATA = 1.0
    ADD_DEL_BUILDING = 3.0
    FORT_KEEPALIVE = 60.0
    CLIENT_LOG_UX_DATA_COOLDOWN = 2.0
    REQUEST_FORT_PUBLIC_INFO = 10.0
    CLIENT_LOG_XMPP_DATA_COOLDOWN = 10.0
    CLUBS_ANY_CMD_COOLDOWN = 1.0
    CLUBS_LONG_COOLDOWN = 5.0
    CALL_GM_METHOD = 0.5
    GM_KEEP_ALIVE = 60.0
    SEND_INVITATION_COOLDOWN = 1.0


IS_SHOW_INGAME_HELP_FIRST_TIME = False

class DENUNCIATION:
    NOT_FAIR_PLAY = 1
    FORBIDDEN_NICK = 2
    BOT = 3
    INCORRECT_BEHAVIOR = 7


DENUNCIATIONS_PER_DAY = 10

class VIOLATOR_KIND:
    UNKNOWN = 0
    ENEMY = 1
    ALLY = 2


GROUND_TYPE_BY_NAME = {'none': 0,
 'firm': 1,
 'medium': 2,
 'soft': 3,
 'slope': 4,
 'death_zone': 5}
GROUND_TYPE_NAME_BY_INDEX = dict(((v, k) for k, v in GROUND_TYPE_BY_NAME.iteritems()))

class DROWN_WARNING_LEVEL:
    SAFE = 0
    CAUTION = 1
    DANGER = 2


class OVERTURN_WARNING_LEVEL:
    SAFE = 0
    CAUTION = 1
    DANGER = 2

    @classmethod
    def isOverturned(cls, warningLevel):
        return warningLevel in (cls.CAUTION, cls.DANGER)


class OVERTURN_CONDITION:
    IGNOR_DELAY = 0.1
    WARNING_COSINE = math.cos(math.radians(70))
    ONBOARD_COSINE = math.cos(math.radians(80))
    OVERTURN_COSINE = math.cos(math.radians(120))
    HULL_PRESSURE = 0.2


TREE_TAG = 'tree'
CUSTOM_DESTRUCTIBLE_TAGS = ('monument',)
DESTR_CODES_BY_TAGS = dict(((tag, code) for code, tag in enumerate(CUSTOM_DESTRUCTIBLE_TAGS)))
DESTR_CODES_BY_TAGS[TREE_TAG] = len(CUSTOM_DESTRUCTIBLE_TAGS)
DESTR_TAGS_BY_CODES = dict(((code, tag) for tag, code in DESTR_CODES_BY_TAGS.iteritems()))

class SYS_MESSAGE_CLAN_EVENT:
    LEFT_CLAN = 1


SYS_MESSAGE_CLAN_EVENT_NAMES = dict([ (v, k) for k, v in SYS_MESSAGE_CLAN_EVENT.__dict__.iteritems() if not k.startswith('_') ])

class SYS_MESSAGE_FORT_EVENT:
    FORT_READY = 1
    RESERVE_ACTIVATED = 2
    RESERVE_EXPIRED = 3
    RESERVE_PRODUCED = 4
    STORAGE_OVERFLOW = 5
    ORDER_CANCELED = 6
    REATTACHED_TO_BASE = 7
    DEF_HOUR_ACTIVATED = 8
    OFF_DAY_ACTIVATED = 9
    VACATION_STARTED = 10
    VACATION_FINISHED = 11
    DEF_HOUR_SHUTDOWN = 12
    DEF_HOUR_CHANGED = 13
    PERIPHERY_CHANGED = 14
    BUILDING_DAMAGED = 15
    BASE_DESTROYED = 16
    SPECIAL_ORDER_EXPIRED = 17
    ORDER_COMPENSATED = 18
    ATTACK_PLANNED = 19
    DEFENCE_PLANNED = 20
    BATTLE_DELETED = 21
    RESOURCE_SET = 22
    RESERVE_SET = 23
    FORT_GOT_8_LEVEL = 24
    BATTLE_DELETED_LEVEL = 25


SYS_MESSAGE_FORT_EVENT_NAMES = dict([ (v, k) for k, v in SYS_MESSAGE_FORT_EVENT.__dict__.iteritems() if not k.startswith('_') ])
MAX_FORTIFICATION_LEVEL = 10
FORT_MAX_LEVEL_RANGE = 1
FORT_MIN_ATTACK_LEVEL = 5
FORT_MAX_ATTACK_LEVEL = MAX_FORTIFICATION_LEVEL

class FORT_BUILDING_TYPE:
    MILITARY_BASE = 1
    FINANCIAL_DEPT = 2
    TANKODROME = 3
    TRAINING_DEPT = 4
    MILITARY_ACADEMY = 5
    TRANSPORT_DEPT = 6
    INTENDANT_SERVICE = 7
    TROPHY_BRIGADE = 8
    OFFICE = 9
    MILITARY_SHOP = 10
    ARTILLERY_SHOP = 11
    BOMBER_SHOP = 12
    _ALL = (MILITARY_BASE,
     FINANCIAL_DEPT,
     TANKODROME,
     TRAINING_DEPT,
     MILITARY_ACADEMY,
     TRANSPORT_DEPT,
     INTENDANT_SERVICE,
     TROPHY_BRIGADE,
     OFFICE,
     MILITARY_SHOP,
     ARTILLERY_SHOP,
     BOMBER_SHOP)


FORT_BUILDING_TYPE_NAMES = dict([ (v, k) for k, v in FORT_BUILDING_TYPE.__dict__.iteritems() if not k.startswith('_') ])

class FORT_ORDER_TYPE:
    COMBAT_PAYMENTS = 1
    TACTICAL_TRAINING = 2
    ADDITIONAL_BRIEFING = 3
    MILITARY_EXERCISES = 4
    HEAVY_TRANSPORT = 5
    EVACUATION = 6
    REQUISITION = 7
    SPECIAL_MISSION = 8
    EVACUATION_EXPIRE = 9
    REQUISITION_EXPIRE = 10
    ARTILLERY = 11
    BOMBER = 12
    COMBAT_PAYMENTS_2_0 = 13
    MILITARY_EXERCISES_2_0 = 14
    TACTICAL_TRAINING_2_0 = 15
    ADDITIONAL_BRIEFING_2_0 = 16
    HEAVY_TRANSPORT_2_0 = 17
    REQUISITION_2_0 = 18
    ALL = (COMBAT_PAYMENTS,
     TACTICAL_TRAINING,
     ADDITIONAL_BRIEFING,
     MILITARY_EXERCISES,
     HEAVY_TRANSPORT,
     EVACUATION,
     REQUISITION,
     SPECIAL_MISSION,
     EVACUATION_EXPIRE,
     REQUISITION_EXPIRE,
     ARTILLERY,
     BOMBER,
     COMBAT_PAYMENTS_2_0,
     MILITARY_EXERCISES_2_0,
     TACTICAL_TRAINING_2_0,
     ADDITIONAL_BRIEFING_2_0,
     HEAVY_TRANSPORT_2_0,
     REQUISITION_2_0)
    ACTIVATED = (COMBAT_PAYMENTS,
     TACTICAL_TRAINING,
     ADDITIONAL_BRIEFING,
     MILITARY_EXERCISES,
     HEAVY_TRANSPORT,
     EVACUATION,
     REQUISITION,
     SPECIAL_MISSION,
     COMBAT_PAYMENTS_2_0,
     MILITARY_EXERCISES_2_0,
     TACTICAL_TRAINING_2_0,
     ADDITIONAL_BRIEFING_2_0,
     HEAVY_TRANSPORT_2_0,
     REQUISITION_2_0)
    CONSUMABLES = (BOMBER, ARTILLERY)
    _EXPIRATION_TO_SOURCE = {EVACUATION_EXPIRE: EVACUATION,
     REQUISITION_EXPIRE: REQUISITION}
    COMPATIBLES = (EVACUATION, REQUISITION, SPECIAL_MISSION)

    @staticmethod
    def isOrderPermanent(orderID):
        return orderID in (FORT_ORDER_TYPE.EVACUATION, FORT_ORDER_TYPE.REQUISITION)

    @staticmethod
    def isOrderCompatible(orderID):
        return orderID in FORT_ORDER_TYPE.COMPATIBLES


FORT_ORDER_TYPE_NAMES = dict([ (v, k) for k, v in FORT_ORDER_TYPE.__dict__.iteritems() if v in FORT_ORDER_TYPE.ALL ])

class USER_SERVER_SETTINGS:
    VERSION = 0
    HIDE_MARKS_ON_GUN = 500
    GAME_EXTENDED = 59
    _ALL = (HIDE_MARKS_ON_GUN,)

    @classmethod
    def isBattleInvitesForbidden(cls, settings):
        if settings and cls.GAME_EXTENDED in settings:
            return not settings[cls.GAME_EXTENDED] >> 2 & 1
        return False


INT_USER_SETTINGS_KEYS = {USER_SERVER_SETTINGS.VERSION: 'Settings version',
 1: 'Game section settings',
 2: 'Graphics section settings',
 3: 'Sound section settings',
 4: 'Controls section settings',
 5: 'Keyboard section settings',
 6: 'Keyboard section settings',
 7: 'Keyboard section settings',
 8: 'Keyboard section settings',
 9: 'Keyboard section settings',
 10: 'Keyboard section settings',
 11: 'Keyboard section settings',
 12: 'Keyboard section settings',
 13: 'Keyboard section settings',
 14: 'Keyboard section settings',
 15: 'Keyboard section settings',
 16: 'Keyboard section settings',
 17: 'Keyboard section settings',
 18: 'Keyboard section settings',
 19: 'Keyboard section settings',
 20: 'Keyboard section settings',
 21: 'Keyboard section settings',
 22: 'Keyboard section settings',
 23: 'Keyboard section settings',
 24: 'Keyboard section settings',
 25: 'Keyboard section settings',
 26: 'Keyboard section settings',
 27: 'Keyboard section settings',
 28: 'Keyboard section settings',
 29: 'Keyboard section settings',
 30: 'Keyboard section settings',
 31: 'Keyboard section settings',
 32: 'Keyboard section settings',
 33: 'Keyboard section settings',
 34: 'Keyboard section settings',
 35: 'Keyboard section settings',
 36: 'Keyboard section settings',
 37: 'Keyboard section settings',
 38: 'Keyboard section settings',
 39: 'Keyboard section settings',
 40: 'Keyboard section settings',
 41: 'Keyboard section settings',
 42: 'Keyboard section settings',
 43: 'Arcade aim setting',
 44: 'Arcade aim setting',
 45: 'Arcade aim setting',
 46: 'Sniper aim setting',
 47: 'Sniper aim setting',
 48: 'Sniper aim setting',
 49: 'Enemy marker setting',
 50: 'Dead marker setting',
 51: 'Ally marker setting',
 52: 'GuiStartBehavior',
 53: 'Feedback section settings',
 54: 'EULAVersion',
 55: 'Gameplay settings',
 56: '[Free]',
 57: 'Users storage revision',
 58: 'Contacts',
 USER_SERVER_SETTINGS.GAME_EXTENDED: 'Game extended section settings',
 60: 'Fallout',
 61: 'Tutorial',
 62: '[Free]',
 63: 'Arcade aim setting',
 64: 'Sniper aim setting',
 65: '[Free]',
 66: '[Free]',
 67: '[Free]',
 68: '[Free]',
 69: '[Free]',
 70: 'Once only hints',
 71: 'Keyboard section settings',
 73: 'Carousel filter',
 74: 'Carousel filter',
 75: 'Fallout carousel filter',
 76: 'Fallout carousel filter',
 77: 'PRMP encyclopedia recommendations 1-2',
 78: 'PRMP encyclopedia recommendations 3-4',
 79: 'PRMP encyclopedia recommendations 5-6',
 USER_SERVER_SETTINGS.HIDE_MARKS_ON_GUN: 'Hide marks on gun'}

class WG_GAMES:
    TANKS = 'wot'
    WARPLANES = 'wowp'
    WARSHIPS = 'wows'
    GENERALS = 'wotg'
    BLITZ = 'wotb'
    WEB = 'web'
    MOB = 'mob'
    ALL = (TANKS,
     WARPLANES,
     WARSHIPS,
     GENERALS,
     BLITZ,
     WEB,
     MOB)


class TOKEN_TYPE:
    XMPPCS = 1
    WGNI = 2
    WOTG = 3
    WOTB = 4
    SERVICE_NAMES = {XMPPCS: 'xmppcs',
     WGNI: 'wgni',
     WOTG: 'wotg',
     WOTB: 'wotb'}
    COOLDOWNS = {XMPPCS: 'REQUEST_CHAT_TOKEN',
     WGNI: 'REQUEST_WEB_TOKEN',
     WOTG: 'REQUEST_TOKEN',
     WOTB: 'REQUEST_TOKEN'}


class NC_MESSAGE_TYPE:
    INFO = 1
    GOLD = 2
    PREMIUM = 3
    BACKYARD = 4
    POLL = 5
    REFERRAL = 6
    DEFAULT = INFO
    RANGE = (INFO,
     GOLD,
     PREMIUM,
     BACKYARD,
     POLL,
     REFERRAL)


class NC_MESSAGE_PRIORITY:
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    DEFAULT = MEDIUM
    ORDER = (LOW, MEDIUM, HIGH)


class NC_CONTEXT_ITEM_TYPE:
    GOLD = 1
    INTEGRAL = 2
    FRACTIONAL = 3
    NICE_NUMBER = 4
    SHORT_TIME = 5
    LONG_TIME = 6
    SHORT_DATE = 7
    LONG_DATE = 8
    DATETIME = 9
    STRING = 10


class WIN_XP_FACTOR_MODE:
    DAILY = 0
    ALWAYS = 1


OBSERVER_VEH_INVENTORY_ID = -5000

class FORT_SCOUTING_DATA_FILTER:
    DEFAULT = 1
    RECENT = 2
    ELECT = 3
    FILTER = 4
    RANGE = (DEFAULT,
     RECENT,
     ELECT,
     FILTER)


class FORT_SCOUTING_DATA_ERROR:
    DONE = 0
    COOLDOWN = 1
    INVALID_NAME = 2
    DB_ERORR = 3
    NOT_IN_CLAN = 4
    INVALID_PARAMS = 5
    DISCONNECTED_FROM_CENTER = 6


FORT_FAVORITES_LIMIT = 100

class PREBATTLE_INVITE_STATUS:
    OK = 0
    WRONG_CLAN = 1
    LEGIONARIES_NOT_ALLOWED = 2


PREBATTLE_INVITE_STATUS_NAMES = dict([ (v, k) for k, v in PREBATTLE_INVITE_STATUS.__dict__.iteritems() if not k.startswith('_') ])
FAIRPLAY_VIOLATIONS_NAMES = ('deserter', 'suicide', 'afk')
FAIRPLAY_VIOLATIONS_MASKS = dict([ (name, 1 << index) for index, name in enumerate(FAIRPLAY_VIOLATIONS_NAMES) ])

class FORT_BATTLE_RESULT:
    WIN = 1
    DRAW = 0
    LOSS = -1


class FORT_COMBAT_RESULT:
    WIN = 1
    DRAW = 0
    LOSS = -1
    TECH_WIN = 10
    TECH_DRAW = -20
    TECH_LOSS = -10

    @staticmethod
    def invert(value):
        if value in (FORT_COMBAT_RESULT.WIN,
         FORT_COMBAT_RESULT.LOSS,
         FORT_COMBAT_RESULT.TECH_WIN,
         FORT_COMBAT_RESULT.TECH_LOSS):
            return -value
        else:
            return value

    @staticmethod
    def invertCombatList(_list):
        return map(lambda combat: (FORT_COMBAT_RESULT.invert(combat[0]),) + combat[1:], _list)


class FORT_BUILDING_STATUS:
    READY_FOR_BATTLE = 0
    LOW_LEVEL = 1
    DESTROYED = 2


FORT_SCHEDULER_ROWS_PER_QUERY = 200
FORT_SCHEDULER_DB_PAGE_SIZE = CURRENT_REALM != 'CT' and 5000 or 5000000
FORT_QUEST_SUFFIX = 'stronghold'

class REF_SYSTEM_FLAG:
    REFERRAL_NEW_PLAYER = 1
    REFERRAL_PHOENIX = 2
    CONFIRMED_INVITE = 4
    CONFIRMED_FIRST_BATTLE = 8
    REFERRAL_BOUGHT_10_LVL_VEH = 16
    PREFIX_TO_TYPE = {'invited_by': REFERRAL_NEW_PLAYER,
     'winback_by': REFERRAL_PHOENIX}


class INVALID_CLIENT_STATS:
    OK = 0
    CLIENT_DEATH = 1
    CLIENT_FOCUS_LOST = 2
    CLIENT_STRAIGHT_INTO_BATTLE = 4
    CLIENT_GS_MAJOR_CHANGED = 8
    CLIENT_GS_MINOR_CHANGED = 16
    CLIENT_RESOLUTION_CHANGED = 32
    CLIENT_WM_CHANGED = 64
    CLIENT_DRR_SCALE_CHANGED = 128


class EQUIP_TMAN_CODE:
    OK = 0
    NO_VEHICLE = 1
    VEHICLE_LOCKED = 2
    NO_FREE_SLOT = 3


class EVENT_CLIENT_DATA:
    ACTION = 1
    ACTION_REV = 2
    QUEST = 3
    QUEST_REV = 4
    INGAME_EVENTS = 7
    INGAME_EVENTS_REV = 8
    NOTIFICATIONS = 9
    NOTIFICATIONS_REV = 10
    PERSONAL_QUEST = 11
    PERSONAL_QUEST_REV = 12
    FORT_QUEST = 13
    FORT_QUEST_REV = 14
    FALLOUT = 15
    FALLOUT_REV = 16
    SQUAD_BONUSES = 17
    SQUAD_BONUSES_REV = 18
    FEATURES_SWITCH = 19
    FEATURES_SWITCH_REV = 20

    @staticmethod
    def REVISION(id):
        raise id % 2 == 1 or AssertionError
        return id + 1


class FLAG_TYPES:
    BIG = 0
    MEDIUM = 1
    SMALL = 2
    RANGE = (BIG, MEDIUM, SMALL)


class FLAG_SPAWN_COOLDOWN:
    ABSORB = 10.0
    SOLO_ABSORB = 10.0
    DROP = 15.0


class FLAG_STATE:
    UNKNOWN = 0
    ON_SPAWN = 1
    ON_GROUND = 2
    ON_VEHICLE = 3
    ABSORBED = 4
    WAITING_FIRST_SPAWN = 5


class FLAG_ACTION:
    PICKED_UP_FROM_BASE = 0
    PICKED_UP_FROM_GROUND = 1
    CAPTURED = 2
    LOST = 3
    RANGE = (PICKED_UP_FROM_BASE,
     PICKED_UP_FROM_GROUND,
     CAPTURED,
     LOST)


FLAG_VOLUME_RADIUS = 10.0

class INVITATION_STATUS:
    ERROR = -1
    PENDING = 0
    ACCEPTED = 1
    DECLINED = 2
    REVOKED = 3


class INVITATION_TYPE:
    SQUAD = PREBATTLE_TYPE.SQUAD
    FALLOUT = PREBATTLE_TYPE.FALLOUT
    RANGE = (SQUAD, FALLOUT)


class REPAIR_FLAGS:
    STOP_FIRE = 1
    HEAL_VEHICLE = 2
    HEAL_CREW = 4
    HEAL_DEVICES = 8
    REPLENISH_AMMO = 16
    REPLENISH_EQUIP = 32
    RELOAD_GUN = 64
    ALL = STOP_FIRE | HEAL_VEHICLE | HEAL_CREW | HEAL_DEVICES | REPLENISH_AMMO | REPLENISH_EQUIP | RELOAD_GUN
    ALL_WITHOUT_RELOAD = STOP_FIRE | HEAL_VEHICLE | HEAL_CREW | HEAL_DEVICES | REPLENISH_AMMO | REPLENISH_EQUIP


class REPAIR_POINT_STATE:
    READY = 0
    REPAIRING = 1
    COOLDOWN_VEH_INSIDE = 2
    COOLDOWN_VEH_OUTSIDE = 3
    DISABLED = 4


class REPAIR_POINT_ACTION:
    START_REPAIR = 0
    RESTART_REPAIR = 1
    CANCEL_REPAIR = 2
    COMPLETE_REPAIR = 3
    ENTER_WHILE_CD = 4
    LEAVE_WHILE_CD = 5
    BECOME_READY = 6
    BECOME_DISABLED = 7


class GLOBAL_MAP_DIVISION(object):
    MIDDLE = 0
    CHAMPION = 1
    ABSOLUTE = 2
    _ORDER = (MIDDLE, CHAMPION, ABSOLUTE)


GLOBAL_MAP_DIVISION_NAMES = dict([ (v, k) for k, v in GLOBAL_MAP_DIVISION.__dict__.iteritems() if not k.startswith('_') ])

class RESOURCE_POINT_STATE:
    UNKNOWN = 0
    FREE = 1
    COOLDOWN = 2
    CAPTURED = 3
    CAPTURED_LOCKED = 4
    BLOCKED = 5


class VEHICLE_PHYSICS_MODE:
    STANDARD = 0
    DETAILED = 1


class VEHICLE_MODE:
    DEFAULT = 0
    SIEGE = 1


class VEHICLE_SIEGE_STATE:
    DISABLED = 0
    SWITCHING_ON = 1
    ENABLED = 2
    SWITCHING_OFF = 3
    SWITCHING = (SWITCHING_ON, SWITCHING_OFF)


class CONTENT_TYPE:
    DEFAULT = 0
    SD_TEXTURES = 1
    HD_TEXTURES = 2
    INCOMPLETE = 3
    TUTORIAL = 4
    SANDBOX = 5


class DEATH_ZONES:
    STATIC = 0
    GAS_ATTACK = 1


KNOWN_QUALIFIER_CONDITION_PARAMS = {'aliveSquadMembersCount',
 'aliveAlliesCount',
 'enemiesCountNearby',
 'lightTankEnemiesCountNearby',
 'heavyTankEnemiesCountNearby',
 'mediumTankEnemiesCountNearby',
 'AT_SPGEnemiesCountNearby',
 'now',
 'playerTankHealthPercent',
 'enemyTankDetectionTime',
 'mapKind',
 'playerTankUnproductiveHitTime',
 'enemyTankDestructionTime',
 'enemyTankCriticalHitTime'}

class FALLOUT_ARENA_TYPE:
    GAMEPLAY_NAMES = {'multiteam': ('fallout', 'fallout2', 'fallout3'),
     'classic': ('fallout4', 'fallout5', 'fallout6')}

    @staticmethod
    def fromGameplayName(gameplayName):
        for type, names in FALLOUT_ARENA_TYPE.GAMEPLAY_NAMES.iteritems():
            if gameplayName in names:
                return type

        return None


class RESPAWN_TYPES:
    NONE = 0
    INFINITE = 1
    SHARED = 2
    LIMITED = 3


class VISIBILITY:
    MAX_RADIUS = 445.0
    MIN_RADIUS = 50.0


VEHICLE_ATTRS_TO_SYNC = frozenset(['circularVisionRadius'])

class OBSTACLE_KIND:
    CHUNK_DESTRUCTIBLE = 1
    ENTITY_DESTRUCTIBLE = 2


class SHELL_TYPES(object):
    HOLLOW_CHARGE = 'HOLLOW_CHARGE'
    HIGH_EXPLOSIVE = 'HIGH_EXPLOSIVE'
    ARMOR_PIERCING = 'ARMOR_PIERCING'
    ARMOR_PIERCING_HE = 'ARMOR_PIERCING_HE'
    ARMOR_PIERCING_CR = 'ARMOR_PIERCING_CR'


SHELL_TYPES_LIST = (SHELL_TYPES.HOLLOW_CHARGE,
 SHELL_TYPES.HIGH_EXPLOSIVE,
 SHELL_TYPES.ARMOR_PIERCING,
 SHELL_TYPES.ARMOR_PIERCING_HE,
 SHELL_TYPES.ARMOR_PIERCING_CR)
SHELL_TYPES_INDICES = dict(((value, index) for index, value in enumerate(SHELL_TYPES_LIST)))

class HIT_INDIRECTION:
    DIRECT_HIT = 0
    HIT_BY_EXTERNAL_EXPLOSION = 1
    HIT_BY_RICOCHET = 2
    MISS = 3
    CEILING_HIT = 4


class SWITCH_STATE(object):
    ALL = 'all'
    TOKEN = 'token'
    NONE = 'none'


class VEHICLE_FRICTION_STATE(object):
    VFS_START = 1
    VFS_UPDATE = 2
    VFS_FINISHED = 3
    _ALL = (VFS_START, VFS_UPDATE, VFS_FINISHED)


class AVATAR_SUBFILTERS(object):
    CAMERA_ARCADE_REL_TRANSLATION = 0
    CAMERA_ARCADE_SHOT_POINT = 1
    CAMERA_SNIPER_ROTATION = 2
    CAMERA_STRATEGIC_SHOT_POINT = 3
    CAMERA_ARTY_SHOT_POINT = 4
    CAMERA_ARTY_TRANSLATION = 5
    CAMERA_ARTY_ROTATION = 6


class FILTER_INTERPOLATION_TYPE(object):
    LINEAR = 0
    SLERP_OF_CARTESIAN = 1
    ANGLE_RADIANS = 2
    SPHERICAL_RADIANS = 3


def getArenaStartTime(arenaUniqueID):
    return arenaUniqueID & 4294967295L


class PIERCING_POWER(object):
    PIERCING_POWER_LAW_POINT = 100.0
    PIERCING_POWER_LAW_DIST = 400.0

    @staticmethod
    def computePiercingPowerAtDist(piercingPower, dist, maxDist):
        pFirst, pLast = piercingPower
        if dist <= PIERCING_POWER.PIERCING_POWER_LAW_POINT:
            return pFirst
        if dist < maxDist + 4.0:
            return max(0.0, pFirst + (pLast - pFirst) * (dist - PIERCING_POWER.PIERCING_POWER_LAW_POINT) / PIERCING_POWER.PIERCING_POWER_LAW_DIST)
        return 0.0
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\constants.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:28 St�edn� Evropa (letn� �as)
