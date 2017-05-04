# 2017.05.04 15:20:51 Støední Evropa (letní èas)
# Embedded file name: scripts/client/FX/__init__.py
"""
The FX module implements a data-driven special effects framework.

For more information, please refer to bigworld/docs/howto_SFX
"""
s_sectionProcessors = {}

def typeCheck(self, listOrType):
    return 1


import Actors
import Events
import Joints
from Effects._Effect import prerequisites
from Effects.OneShot import OneShot
from Effects.Persistent import Persistent
from Effects.Buffered import getBufferedOneShotEffect
from Effects.Buffered import bufferedOneShotEffect
from Effects.Buffered import cleanupBufferedEffects
from Effects.Buffered import outputOverruns
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\FX\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:20:51 Støední Evropa (letní èas)
