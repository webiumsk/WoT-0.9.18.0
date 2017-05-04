# 2017.05.04 15:24:45 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/AbstractViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class AbstractViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def onFocusIn(self, alias):
        self._printOverrideError('onFocusIn')

    def as_setupContextHintBuilderS(self, builderLnk, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setupContextHintBuilder(builderLnk, data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\entities\abstract\AbstractViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:45 Støední Evropa (letní èas)
