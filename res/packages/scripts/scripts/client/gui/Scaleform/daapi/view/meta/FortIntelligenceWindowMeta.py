# 2017.05.04 15:24:28 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortIntelligenceWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortIntelligenceWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def requestClanFortInfo(self, index):
        self._printOverrideError('requestClanFortInfo')

    def as_setStatusTextS(self, statusText):
        if self._isDAAPIInited():
            return self.flashObject.as_setStatusText(statusText)

    def as_getSearchDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getSearchDP()

    def as_getCurrentListIndexS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getCurrentListIndex()

    def as_selectByIndexS(self, index):
        if self._isDAAPIInited():
            return self.flashObject.as_selectByIndex(index)

    def as_setTableHeaderS(self, data):
        """
        :param data: Represented by NormalSortingTableHeaderVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTableHeader(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\FortIntelligenceWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:28 Støední Evropa (letní èas)
