# 2017.05.04 15:26:51 Støední Evropa (letní èas)
# Embedded file name: scripts/client/messenger/inject.py
from messenger import MessengerEntry

class messengerEntryProperty(property):

    def __get__(self, obj, objType = None):
        return MessengerEntry.g_instance


class channelsCtrlProperty(property):

    def __get__(self, obj, objType = None):
        return MessengerEntry.g_instance.gui.channelsCtrl
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\messenger\inject.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:51 Støední Evropa (letní èas)
