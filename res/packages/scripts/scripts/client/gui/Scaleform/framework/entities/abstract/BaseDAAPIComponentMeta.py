# 2017.05.04 15:24:46 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/BaseDAAPIComponentMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class BaseDAAPIComponentMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    """

    def registerFlashComponent(self, component, alias):
        """
        :param component: Represented by IDAAPIModule (AS)
        """
        self._printOverrideError('registerFlashComponent')

    def isFlashComponentRegistered(self, alias):
        self._printOverrideError('isFlashComponentRegistered')

    def unregisterFlashComponent(self, alias):
        self._printOverrideError('unregisterFlashComponent')

    def as_populateS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_populate()

    def as_disposeS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_dispose()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\entities\abstract\BaseDAAPIComponentMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:46 Støední Evropa (letní èas)
