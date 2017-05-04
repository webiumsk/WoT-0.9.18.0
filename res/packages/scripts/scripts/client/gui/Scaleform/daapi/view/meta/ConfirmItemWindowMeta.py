# 2017.05.04 15:24:21 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ConfirmItemWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ConfirmItemWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def submit(self, count, currency):
        self._printOverrideError('submit')

    def as_setDataS(self, value):
        """
        :param value: Represented by ConfirmItemWindowVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(value)

    def as_setSettingsS(self, value):
        """
        :param value: Represented by DialogSettingsVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSettings(value)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\ConfirmItemWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:21 Støední Evropa (letní èas)
