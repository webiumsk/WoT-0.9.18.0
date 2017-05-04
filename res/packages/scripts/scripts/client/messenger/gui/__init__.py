# 2017.05.04 15:26:58 Støední Evropa (letní èas)
# Embedded file name: scripts/client/messenger/gui/__init__.py
from messenger.m_constants import MESSENGER_SCOPE

def setGUIEntries(decorator):
    from messenger.gui.Scaleform.battle_entry import BattleEntry
    from messenger.gui.Scaleform.lobby_entry import LobbyEntry
    decorator.setEntry(MESSENGER_SCOPE.LOBBY, LobbyEntry())
    decorator.setEntry(MESSENGER_SCOPE.BATTLE, BattleEntry())
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\messenger\gui\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:58 Støední Evropa (letní èas)
