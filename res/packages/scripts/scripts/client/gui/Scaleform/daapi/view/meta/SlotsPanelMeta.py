# 2017.05.04 15:24:38 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SlotsPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class SlotsPanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def getSlotTooltipBody(self, orderID):
        self._printOverrideError('getSlotTooltipBody')

    def as_setPanelPropsS(self, data):
        """
        :param data: Represented by SlotsPanelPropsVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setPanelProps(data)

    def as_setSlotsS(self, orders):
        """
        :param orders: Represented by Vector.<SlotVO> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSlots(orders)

    def as_updateSlotS(self, data):
        """
        :param data: Represented by SlotVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateSlot(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\SlotsPanelMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:38 Støední Evropa (letní èas)
