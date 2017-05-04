# 2017.05.04 15:20:30 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/AvatarInputHandler/FalloutDeathMode.py
import weakref
import BigWorld
import GUI
import SoundGroups
from AvatarInputHandler import aih_global_binding
from DynamicCameras.ArcadeCamera import ArcadeCamera
from control_modes import IControlMode, _ARCADE_CAM_PIVOT_POS
from mathUtils import clamp

class FalloutDeathMode(IControlMode):
    curVehicleID = property(lambda self: self.__curVehicleID)
    aimingMode = property(lambda self: self._aimingMode)
    __aimOffset = aih_global_binding.bindRO(aih_global_binding.BINDING_ID.AIM_OFFSET)

    def __init__(self, dataSection, avatarInputHandler):
        self.__aih = weakref.proxy(avatarInputHandler)
        self.__cam = ArcadeCamera(dataSection['camera'], dataSection.readVector2('defaultOffset'))
        self.__isEnabled = False
        self.__curVehicleID = None
        self._aimingMode = 0
        return

    def create(self):
        self.__cam.create(_ARCADE_CAM_PIVOT_POS, None, True)
        return

    def destroy(self):
        self.disable()
        self.__cam.destroy()
        self.__cam = None
        return

    def enable(self, **args):
        SoundGroups.g_instance.changePlayMode(0)
        self.__cam.enable(None, False, args.get('postmortemParams'))
        player = BigWorld.player()
        self.__curVehicleID = player.playerVehicleID
        self.__isEnabled = True
        return

    def disable(self):
        self.__isEnabled = False
        self.__cam.disable()

    def handleMouseEvent(self, dx, dy, dz):
        raise self.__isEnabled or AssertionError
        GUI.mcursor().position = self.__aimOffset
        self.__cam.update(dx, dy, clamp(-1.0, 1.0, dz))
        return True
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\AvatarInputHandler\FalloutDeathMode.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:20:30 St�edn� Evropa (letn� �as)
