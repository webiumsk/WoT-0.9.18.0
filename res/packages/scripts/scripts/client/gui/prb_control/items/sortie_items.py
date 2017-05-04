# 2017.05.04 15:22:19 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/prb_control/items/sortie_items.py
from UnitBase import SORTIE_DIVISION_NAMES, SORTIE_DIVISION, SORTIE_DIVISION_NAME_TO_FLAGS
from debug_utils import LOG_ERROR
_SORTIE_DIVISION_LEVEL_TO_NAME = dict([ (v, k) for k, v in SORTIE_DIVISION_NAMES.iteritems() ])

def getDivisionsOrderData():
    ORDER = SORTIE_DIVISION._ORDER
    result = [''] * len(ORDER)
    for level, name in SORTIE_DIVISION_NAMES.iteritems():
        if level in ORDER:
            result[ORDER.index(level)] = (name, level, SORTIE_DIVISION_NAME_TO_FLAGS[name])

    return result


def getDivisionLevel(name):
    level = 0
    if name in _SORTIE_DIVISION_LEVEL_TO_NAME:
        level = _SORTIE_DIVISION_LEVEL_TO_NAME[name]
    else:
        LOG_ERROR('Name of division is not valid', level)
    return level


def getDivisionLevelByUnit(unit):
    divisionName = getDivisionNameByType(unit.getRosterTypeID())
    if divisionName:
        return getattr(SORTIE_DIVISION, getDivisionNameByType(unit.getRosterTypeID()))


def getDivisionNameByType(rosterTypeID):
    for name, flags in SORTIE_DIVISION_NAME_TO_FLAGS.iteritems():
        if rosterTypeID == flags:
            return name

    return ''


def getDivisionNameByUnit(unit):
    if unit is None:
        LOG_ERROR('Unit is not defined')
        return ''
    else:
        return getDivisionNameByType(unit.getRosterTypeID())
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\items\sortie_items.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:19 St�edn� Evropa (letn� �as)
