# 2017.05.04 15:24:16 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BarracksMeta.py
from gui.Scaleform.framework.entities.View import View

class BarracksMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    """

    def invalidateTanksList(self):
        self._printOverrideError('invalidateTanksList')

    def setFilter(self, nation, role, tankType, location, nationID):
        self._printOverrideError('setFilter')

    def onShowRecruitWindowClick(self, rendererData, menuEnabled):
        self._printOverrideError('onShowRecruitWindowClick')

    def actTankman(self, dataCompact):
        self._printOverrideError('actTankman')

    def buyBerths(self):
        self._printOverrideError('buyBerths')

    def closeBarracks(self):
        self._printOverrideError('closeBarracks')

    def setTankmenFilter(self):
        self._printOverrideError('setTankmenFilter')

    def openPersonalCase(self, value, tabNumber):
        self._printOverrideError('openPersonalCase')

    def as_setTankmenS(self, data):
        """
        :param data: Represented by BarracksTankmenVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTankmen(data)

    def as_updateTanksListS(self, provider):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTanksList(provider)

    def as_setTankmenFilterS(self, nation, role, tankType, location, nationID):
        if self._isDAAPIInited():
            return self.flashObject.as_setTankmenFilter(nation, role, tankType, location, nationID)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BarracksMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:16 Støední Evropa (letní èas)
