# 2017.05.04 15:25:08 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/locale/NATIONS.py
"""
This file was generated using the wgpygen.
Please, don't edit this file manually.
"""
from debug_utils import LOG_WARNING

class NATIONS(object):
    USSR = '#nations:ussr'
    GERMANY = '#nations:germany'
    USA = '#nations:usa'
    FRANCE = '#nations:france'
    UK = '#nations:uk'
    JAPAN = '#nations:japan'
    CZECH = '#nations:czech'
    CHINA = '#nations:china'
    SWEDEN = '#nations:sweden'
    ALL_ENUM = (USSR,
     GERMANY,
     USA,
     FRANCE,
     UK,
     JAPAN,
     CZECH,
     CHINA,
     SWEDEN)

    @classmethod
    def all(cls, key0):
        outcome = '#nations:{}'.format(key0)
        if outcome not in cls.ALL_ENUM:
            LOG_WARNING('Localization key "{}" not found'.format(outcome))
            return None
        else:
            return outcome
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\locale\NATIONS.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:25:08 St�edn� Evropa (letn� �as)
