# 2017.05.04 15:20:01 Støední Evropa (letní èas)
# Embedded file name: scripts/client/GasAttack.py
import BigWorld
from debug_utils import LOG_DEBUG

class GasAttack(BigWorld.UserDataObject):

    def __init__(self):
        BigWorld.UserDataObject.__init__(self)
        LOG_DEBUG('GasAttack ', self.position)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\GasAttack.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:20:01 Støední Evropa (letní èas)
