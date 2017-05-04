# 2017.05.04 15:28:07 Støední Evropa (letní èas)
# Embedded file name: scripts/client/Vibroeffects/Controllers/OnceController.py
import BigWorld
from Vibroeffects import VibroManager
from debug_utils import *

class OnceController:

    def __init__(self, effectName, gain = 100):
        VibroManager.g_instance.launchQuickEffect(effectName, 1, gain)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\Vibroeffects\Controllers\OnceController.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:07 Støední Evropa (letní èas)
