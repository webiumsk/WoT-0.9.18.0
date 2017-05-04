# 2017.05.04 15:24:35 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/QuestsSeasonsViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class QuestsSeasonsViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def onShowAwardsClick(self):
        self._printOverrideError('onShowAwardsClick')

    def onTileClick(self, tileID):
        self._printOverrideError('onTileClick')

    def onSlotClick(self, slotID):
        self._printOverrideError('onSlotClick')

    def as_setDataS(self, data):
        """
        :param data: Represented by QuestsSeasonsViewVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setSeasonsDataS(self, data):
        """
        :param data: Represented by SeasonsDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSeasonsData(data)

    def as_setSlotsDataS(self, data):
        """
        :param data: Represented by QuestSlotsDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSlotsData(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\QuestsSeasonsViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:35 Støední Evropa (letní èas)
