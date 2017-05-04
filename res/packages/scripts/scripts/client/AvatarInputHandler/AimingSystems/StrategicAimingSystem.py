# 2017.05.04 15:20:36 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/AvatarInputHandler/AimingSystems/StrategicAimingSystem.py
import BigWorld
import Math
from Math import Vector3, Matrix
import math
from AvatarInputHandler import mathUtils, AimingSystems
from AvatarInputHandler.AimingSystems import IAimingSystem
from AvatarInputHandler.cameras import _clampPoint2DInBox2D

class StrategicAimingSystem(IAimingSystem):
    _LOOK_DIR = Vector3(0, -math.cos(0.001), math.sin(0.001))
    height = property(lambda self: self.__height)
    heightFromPlane = property(lambda self: self.__heightFromPlane)
    planePosition = property(lambda self: self._planePosition)

    def __init__(self, height, yaw):
        IAimingSystem.__init__(self)
        self._matrix = mathUtils.createRotationMatrix((yaw, 0, 0))
        self._planePosition = Vector3(0, 0, 0)
        self.__height = height
        self.__heightFromPlane = 0.0

    def destroy(self):
        pass

    def enable(self, targetPos):
        self.updateTargetPos(targetPos)

    def disable(self):
        pass

    def getDesiredShotPoint(self, terrainOnlyCheck = False):
        return AimingSystems.getDesiredShotPoint(self._matrix.translation, Vector3(0, -1, 0), True, True, terrainOnlyCheck)

    def handleMovement(self, dx, dy):
        shift = self._matrix.applyVector(Vector3(dx, 0, dy))
        self._planePosition += Vector3(shift.x, 0, shift.z)
        self._updateMatrix()

    def updateTargetPos(self, targetPos):
        self._planePosition.x = targetPos.x
        self._planePosition.z = targetPos.z
        self._updateMatrix()

    def _clampToArenaBB(self):
        bb = BigWorld.player().arena.arenaType.boundingBox
        pos2D = _clampPoint2DInBox2D(bb[0], bb[1], Math.Vector2(self._planePosition.x, self._planePosition.z))
        self._planePosition.x = pos2D[0]
        self._planePosition.z = pos2D[1]

    def _updateMatrix(self):
        self._clampToArenaBB()
        collPoint = BigWorld.wg_collideSegment(BigWorld.player().spaceID, self._planePosition + Math.Vector3(0, 1000.0, 0), self._planePosition + Math.Vector3(0, -250.0, 0), 3)
        self.__heightFromPlane = 0.0 if collPoint is None else collPoint[0][1]
        self._matrix.translation = self._planePosition + Vector3(0, self.__heightFromPlane + self.__height, 0)
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\AvatarInputHandler\AimingSystems\StrategicAimingSystem.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:20:36 St�edn� Evropa (letn� �as)
