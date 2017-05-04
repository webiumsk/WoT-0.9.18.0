# 2017.05.04 15:24:29 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortTransportConfirmationWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortTransportConfirmationWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def onCancel(self):
        self._printOverrideError('onCancel')

    def onTransporting(self, size):
        self._printOverrideError('onTransporting')

    def as_setMaxTransportingSizeS(self, maxSizeStr):
        if self._isDAAPIInited():
            return self.flashObject.as_setMaxTransportingSize(maxSizeStr)

    def as_setFooterTextS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setFooterText(text)

    def as_setDataS(self, data):
        """
        :param data: Represented by TransportingVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_enableForFirstTransportingS(self, isFirstTransporting):
        if self._isDAAPIInited():
            return self.flashObject.as_enableForFirstTransporting(isFirstTransporting)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\FortTransportConfirmationWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:29 Støední Evropa (letní èas)
