# 2017.05.04 15:24:21 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ConfirmDialogMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ConfirmDialogMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def submit(self, selected):
        self._printOverrideError('submit')

    def as_setSettingsS(self, data):
        """
        :param data: Represented by ConfirmDialogVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSettings(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\ConfirmDialogMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:21 Støední Evropa (letní èas)
