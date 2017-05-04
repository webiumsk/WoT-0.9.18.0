# 2017.05.04 15:24:16 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BaseRallyListViewMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyView import BaseRallyView

class BaseRallyListViewMeta(BaseRallyView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyView
    """

    def getRallyDetails(self, index):
        self._printOverrideError('getRallyDetails')

    def as_selectByIndexS(self, index):
        if self._isDAAPIInited():
            return self.flashObject.as_selectByIndex(index)

    def as_selectByIDS(self, rallyID):
        if self._isDAAPIInited():
            return self.flashObject.as_selectByID(rallyID)

    def as_getSearchDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getSearchDP()

    def as_setDetailsS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setDetails(value)

    def as_setVehiclesTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehiclesTitle(value)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BaseRallyListViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:16 Støední Evropa (letní èas)
