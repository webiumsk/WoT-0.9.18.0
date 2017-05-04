# 2017.05.04 15:24:06 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/trainings/formatters.py
from gui.Scaleform.locale.MENU import MENU
from gui.shared.utils.functions import getArenaSubTypeName
from helpers import i18n
ICONS_MASK = '../maps/icons/map/%(prefix)s%(geometryName)s.png'

def getMapIconPath(arenaType, prefix = ''):
    return ICONS_MASK % {'geometryName': arenaType.geometryName,
     'prefix': prefix}


def getRoundLenString(roundLength):
    return i18n.makeString(MENU.TRAINING_INFO_TIMEOUT_VALUE, roundLength / 60)


def getTrainingRoomTitle(arenaType):
    return i18n.makeString(MENU.TRAINING_INFO_TITLE, arenaType.name)


def getArenaSubTypeString(arenaTypeID):
    arenaSubTypeName = getArenaSubTypeName(arenaTypeID)
    return i18n.makeString('#arenas:type/%s/name' % arenaSubTypeName)


def getPlayerStateString(state):
    return i18n.makeString('#menu:training/info/states/state%d' % state)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\trainings\formatters.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:06 St�edn� Evropa (letn� �as)
