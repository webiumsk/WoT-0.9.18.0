# 2017.05.04 15:28:05 Støední Evropa (letní èas)
# Embedded file name: scripts/client/vehicle_systems/components/world_connectors.py
import BigWorld
from svarog_script import auto_properties
import svarog_script.py_component
from vehicle_systems.tankStructure import TankPartNames

class GunRotatorConnector(svarog_script.py_component.Component):

    def __init__(self, appearance):
        self.__appearance = appearance

    def activate(self):
        soundEffect = BigWorld.player().gunRotator.soundEffect
        if soundEffect is not None:
            soundEffect.connectSoundToMatrix(self.__appearance.compoundModel.node(TankPartNames.TURRET))
        return

    def deactivate(self):
        soundEffect = BigWorld.player().gunRotator.soundEffect
        if soundEffect is not None:
            soundEffect.lockSoundMatrix()
        return

    def destroy(self):
        self.__appearance = None
        self.processVehicleDeath(None)
        return

    def processVehicleDeath(self, vehicleDamageState):
        self.deactivate()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\vehicle_systems\components\world_connectors.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:06 Støední Evropa (letní èas)
