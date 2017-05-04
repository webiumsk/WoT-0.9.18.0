# 2017.05.04 15:20:35 Støední Evropa (letní èas)
# Embedded file name: scripts/client/AvatarInputHandler/AimingSystems/steady_vehicle_matrix.py
from AvatarInputHandler import mathUtils
import BigWorld
import Math
from svarog_script.py_component import Component

class SteadyVehicleMatrixCalculator(Component):
    outputMProv = property(lambda self: self.__outputMProv)
    stabilisedMProv = property(lambda self: self.__stabilisedMProv)

    def __init__(self):
        self.__outputMProv = Math.WGCombinedMP()
        self.__stabilisedMProv = Math.WGAdaptiveMatrixProvider()

    def __relinkToIdentity(self):
        self.__outputMProv.rotationSrc = mathUtils.createIdentityMatrix()
        self.__outputMProv.translationSrc = self.__outputMProv.rotationSrc
        self.__stabilisedMProv.target = self.__outputMProv.rotationSrc

    def relinkSources(self):
        vehicle = BigWorld.player().getVehicleAttached()
        if vehicle is None:
            self.__relinkToIdentity()
            return
        else:
            typeDescriptor = vehicle.typeDescriptor
            if typeDescriptor.isPitchHullAimingAvailable:
                self.__outputMProv.rotationSrc = vehicle.filter.groundPlacingMatrixFiltered
                self.__outputMProv.translationSrc = vehicle.filter.stabilisedMatrix
            else:
                self.__outputMProv.rotationSrc = vehicle.filter.stabilisedMatrix
                self.__outputMProv.translationSrc = self.__outputMProv.rotationSrc
            self.__stabilisedMProv.target = vehicle.filter.stabilisedMatrix
            return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\AvatarInputHandler\AimingSystems\steady_vehicle_matrix.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:20:35 Støední Evropa (letní èas)
