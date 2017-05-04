# 2017.05.04 15:23:13 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/exchange/BaseExchangeWindow.py
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.view.meta.BaseExchangeWindowMeta import BaseExchangeWindowMeta

class BaseExchangeWindow(BaseExchangeWindowMeta):

    def __init__(self, ctx = None):
        super(BaseExchangeWindow, self).__init__(self)

    def _populate(self):
        super(BaseExchangeWindow, self)._populate()
        self._subscribe()

    def _subscribe(self):
        pass

    def _setGoldCallBack(self, gold):
        self.as_setPrimaryCurrencyS(gold)

    def _dispose(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        super(BaseExchangeWindow, self)._dispose()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\exchange\BaseExchangeWindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:13 Støední Evropa (letní èas)
