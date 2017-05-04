# 2017.05.04 15:21:52 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/miniclient/vehicle_compare/aspects.py
from helpers import aop

class MakeVehicleCompareUnavailable(aop.Aspect):

    def atReturn(self, cd):
        cd.change()
        return False
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\miniclient\vehicle_compare\aspects.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:52 Støední Evropa (letní èas)
