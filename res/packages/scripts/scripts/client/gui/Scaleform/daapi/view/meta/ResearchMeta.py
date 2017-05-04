# 2017.05.04 15:24:36 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ResearchMeta.py
from gui.Scaleform.daapi.view.lobby.techtree.ResearchView import ResearchView

class ResearchMeta(ResearchView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends ResearchView
    """

    def requestNationData(self):
        self._printOverrideError('requestNationData')

    def getResearchItemsData(self, vehCD, rootChanged):
        self._printOverrideError('getResearchItemsData')

    def onResearchItemsDrawn(self):
        self._printOverrideError('onResearchItemsDrawn')

    def goToTechTree(self, nation):
        self._printOverrideError('goToTechTree')

    def exitFromResearch(self):
        self._printOverrideError('exitFromResearch')

    def goToVehicleView(self, itemCD):
        self._printOverrideError('goToVehicleView')

    def compareVehicle(self, itemCD):
        self._printOverrideError('compareVehicle')

    def as_drawResearchItemsS(self, nation, vehCD):
        if self._isDAAPIInited():
            return self.flashObject.as_drawResearchItems(nation, vehCD)

    def as_setFreeXPS(self, freeXP):
        if self._isDAAPIInited():
            return self.flashObject.as_setFreeXP(freeXP)

    def as_setInstalledItemsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInstalledItems(data)

    def as_setWalletStatusS(self, walletStatus):
        if self._isDAAPIInited():
            return self.flashObject.as_setWalletStatus(walletStatus)

    def as_setRootNodeVehCompareDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setRootNodeVehCompareData(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\ResearchMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:36 Støední Evropa (letní èas)
