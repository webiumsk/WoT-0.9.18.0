# 2017.05.04 15:24:39 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StoreViewMeta.py
from gui.Scaleform.framework.entities.View import View

class StoreViewMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    """

    def onClose(self):
        self._printOverrideError('onClose')

    def onTabChange(self, tabId):
        self._printOverrideError('onTabChange')

    def as_showStorePageS(self, viewAlias):
        if self._isDAAPIInited():
            return self.flashObject.as_showStorePage(viewAlias)

    def as_initS(self, data):
        """
        :param data: Represented by StoreViewInitVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_init(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\StoreViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:39 Støední Evropa (letní èas)
