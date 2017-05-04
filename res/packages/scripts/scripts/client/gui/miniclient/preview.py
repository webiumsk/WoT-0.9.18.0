# 2017.05.04 15:21:48 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/miniclient/preview.py
from helpers import aop

class ChangeVehicleIsPreviewAllowed(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, 'gui.shared.gui_items.Vehicle', 'Vehicle', 'isPreviewAllowed', aspects=(_ChangedIsPreviewAllowed(config),))


class _ChangedIsPreviewAllowed(aop.Aspect):

    def __init__(self, config):
        self.__vehicle_is_available = config['vehicle_is_available']
        aop.Aspect.__init__(self)

    def atCall(self, cd):
        vehicle = cd.self
        cd.avoid()
        return self.__vehicle_is_available(vehicle) and cd.function(cd.self)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\miniclient\preview.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:48 Støední Evropa (letní èas)
