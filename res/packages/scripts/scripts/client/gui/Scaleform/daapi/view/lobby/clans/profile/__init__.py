# 2017.05.04 15:23:07 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/clans/profile/__init__.py
from gui.shared.utils.functions import getArenaGeomentryName
from helpers.i18n import makeString
MAX_MEMBERS_IN_CLAN = 100

def getI18ArenaById(arenaId):
    return makeString('#arenas:%s/name' % getArenaGeomentryName(arenaId))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\clans\profile\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:07 Støední Evropa (letní èas)
