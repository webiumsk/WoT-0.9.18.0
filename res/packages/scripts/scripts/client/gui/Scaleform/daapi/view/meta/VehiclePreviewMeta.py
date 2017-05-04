# 2017.05.04 15:24:41 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehiclePreviewMeta.py
from gui.Scaleform.framework.entities.View import View

class VehiclePreviewMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    """

    def closeView(self):
        self._printOverrideError('closeView')

    def onBackClick(self):
        self._printOverrideError('onBackClick')

    def onBuyOrResearchClick(self):
        self._printOverrideError('onBuyOrResearchClick')

    def onOpenInfoTab(self, index):
        self._printOverrideError('onOpenInfoTab')

    def onCompareClick(self):
        self._printOverrideError('onCompareClick')

    def as_setStaticDataS(self, data):
        """
        :param data: Represented by VehPreviewStaticDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticData(data)

    def as_updateInfoDataS(self, data):
        """
        :param data: Represented by VehPreviewInfoPanelVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateInfoData(data)

    def as_updateVehicleStatusS(self, status):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehicleStatus(status)

    def as_updatePriceS(self, data):
        """
        :param data: Represented by VehPreviewPriceDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updatePrice(data)

    def as_updateBuyButtonS(self, data):
        """
        :param data: Represented by VehPreviewBuyButtonVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateBuyButton(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\VehiclePreviewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:41 Støední Evropa (letní èas)
