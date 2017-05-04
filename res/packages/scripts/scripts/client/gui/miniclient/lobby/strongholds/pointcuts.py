# 2017.05.04 15:21:51 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/miniclient/lobby/strongholds/pointcuts.py
from helpers import aop
import aspects

class MakeStrongholdsUnavailable(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.header.LobbyHeader', 'LobbyHeader', '_updateStrongholdsSelector', aspects=(aspects.MakeStrongholdsUnavailable(),))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\miniclient\lobby\strongholds\pointcuts.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:51 Støední Evropa (letní èas)
