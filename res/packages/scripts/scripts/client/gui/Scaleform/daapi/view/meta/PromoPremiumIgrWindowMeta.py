# 2017.05.04 15:24:34 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PromoPremiumIgrWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class PromoPremiumIgrWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def as_setTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setTitle(value)

    def as_setTextS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setText(value)

    def as_setWindowTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setWindowTitle(value)

    def as_setApplyButtonLabelS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setApplyButtonLabel(value)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\PromoPremiumIgrWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:34 Støední Evropa (letní èas)
