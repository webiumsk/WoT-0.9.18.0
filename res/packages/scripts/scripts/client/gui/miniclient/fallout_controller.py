# 2017.05.04 15:21:48 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/miniclient/fallout_controller.py
from helpers import aop

class _ParametrizeInitAspect(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        return False


class InitFalloutPointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.game_control.fallout_controller', 'FalloutController', 'isAvailable', aspects=(_ParametrizeInitAspect,))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\miniclient\fallout_controller.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:48 Støední Evropa (letní èas)
