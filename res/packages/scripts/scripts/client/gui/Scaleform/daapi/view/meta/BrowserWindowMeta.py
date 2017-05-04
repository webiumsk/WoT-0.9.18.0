# 2017.05.04 15:24:18 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BrowserWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class BrowserWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def as_configureS(self, title, showActionBtn, showCloseBtn):
        if self._isDAAPIInited():
            return self.flashObject.as_configure(title, showActionBtn, showCloseBtn)

    def as_setSizeS(self, width, height):
        if self._isDAAPIInited():
            return self.flashObject.as_setSize(width, height)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BrowserWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:19 Støední Evropa (letní èas)
