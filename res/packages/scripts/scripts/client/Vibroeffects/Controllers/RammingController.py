# 2017.05.04 15:28:07 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/Vibroeffects/Controllers/RammingController.py
import BigWorld
from OnceController import OnceController
from constants import DESTRUCTIBLE_MATKIND

class RammingController:
    RAMMING_EXECUTION_DELAY = 2.5
    MIN_IMPACT_SPEED = 3
    __executionForbidden = None

    def __allowExecution(self):
        self.__executionForbidden = None
        return

    def destroy(self):
        if self.__executionForbidden is not None:
            BigWorld.cancelCallback(self.__executionForbidden)
        return

    def execute(self, vehicleSpeed, matKind):
        if not self.__executionForbidden and vehicleSpeed >= self.MIN_IMPACT_SPEED:
            effectName = 'ramming_vehicle_veff'
            if matKind is not None and DESTRUCTIBLE_MATKIND.MIN <= matKind <= DESTRUCTIBLE_MATKIND.MAX:
                effectName = 'ramming_destructible_veff'
            else:
                effectName = 'ramming_indestructible_veff'
            OnceController(effectName)
            self.__executionForbidden = BigWorld.callback(self.RAMMING_EXECUTION_DELAY, self.__allowExecution)
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\Vibroeffects\Controllers\RammingController.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:07 St�edn� Evropa (letn� �as)
