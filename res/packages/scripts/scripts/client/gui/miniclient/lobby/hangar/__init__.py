# 2017.05.04 15:21:49 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/miniclient/lobby/hangar/__init__.py
import pointcuts as _pointcuts

def configure_pointcuts(config):
    _pointcuts.DisableTankServiceButtons(config)
    _pointcuts.MaintenanceButtonFlickering(config)
    _pointcuts.DeviceButtonsFlickering(config)
    _pointcuts.ShowMiniclientInfo()
    _pointcuts.TankHangarStatus(config)
    _pointcuts.TankModelHangarVisibility(config)
    _pointcuts.EnableCrew(config)
    _pointcuts.ChangeLobbyMenuTooltip()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\miniclient\lobby\hangar\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:49 Støední Evropa (letní èas)
