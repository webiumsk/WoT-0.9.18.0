# 2017.05.04 15:24:52 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/genConsts/FITTING_TYPES.py


class FITTING_TYPES(object):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    """
    OPTIONAL_DEVICE = 'optionalDevice'
    EQUIPMENT = 'equipment'
    SHELL = 'shell'
    VEHICLE = 'vehicle'
    MODULE = 'module'
    ORDER = 'order'
    STORE_SLOTS = [VEHICLE,
     MODULE,
     SHELL,
     OPTIONAL_DEVICE,
     EQUIPMENT]
    ARTEFACT_SLOTS = [OPTIONAL_DEVICE, EQUIPMENT]
    VEHICLE_GUN = 'vehicleGun'
    VEHICLE_TURRET = 'vehicleTurret'
    VEHICLE_CHASSIS = 'vehicleChassis'
    VEHICLE_ENGINE = 'vehicleEngine'
    VEHICLE_RADIO = 'vehicleRadio'
    MANDATORY_SLOTS = [VEHICLE_GUN,
     VEHICLE_TURRET,
     VEHICLE_CHASSIS,
     VEHICLE_ENGINE,
     VEHICLE_RADIO]
    RESERVE_SLOT1 = 'reserveSlot1'
    RESERVE_SLOT2 = 'reserveSlot2'
    RESERVE_SLOT3 = 'reserveSlot3'
    RESERVES_SLOTS = [RESERVE_SLOT1, RESERVE_SLOT2, RESERVE_SLOT3]
    TARGET_OTHER = 'other'
    TARGET_HANGAR = 'hangar'
    TARGET_HANGAR_CANT_INSTALL = 'hangarCantInstall'
    TARGET_VEHICLE = 'vehicle'
    ITEM_TARGETS = [TARGET_OTHER,
     TARGET_HANGAR,
     TARGET_HANGAR_CANT_INSTALL,
     TARGET_VEHICLE]
    OPTIONAL_DEVICE_FITTING_ITEM_RENDERER = 'OptDevFittingItemRendererUI'
    GUN_TURRET_FITTING_ITEM_RENDERER = 'GunTurretFittingItemRendererUI'
    RESERVE_FITTING_ITEM_RENDERER = 'ReserveFittingItemRendererUI'
    ENGINE_CHASSIS_FITTING_ITEM_RENDERER = 'EngineChassisFittingItemRendererUI'
    RADIO_FITTING_ITEM_RENDERER = 'RadioFittingItemRendererUI'
    FITTING_RENDERERS = [OPTIONAL_DEVICE_FITTING_ITEM_RENDERER,
     GUN_TURRET_FITTING_ITEM_RENDERER,
     RESERVE_FITTING_ITEM_RENDERER,
     ENGINE_CHASSIS_FITTING_ITEM_RENDERER,
     RADIO_FITTING_ITEM_RENDERER]
    OPTIONAL_DEVICE_RENDERER_DATA_CLASS_NAME = 'net.wg.gui.lobby.modulesPanel.data.OptionalDeviceVO'
    MODULE_FITTING_RENDERER_DATA_CLASS_NAME = 'net.wg.gui.lobby.modulesPanel.data.ModuleVO'
    FITTING_RENDERER_DATA_NAMES = [OPTIONAL_DEVICE_RENDERER_DATA_CLASS_NAME, MODULE_FITTING_RENDERER_DATA_CLASS_NAME]
    HANGAR_POPOVER_TOP_MARGIN = 80
    VEHPREVIEW_POPOVER_MIN_AVAILABLE_HEIGHT = 575
    LARGE_POPOVER_WIDTH = 540
    MEDUIM_POPOVER_WIDTH = 500
    SHORT_POPOVER_WIDTH = 440
    RESERVE_POPOVER_WIDTH = 480
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\genConsts\FITTING_TYPES.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:52 St�edn� Evropa (letn� �as)