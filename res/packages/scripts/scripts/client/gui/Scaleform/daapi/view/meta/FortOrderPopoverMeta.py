# 2017.05.04 15:24:28 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortOrderPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class FortOrderPopoverMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    """

    def requestForCreateOrder(self):
        self._printOverrideError('requestForCreateOrder')

    def requestForUseOrder(self):
        self._printOverrideError('requestForUseOrder')

    def getLeftTime(self):
        self._printOverrideError('getLeftTime')

    def getLeftTimeStr(self):
        self._printOverrideError('getLeftTimeStr')

    def getLeftTimeTooltip(self):
        self._printOverrideError('getLeftTimeTooltip')

    def openQuest(self, questID):
        self._printOverrideError('openQuest')

    def openOrderDetailsWindow(self):
        self._printOverrideError('openOrderDetailsWindow')

    def as_setInitDataS(self, data):
        """
        :param data: Represented by OrderPopoverVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_disableOrderS(self, daisable):
        if self._isDAAPIInited():
            return self.flashObject.as_disableOrder(daisable)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\FortOrderPopoverMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:28 Støední Evropa (letní èas)
