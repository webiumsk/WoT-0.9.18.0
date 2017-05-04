# 2017.05.04 15:28:03 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/vehicle_systems/tankStructure.py
import BigWorld
from collections import namedtuple

class ModelStates:
    UNDAMAGED = 'undamaged'
    DESTROYED = 'destroyed'
    EXPLODED = 'exploded'


class TankPartNames:
    CHASSIS = 'chassis'
    HULL = 'hull'
    TURRET = 'turret'
    GUN = 'gun'
    ALL = (CHASSIS,
     HULL,
     TURRET,
     GUN)

    @staticmethod
    def getIdx(name):
        for idx, n in enumerate(TankPartNames.ALL):
            if n == name:
                return idx

        raise Exception('Invalid part name!')


VehiclePartsTuple = namedtuple('VehiclePartsTuple', TankPartNames.ALL)

class TankPartIndexes:
    CHASSIS = 0
    HULL = 1
    TURRET = 2
    GUN = 3
    ALL = (CHASSIS,
     HULL,
     TURRET,
     GUN)

    @staticmethod
    def getName(idx):
        return TankPartNames.ALL[idx]


class TankNodeNames:
    TRACK_LEFT_FRONT = 'HP_Track_LFront'
    TRACK_LEFT_REAR = 'HP_Track_LRear'
    TRACK_RIGHT_FRONT = 'HP_Track_RFront'
    TRACK_RIGHT_REAR = 'HP_Track_RRear'
    TRACK_LEFT_UP_FRONT = 'HP_TrackUp_LFront'
    TRACK_LEFT_UP_REAR = 'HP_TrackUp_LRear'
    TRACK_RIGHT_UP_FRONT = 'HP_TrackUp_RFront'
    TRACK_RIGHT_UP_REAR = 'HP_TrackUp_RRear'
    GUI = 'HP_gui'
    HULL_SWINGING = 'V'
    TURRET_JOINT = 'HP_turretJoint'
    HULL_FIRE_1 = 'HP_Fire_1'
    GUN_JOINT = 'HP_gunJoint'
    GUN_INCLINATION = 'Gun'
    GUN_RECOIL = 'G'
    TRACK_LEFT_MID = 'DM_Track_LMid'
    TRACK_RIGHT_MID = 'DM_Track_RMid'
    CHASSIS_MID_TRAIL = 'DM_Mid_Trail'


class TankSoundObjectsIndexes:
    CHASSIS = 0
    ENGINE = 1
    GUN = 2
    HIT = 3
    COUNT = 4


UNDAMAGED_SKELETON = VehiclePartsTuple(chassis=[('Tank', ''),
 (TankNodeNames.HULL_SWINGING, 'Tank'),
 (TankNodeNames.GUI, ''),
 (TankNodeNames.TRACK_LEFT_FRONT, ''),
 (TankNodeNames.TRACK_LEFT_REAR, ''),
 (TankNodeNames.TRACK_RIGHT_FRONT, ''),
 (TankNodeNames.TRACK_RIGHT_REAR, '')], hull=[('HP_Fire_1', ''),
 (TankNodeNames.TRACK_LEFT_UP_FRONT, ''),
 (TankNodeNames.TRACK_LEFT_UP_REAR, ''),
 (TankNodeNames.TRACK_RIGHT_UP_FRONT, ''),
 (TankNodeNames.TRACK_RIGHT_UP_REAR, '')], turret=[('HP_gunJoint', '')], gun=[(TankNodeNames.GUN_INCLINATION, ''), (TankNodeNames.GUN_RECOIL, TankNodeNames.GUN_INCLINATION), ('HP_gunFire', TankNodeNames.GUN_RECOIL)])
CRASHED_SKELETON = VehiclePartsTuple(chassis=[('Tank', ''), ('V', 'Tank'), ('HP_gui', '')], hull=[('HP_Fire_1', '')], turret=[('HP_gunJoint', '')], gun=[])

def getUndamagedSkeleton(vehicleDesc):
    exhaustNodes = getExhaustNodesFromDesc(vehicleDesc)
    exhaustNodes = [ (x, '') for x in exhaustNodes ]
    turretJointNode = (vehicleDesc.hull['turretHardPoints'][0], '')
    result = VehiclePartsTuple(chassis=UNDAMAGED_SKELETON.chassis, hull=UNDAMAGED_SKELETON.hull + exhaustNodes + [turretJointNode], turret=UNDAMAGED_SKELETON.turret, gun=UNDAMAGED_SKELETON.gun)
    return result


def getCrashedSkeleton(vehicleDesc):
    turretJointNode = (vehicleDesc.hull['turretHardPoints'][0], '')
    result = VehiclePartsTuple(chassis=CRASHED_SKELETON.chassis, hull=CRASHED_SKELETON.hull + [turretJointNode], turret=CRASHED_SKELETON.turret, gun=CRASHED_SKELETON.gun)
    return result


def getSkeleton(vehicleDesc, modelStateName):
    if modelStateName == 'undamaged':
        return getUndamagedSkeleton(vehicleDesc)
    return getCrashedSkeleton(vehicleDesc)


def getPartModelsFromDesc(vehicleDesc, modelStateName):
    return VehiclePartsTuple(vehicleDesc.chassis['models'][modelStateName], vehicleDesc.hull['models'][modelStateName], vehicleDesc.turret['models'][modelStateName], vehicleDesc.gun['models'][modelStateName])
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\vehicle_systems\tankStructure.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:03 St�edn� Evropa (letn� �as)
