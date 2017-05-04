# 2017.05.04 15:24:42 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/WindowViewMeta.py
from gui.Scaleform.daapi.view.meta.WrapperViewMeta import WrapperViewMeta

class WindowViewMeta(WrapperViewMeta):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends WrapperViewMeta
    """

    def onWindowMinimize(self):
        self._printOverrideError('onWindowMinimize')

    def onSourceLoaded(self):
        self._printOverrideError('onSourceLoaded')

    def onTryClosing(self):
        self._printOverrideError('onTryClosing')

    def as_getGeometryS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getGeometry()

    def as_setGeometryS(self, x, y, width, height):
        if self._isDAAPIInited():
            return self.flashObject.as_setGeometry(x, y, width, height)

    def as_isModalS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_isModal()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\WindowViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:42 Støední Evropa (letní èas)
