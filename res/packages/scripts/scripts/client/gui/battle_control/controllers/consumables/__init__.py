# 2017.05.04 15:21:18 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/battle_control/controllers/consumables/__init__.py
from gui.battle_control.controllers.consumables import ammo_ctrl
from gui.battle_control.controllers.consumables import equipment_ctrl
from gui.battle_control.controllers.consumables import opt_devices_ctrl

def createAmmoCtrl(setup):
    if setup.isReplayRecording:
        return ammo_ctrl.AmmoReplayRecorder(setup.replayCtrl)
    if setup.isReplayPlaying:
        return ammo_ctrl.AmmoReplayPlayer(setup.replayCtrl)
    return ammo_ctrl.AmmoController()


def createEquipmentCtrl(setup):
    if setup.isReplayPlaying:
        clazz = equipment_ctrl.EquipmentsReplayPlayer
    else:
        clazz = equipment_ctrl.EquipmentsController
    return clazz()


def createOptDevicesCtrl():
    return opt_devices_ctrl.OptionalDevicesController()


__all__ = ('createAmmoCtrl', 'createEquipmentCtrl', 'createOptDevicesCtrl')
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\battle_control\controllers\consumables\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:18 Støední Evropa (letní èas)
