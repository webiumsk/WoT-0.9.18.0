# 2017.05.04 15:24:21 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ConfirmExchangeDialogMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ConfirmExchangeDialogMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def exchange(self, goldValue):
        self._printOverrideError('exchange')

    def as_updateS(self, data):
        """
        :param data: Represented by ConfirmExchangeDialogVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_update(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\ConfirmExchangeDialogMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:21 Støední Evropa (letní èas)
