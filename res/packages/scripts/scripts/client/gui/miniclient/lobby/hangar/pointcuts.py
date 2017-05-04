# 2017.05.04 15:21:49 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/miniclient/lobby/hangar/pointcuts.py
import aspects
from helpers import aop

class ShowMiniclientInfo(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.hangar.Hangar', 'Hangar', '_populate', aspects=(aspects.ShowMiniclientInfo,))


class DisableTankServiceButtons(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.hangar.Hangar', 'Hangar', 'as_setupAmmunitionPanelS', aspects=(aspects.DisableTankServiceButtons(config),))


class MaintenanceButtonFlickering(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.hangar.AmmunitionPanel', 'AmmunitionPanel', 'as_setAmmoS', aspects=(aspects.MaintenanceButtonFlickering(config),))


class DeviceButtonsFlickering(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.hangar.AmmunitionPanel', 'AmmunitionPanel', 'as_setDataS', aspects=(aspects.DeviceButtonsFlickering(config),))


class TankModelHangarVisibility(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, 'CurrentVehicle', '_CurrentVehicle', 'isInHangar', aspects=(aspects.TankModelHangarVisibility(config),))


class TankHangarStatus(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, 'CurrentVehicle', '_CurrentVehicle', 'getHangarMessage', aspects=(aspects.TankHangarStatus(config),))


class EnableCrew(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.hangar.Hangar', 'Hangar', 'as_setCrewEnabledS', aspects=(aspects.EnableCrew(config),))


class ChangeLobbyMenuTooltip(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby', 'LobbyMenu', '_getVersionMessage', aspects=(aspects.ChangeLobbyMenuTooltip,))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\miniclient\lobby\hangar\pointcuts.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:49 St�edn� Evropa (letn� �as)
