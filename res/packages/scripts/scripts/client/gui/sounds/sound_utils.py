# 2017.05.04 15:26:33 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/sounds/sound_utils.py
from debug_utils import LOG_DEBUG
from gui.sounds.sound_constants import IS_ADVANCED_LOGGING
if IS_ADVANCED_LOGGING:

    def SOUND_DEBUG(msg, *kargs):
        LOG_DEBUG('[SOUND]', msg, kargs)


else:

    def SOUND_DEBUG(msg, *kargs):
        pass
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\sounds\sound_utils.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:33 Støední Evropa (letní èas)
