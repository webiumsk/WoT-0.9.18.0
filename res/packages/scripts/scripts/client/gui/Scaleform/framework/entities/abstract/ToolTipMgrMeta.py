# 2017.05.04 15:24:47 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/ToolTipMgrMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class ToolTipMgrMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    """

    def onCreateComplexTooltip(self, tooltipId, stateType):
        self._printOverrideError('onCreateComplexTooltip')

    def onCreateTypedTooltip(self, tooltipType, args, stateType):
        self._printOverrideError('onCreateTypedTooltip')

    def onHideTooltip(self, tooltipId):
        self._printOverrideError('onHideTooltip')

    def as_showS(self, tooltipData, linkage):
        if self._isDAAPIInited():
            return self.flashObject.as_show(tooltipData, linkage)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\entities\abstract\ToolTipMgrMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:47 Støední Evropa (letní èas)
