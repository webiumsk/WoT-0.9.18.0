# 2017.05.04 15:24:16 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BaseExchangeWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class BaseExchangeWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def exchange(self, data):
        self._printOverrideError('exchange')

    def as_setPrimaryCurrencyS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPrimaryCurrency(value)

    def as_exchangeRateS(self, data):
        """
        :param data: Represented by BaseExchangeWindowRateVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_exchangeRate(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BaseExchangeWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:16 Støední Evropa (letní èas)
