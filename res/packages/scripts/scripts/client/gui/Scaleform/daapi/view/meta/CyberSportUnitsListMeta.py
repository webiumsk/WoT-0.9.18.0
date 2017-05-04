# 2017.05.04 15:24:23 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CyberSportUnitsListMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyListView import BaseRallyListView

class CyberSportUnitsListMeta(BaseRallyListView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyListView
    """

    def getTeamData(self, index):
        self._printOverrideError('getTeamData')

    def refreshTeams(self):
        self._printOverrideError('refreshTeams')

    def filterVehicles(self):
        self._printOverrideError('filterVehicles')

    def loadPrevious(self):
        self._printOverrideError('loadPrevious')

    def loadNext(self):
        self._printOverrideError('loadNext')

    def as_setDummyS(self, data):
        """
        :param data: Represented by DummyVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDummy(data)

    def as_setDummyVisibleS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setDummyVisible(visible)

    def as_setHeaderS(self, data):
        """
        :param data: Represented by UnitListViewHeaderVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setHeader(data)

    def as_updateNavigationBlockS(self, data):
        """
        :param data: Represented by NavigationBlockVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateNavigationBlock(data)

    def as_updateRallyIconS(self, iconPath):
        if self._isDAAPIInited():
            return self.flashObject.as_updateRallyIcon(iconPath)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\CyberSportUnitsListMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:23 Støední Evropa (letní èas)
