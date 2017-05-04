# 2017.05.04 15:21:52 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/miniclient/tech_tree/pointcuts.py
import aspects
from helpers import aop

class OnTechTreePopulate(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.techtree.TechTree', 'TechTree', '_populate', aspects=(aspects.OnTechTreePopulate,))


class OnBuyVehicle(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.vehicle_obtain_windows', 'VehicleBuyWindow', 'submit', aspects=(aspects.OnBuyVehicle(config),))


class OnRestoreVehicle(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.vehicle_obtain_windows', 'VehicleRestoreWindow', 'submit', aspects=(aspects.OnRestoreVehicle(config),))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\miniclient\tech_tree\pointcuts.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:52 Støední Evropa (letní èas)
