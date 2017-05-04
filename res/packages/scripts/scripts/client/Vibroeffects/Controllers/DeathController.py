# 2017.05.04 15:28:07 Støední Evropa (letní èas)
# Embedded file name: scripts/client/Vibroeffects/Controllers/DeathController.py
from OnceController import OnceController

class DeathController:
    __wasVehicleAlive = None

    def update(self, isVehicleAlive):
        if self.__wasVehicleAlive and not isVehicleAlive:
            OnceController('crit_death_veff')
        self.__wasVehicleAlive = isVehicleAlive
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\Vibroeffects\Controllers\DeathController.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:07 Støední Evropa (letní èas)
