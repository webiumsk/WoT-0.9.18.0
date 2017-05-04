# 2017.05.04 15:21:57 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/prb_control/entities/base/__init__.py
from adisp import process
from CurrentVehicle import g_currentVehicle
from gui.shared.utils import functions

def vehicleAmmoCheck(func):
    """
    Vehicle ammo loadout check decorator.
    Args:
        func: decorated function
    
    Returns:
        wrapped function with ammo check
    """

    @process
    def wrapper(*args, **kwargs):
        res = yield functions.checkAmmoLevel((g_currentVehicle.item,))
        if res:
            func(*args, **kwargs)
        elif kwargs.get('callback') is not None:
            kwargs.get('callback')(False)
        return

    return wrapper
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\base\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:57 Støední Evropa (letní èas)
