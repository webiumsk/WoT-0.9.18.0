# 2017.05.04 15:25:43 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/formatters/tankmen.py
from gui.shared import g_itemsCache

def formatDeletedTankmanStr(tankman):
    vehicle = g_itemsCache.items.getItemByCD(tankman.vehicleNativeDescr.type.compactDescr)
    return tankman.fullUserName + ' (%s, %s)' % (tankman.roleUserName, vehicle.userName)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\formatters\tankmen.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:25:43 Støední Evropa (letní èas)
