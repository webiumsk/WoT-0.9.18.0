# 2017.05.04 15:24:15 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AbstractRallyViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class AbstractRallyViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def viewSize(self, width, height):
        self._printOverrideError('viewSize')

    def as_setPyAliasS(self, alias):
        if self._isDAAPIInited():
            return self.flashObject.as_setPyAlias(alias)

    def as_getPyAliasS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getPyAlias()

    def as_loadBrowserS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_loadBrowser()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\AbstractRallyViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:15 Støední Evropa (letní èas)
