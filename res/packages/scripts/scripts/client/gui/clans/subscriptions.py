# 2017.05.04 15:21:33 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/clans/subscriptions.py
from gui.clans.interfaces import IClanListener
from gui.shared.utils.listeners_collection import ListenersCollection

class ClansListeners(ListenersCollection):

    def __init__(self):
        super(ClansListeners, self).__init__()
        self._setListenerClass(IClanListener)

    def notify(self, eventType, *args):
        self._invokeListeners(eventType, *args)

    def addListener(self, listener):
        if not self.hasListener(listener):
            super(ClansListeners, self).addListener(listener)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\clans\subscriptions.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:33 Støední Evropa (letní èas)
