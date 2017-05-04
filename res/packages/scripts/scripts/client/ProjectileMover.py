# 2017.05.04 15:20:04 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/ProjectileMover.py
from collections import namedtuple
import Math
import constants
import TriggersManager
from TriggersManager import TRIGGER_TYPE
from debug_utils import *
import FlockManager
from vehicle_systems.tankStructure import TankPartNames, TankNodeNames
from helpers import gEffectsDisabled

def ownVehicleGunPositionGetter():
    ownVehicle = BigWorld.entities.get(BigWorld.player().playerVehicleID, None)
    if ownVehicle:
        compoundModel = ownVehicle.appearance.compoundModel
        if compoundModel is None:
            return Math.Vector3(0.0, 0.0, 0.0)
        gunMat = ownVehicle.appearance.compoundModel.node(TankPartNames.GUN)
        if gunMat is None:
            gunMat = ownVehicle.appearance.compoundModel.node(TankNodeNames.TURRET_JOINT)
        return Math.Matrix(gunMat).translation
    else:
        return Math.Vector3(0.0, 0.0, 0.0)
        return


class ProjectileMover(object):
    __START_POINT_MAX_DIFF = 20
    __PROJECTILE_HIDING_TIME = 0.05
    __PROJECTILE_TIME_AFTER_DEATH = 2.0
    __AUTO_SCALE_DISTANCE = 180.0

    def __init__(self):
        self.__projectiles = dict()
        self.salvo = BigWorld.PySalvo(1000, 0, -100)
        self.__ballistics = BigWorld.PyBallisticsSimulator(lambda start, end: BigWorld.player().arena.collideWithSpaceBB(start, end), self.__killProjectile, self.__deleteProjectile)
        if self.__ballistics is not None:
            self.__ballistics.setFixedBallisticsParams(self.__PROJECTILE_HIDING_TIME, self.__PROJECTILE_TIME_AFTER_DEATH, self.__AUTO_SCALE_DISTANCE, constants.SERVER_TICK_LENGTH)
        player = BigWorld.player()
        if player is not None and player.inputHandler is not None:
            player.inputHandler.onCameraChanged += self.__onCameraChanged
        return

    def destroy(self):
        player = BigWorld.player()
        if player is not None and player.inputHandler is not None:
            player.inputHandler.onCameraChanged -= self.__onCameraChanged
        self.__ballistics = None
        for shotID in self.__projectiles.keys():
            self.__delProjectile(shotID)

        return

    def add(self, shotID, effectsDescr, gravity, refStartPoint, refVelocity, startPoint, maxDistance, attackerID = 0, tracerCameraPos = Math.Vector3(0, 0, 0)):
        import BattleReplay
        if BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            return
        else:
            if startPoint.distTo(refStartPoint) > ProjectileMover.__START_POINT_MAX_DIFF:
                startPoint = refStartPoint
            artID = effectsDescr.get('artilleryID')
            if artID is not None:
                self.salvo.addProjectile(artID, gravity, refStartPoint, refVelocity)
                return
            projectileMotor = self.__ballistics.addProjectile(shotID, gravity, refStartPoint, refVelocity, startPoint, maxDistance, attackerID, ownVehicleGunPositionGetter(), tracerCameraPos)
            if projectileMotor is None:
                return
            projModelName, projModelOwnShotName, projEffects = effectsDescr['projectile']
            isOwnShoot = attackerID == BigWorld.player().playerVehicleID
            model = BigWorld.Model(projModelOwnShotName if isOwnShoot else projModelName)
            proj = {'model': model,
             'motor': projectileMotor,
             'effectsDescr': effectsDescr,
             'showExplosion': False,
             'fireMissedTrigger': isOwnShoot,
             'autoScaleProjectile': isOwnShoot,
             'attackerID': attackerID,
             'effectsData': {}}
            if not gEffectsDisabled():
                BigWorld.player().addModel(model)
                model.addMotor(projectileMotor)
                model.visible = False
                model.visibleAttachments = True
                projEffects.attachTo(proj['model'], proj['effectsData'], 'flying', isPlayerVehicle=isOwnShoot, isArtillery=False)
            self.__projectiles[shotID] = proj
            FlockManager.getManager().onProjectile(startPoint)
            return

    def hide(self, shotID, endPoint):
        proj = self.__projectiles.pop(shotID, None)
        if proj is None:
            return
        else:
            if -shotID in self.__projectiles:
                self.__delProjectile(-shotID)
            self.__projectiles[-shotID] = proj
            proj['fireMissedTrigger'] = False
            proj['showExplosion'] = False
            self.__notifyProjectileHit(endPoint, proj)
            self.__ballistics.hideProjectile(shotID, endPoint)
            return

    def explode(self, shotID, effectsDescr, effectMaterial, endPoint, velocityDir):
        if effectsDescr.has_key('artilleryID'):
            return
        else:
            proj = self.__projectiles.get(shotID)
            if proj is None:
                __proj = {}
                __proj['effectsDescr'] = effectsDescr
                __proj['effectMaterial'] = effectMaterial
                __proj['attackerID'] = 0
                self.__addExplosionEffect(endPoint, __proj, velocityDir)
                return
            if proj['fireMissedTrigger']:
                proj['fireMissedTrigger'] = False
                TriggersManager.g_manager.fireTrigger(TRIGGER_TYPE.PLAYER_SHOT_MISSED)
            params = self.__ballistics.explodeProjectile(shotID, endPoint)
            if params is not None:
                if not proj.has_key('effectMaterial'):
                    proj['effectMaterial'] = effectMaterial
                self.__addExplosionEffect(params[0], proj, params[1])
            else:
                proj['showExplosion'] = True
                proj['effectMaterial'] = effectMaterial
            self.__notifyProjectileHit(endPoint, proj)
            return

    def hold(self, shotID):
        self.__ballistics.holdProjectile(shotID)

    def setSpaceID(self, spaceID):
        if self.__ballistics:
            self.__ballistics.setVariableBallisticsParams(spaceID)

    def __notifyProjectileHit(self, hitPosition, proj):
        caliber = proj['effectsDescr']['caliber']
        isOwnShot = proj['autoScaleProjectile']
        BigWorld.player().inputHandler.onProjectileHit(hitPosition, caliber, isOwnShot)
        FlockManager.getManager().onProjectile(hitPosition)

    def __addExplosionEffect(self, position, proj, velocityDir):
        effectTypeStr = proj.get('effectMaterial', '') + 'Hit'
        p0 = Math.Vector3(position.x, 1000, position.z)
        p1 = Math.Vector3(position.x, -1000, position.z)
        waterDist = BigWorld.wg_collideWater(p0, p1, False)
        if waterDist > 0:
            waterY = p0.y - waterDist
            testRes = BigWorld.wg_collideSegment(BigWorld.player().spaceID, p0, p1, 128)
            staticY = testRes[0].y if testRes is not None else waterY
            if staticY < waterY and position.y - waterY <= 0.1:
                shallowWaterDepth, rippleDiameter = proj['effectsDescr']['waterParams']
                if waterY - staticY < shallowWaterDepth:
                    effectTypeStr = 'shallowWaterHit'
                else:
                    effectTypeStr = 'deepWaterHit'
                position = Math.Vector3(position.x, waterY, position.z)
                self.__addWaterRipples(position, rippleDiameter, 5)
        keyPoints, effects, _ = proj['effectsDescr'][effectTypeStr]
        BigWorld.player().terrainEffects.addNew(position, effects, keyPoints, None, dir=velocityDir, start=position + velocityDir.scale(-1.0), end=position + velocityDir.scale(1.0), attackerID=proj['attackerID'])
        return

    def __killProjectile(self, shotID, position, impactVelDir):
        proj = self.__projectiles.get(shotID)
        if proj is None:
            return
        else:
            effectsDescr = proj['effectsDescr']
            projEffects = effectsDescr['projectile'][2]
            projEffects.detachFrom(proj['effectsData'], 'stopFlying')
            if proj['showExplosion']:
                self.__addExplosionEffect(position, proj, impactVelDir)
            return

    def __deleteProjectile(self, shotID):
        proj = self.__projectiles.get(shotID)
        if proj is None:
            return
        else:
            self.__delProjectile(shotID)
            if proj['fireMissedTrigger']:
                TriggersManager.g_manager.fireTrigger(TRIGGER_TYPE.PLAYER_SHOT_MISSED)
            return

    def __addWaterRipples(self, position, rippleDiameter, ripplesLeft):
        BigWorld.wg_addWaterRipples(position, rippleDiameter)
        if ripplesLeft > 0:
            BigWorld.callback(0, lambda : self.__addWaterRipples(position, rippleDiameter, ripplesLeft - 1))

    def __delProjectile(self, shotID):
        proj = self.__projectiles.pop(shotID)
        if proj is None:
            return
        else:
            projEffects = proj['effectsDescr']['projectile'][2]
            projEffects.detachAllFrom(proj['effectsData'])
            proj['model'].delMotor(proj['motor'])
            BigWorld.player().delModel(proj['model'])
            return

    def __onCameraChanged(self, cameraName, currentVehicleId = None):
        self.__ballistics.setBallisticsAutoScale(cameraName != 'sniper')


class EntityCollisionData(namedtuple('collisionData', ('entity', 'hitAngleCos', 'armor'))):

    def isVehicle(self):
        return self.entity.__class__.__name__ == 'Vehicle'


def collideEntities(startPoint, endPoint, entities, skipGun = False):
    res = None
    dir = endPoint - startPoint
    endDist = dir.length
    dir.normalise()
    for entity in entities:
        collisionResult = entity.collideSegment(startPoint, endPoint, skipGun)
        if collisionResult is None:
            continue
        dist = collisionResult[0]
        if dist < endDist:
            endPoint = startPoint + dir * dist
            endDist = dist
            res = (dist, EntityCollisionData(entity, collisionResult.hitAngleCos, collisionResult.armor))

    return res


def collideVehiclesAndStaticScene(startPoint, endPoint, vehicles, collisionFlags = 128, skipGun = False):
    testResStatic = BigWorld.wg_collideSegment(BigWorld.player().spaceID, startPoint, endPoint, collisionFlags)
    testResDynamic = collideEntities(startPoint, endPoint if testResStatic is None else testResStatic[0], vehicles, skipGun)
    if testResStatic is None and testResDynamic is None:
        return
    else:
        distDynamic = 1000000.0
        if testResDynamic is not None:
            distDynamic = testResDynamic[0]
        distStatic = 1000000.0
        if testResStatic is not None:
            distStatic = (testResStatic[0] - startPoint).length
        if distDynamic <= distStatic:
            dir = endPoint - startPoint
            dir.normalise()
            return (startPoint + distDynamic * dir, testResDynamic[1])
        return (testResStatic[0], None)
        return


def segmentMayHitEntity(entity, startPoint, endPoint):
    method = getattr(entity.filter, 'segmentMayHitEntity', lambda a, b: True)
    return method(startPoint, endPoint, 1)


def getCollidableEntities(exceptIDs, startPoint = None, endPoint = None):
    segmentTest = startPoint is not None and endPoint is not None
    vehicles = []
    for vehicleID in BigWorld.player().arena.vehicles.iterkeys():
        if vehicleID in exceptIDs:
            continue
        vehicle = BigWorld.entity(vehicleID)
        if vehicle is None or not vehicle.isStarted:
            continue
        if segmentTest and not segmentMayHitEntity(vehicle, startPoint, endPoint):
            continue
        vehicles.append(vehicle)

    for entity in ProjectileAwareEntities.entities:
        if segmentTest and not segmentMayHitEntity(entity, startPoint, endPoint):
            continue
        vehicles.append(entity)

    return vehicles


def collideDynamic(startPoint, endPoint, exceptIDs, skipGun = False):
    return collideEntities(startPoint, endPoint, getCollidableEntities(exceptIDs, startPoint, endPoint), skipGun)


def collideDynamicAndStatic(startPoint, endPoint, exceptIDs, collisionFlags = 128, skipGun = False):
    return collideVehiclesAndStaticScene(startPoint, endPoint, getCollidableEntities(exceptIDs, startPoint, endPoint), collisionFlags, skipGun)


class ProjectileAwareEntities(object):
    entities = list()

    @staticmethod
    def addEntity(entity):
        ProjectileAwareEntities.entities.append(entity)

    @staticmethod
    def removeEntity(entity):
        ProjectileAwareEntities.entities.remove(entity)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\ProjectileMover.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:20:05 St�edn� Evropa (letn� �as)
