# 2017.05.04 15:24:38 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StoreTableMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class StoreTableMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def refreshStoreTableDataProvider(self):
        self._printOverrideError('refreshStoreTableDataProvider')

    def as_getTableDataProviderS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getTableDataProvider()

    def as_setDataS(self, data):
        """
        :param data: Represented by StoreTableVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\StoreTableMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:38 Støední Evropa (letní èas)
