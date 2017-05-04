# 2017.05.04 15:24:28 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortListMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyListView import BaseRallyListView

class FortListMeta(BaseRallyListView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyListView
    """

    def changeDivisionIndex(self, index):
        self._printOverrideError('changeDivisionIndex')

    def as_getDivisionsDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDivisionsDP()

    def as_setSelectedDivisionS(self, index):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedDivision(index)

    def as_setCreationEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCreationEnabled(value)

    def as_setRegulationInfoS(self, data):
        """
        :param data: Represented by FortRegulationInfoVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setRegulationInfo(data)

    def as_setTableHeaderS(self, data):
        """
        :param data: Represented by NormalSortingTableHeaderVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTableHeader(data)

    def as_tryShowTextMessageS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_tryShowTextMessage()

    def as_setCurfewEnabledS(self, showWarning):
        if self._isDAAPIInited():
            return self.flashObject.as_setCurfewEnabled(showWarning)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\FortListMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:28 Støední Evropa (letní èas)
