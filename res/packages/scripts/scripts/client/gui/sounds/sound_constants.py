# 2017.05.04 15:26:33 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/sounds/sound_constants.py
from shared_utils import CONST_CONTAINER

class EnabledStatus(object):
    ENABLED_DEFAULT = 0
    ENABLED_BY_USER = 1
    DISABLED = 2

    @classmethod
    def isEnabled(cls, status):
        return status in (cls.ENABLED_DEFAULT, cls.ENABLED_BY_USER)


class HQRenderState(object):
    LQ_HQ_ENABLED = 0
    LQ_FOR_ALL = 1
    HQ_FOR_ALL = 2

    @classmethod
    def isEnabled(cls, status, isMSR):
        if status == cls.LQ_HQ_ENABLED:
            return not isMSR
        else:
            return status == cls.HQ_FOR_ALL


PLAYING_SOUND_CHECK_PERIOD = 1.0
IS_ADVANCED_LOGGING = False

class SoundSystems(CONST_CONTAINER):
    UNKNOWN = 0
    WWISE = 1

    @classmethod
    def getUserName(cls, sysID):
        return cls.getKeyByValue(sysID) or cls.UNKNOWN


class SoundFilters(CONST_CONTAINER):
    EMPTY = 1
    FILTERED_HANGAR = 2
    FORT_FILTER = 3


class SPEAKERS_CONFIG(object):
    AUTO_DETECTION = 0
    SPEAKER_SETUP_2_0 = 2
    SPEAKER_SETUP_5_1 = 5
    SPEAKER_SETUP_7_1 = 7
    RANGE = (AUTO_DETECTION,
     SPEAKER_SETUP_2_0,
     SPEAKER_SETUP_5_1,
     SPEAKER_SETUP_7_1)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\sounds\sound_constants.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:33 St�edn� Evropa (letn� �as)
