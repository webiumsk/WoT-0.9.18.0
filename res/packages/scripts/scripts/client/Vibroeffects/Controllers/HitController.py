# 2017.05.04 15:28:07 Støední Evropa (letní èas)
# Embedded file name: scripts/client/Vibroeffects/Controllers/HitController.py
import BigWorld
import Math
from constants import VEHICLE_HIT_EFFECT as HIT_EFFECT
from debug_utils import *
from OnceController import OnceController
import math

class HitController:

    def __init__(self, hitEffectCode):
        if hitEffectCode in (HIT_EFFECT.ARMOR_NOT_PIERCED, HIT_EFFECT.ARMOR_PIERCED_NO_DAMAGE):
            OnceController('hit_nonpenetration_veff')
            return
        if hitEffectCode in HIT_EFFECT.RICOCHETS:
            OnceController('hit_ricochet_veff')
            return
        if hitEffectCode == HIT_EFFECT.MAX_CODE + 1:
            OnceController('hit_splash_veff')
            return
        OnceController('hit_veff')
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\Vibroeffects\Controllers\HitController.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:07 Støední Evropa (letní èas)
