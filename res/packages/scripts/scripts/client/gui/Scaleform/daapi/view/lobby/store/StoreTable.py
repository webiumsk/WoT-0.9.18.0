# 2017.05.04 15:23:59 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/store/StoreTable.py
from gui.Scaleform.daapi.view.lobby.store.StoreTableDataProvider import StoreTableDataProvider
from gui.Scaleform.daapi.view.meta.StoreTableMeta import StoreTableMeta

class StoreTable(StoreTableMeta):

    def __init__(self):
        super(StoreTable, self).__init__()
        self._storeTableDataProvider = None
        return

    def _populate(self):
        super(StoreTable, self)._populate()
        self._storeTableDataProvider = StoreTableDataProvider()
        self._storeTableDataProvider.setFlashObject(self.as_getTableDataProviderS())

    def _dispose(self):
        if self._storeTableDataProvider is not None:
            self._storeTableDataProvider.clearList()
            self._storeTableDataProvider._dispose()
            self._storeTableDataProvider = None
        super(StoreTable, self)._dispose()
        return

    def setDataProviderValues(self, dpList):
        if self._storeTableDataProvider is not None:
            self._storeTableDataProvider.buildList(dpList)
        return

    def refreshStoreTableDataProvider(self):
        if self._storeTableDataProvider is not None:
            self._storeTableDataProvider.refresh()
        return

    def clearStoreTableDataProvider(self):
        if self._storeTableDataProvider is not None:
            self._storeTableDataProvider.clearList()
        return

    def setItemWrapper(self, itemWrapper):
        if self._storeTableDataProvider is not None:
            self._storeTableDataProvider.setItemWrapper(itemWrapper)
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\store\StoreTable.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:59 St�edn� Evropa (letn� �as)
