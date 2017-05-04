# 2017.05.04 15:24:22 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CustomizationBuyWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class CustomizationBuyWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def buy(self):
        self._printOverrideError('buy')

    def selectItem(self, id):
        self._printOverrideError('selectItem')

    def deselectItem(self, id):
        self._printOverrideError('deselectItem')

    def changePriceItem(self, id, priceMode):
        self._printOverrideError('changePriceItem')

    def as_getPurchaseDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getPurchaseDP()

    def as_setInitDataS(self, data):
        """
        :param data: Represented by InitBuyWindowVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_setTotalDataS(self, data):
        """
        :param data: Represented by PurchasesTotalVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTotalData(data)

    def as_setBuyBtnEnabledS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setBuyBtnEnabled(isEnabled)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\CustomizationBuyWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:22 Støední Evropa (letní èas)
