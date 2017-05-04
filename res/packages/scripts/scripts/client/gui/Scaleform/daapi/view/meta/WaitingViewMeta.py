# 2017.05.04 15:24:42 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/WaitingViewMeta.py
from gui.Scaleform.framework.entities.View import View

class WaitingViewMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    """

    def showS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.show(data)

    def hideS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.hide(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\WaitingViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:42 Støední Evropa (letní èas)
