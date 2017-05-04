# 2017.05.04 15:25:47 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/fortifications/fort_listener.py
from gui.shared.ClanCache import g_clanCache
from gui.shared.fortifications import interfaces

class fortProviderProperty(property):

    def __get__(self, obj, objType = None):
        return g_clanCache.fortProvider


class fortCtrlProperty(property):

    def __get__(self, obj, objType = None):
        provider = g_clanCache.fortProvider
        ctrl = None
        if provider:
            ctrl = provider.getController()
        return ctrl


class fortStateProperty(property):

    def __get__(self, obj, objType = None):
        provider = g_clanCache.fortProvider
        state = None
        if provider:
            state = provider.getState()
        return state


class FortListener(interfaces.IFortListener):

    @fortProviderProperty
    def fortProvider(self):
        return None

    @fortCtrlProperty
    def fortCtrl(self):
        return interfaces.IFortController()

    @fortStateProperty
    def fortState(self):
        return None

    def startFortListening(self):
        provider = self.fortProvider
        if provider:
            provider.addListener(self)

    def stopFortListening(self):
        provider = self.fortProvider
        if provider:
            provider.removeListener(self)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\fortifications\fort_listener.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:25:47 St�edn� Evropa (letn� �as)
