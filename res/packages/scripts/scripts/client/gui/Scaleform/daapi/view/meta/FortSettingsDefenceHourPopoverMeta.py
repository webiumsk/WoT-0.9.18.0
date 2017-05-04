# 2017.05.04 15:24:29 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortSettingsDefenceHourPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class FortSettingsDefenceHourPopoverMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    """

    def onApply(self, hour):
        self._printOverrideError('onApply')

    def as_setDataS(self, data):
        """
        :param data: Represented by DefenceHourPopoverVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setTextsS(self, data):
        """
        :param data: Represented by DefenceHourPopoverVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTexts(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\FortSettingsDefenceHourPopoverMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:29 Støední Evropa (letní èas)
