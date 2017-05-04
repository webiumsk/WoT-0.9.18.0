# 2017.05.04 15:24:27 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortIntelligenceClanFilterPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class FortIntelligenceClanFilterPopoverMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    """

    def useFilter(self, value, isDefaultData):
        """
        :param value: Represented by IntelligenceClanFilterVO (AS)
        """
        self._printOverrideError('useFilter')

    def getAvailabilityProvider(self):
        self._printOverrideError('getAvailabilityProvider')

    def as_setDescriptionsTextS(self, header, clanLevel, startHourRange):
        if self._isDAAPIInited():
            return self.flashObject.as_setDescriptionsText(header, clanLevel, startHourRange)

    def as_setButtonsTextS(self, defaultButtonText, applyButtonText, cancelButtonText):
        if self._isDAAPIInited():
            return self.flashObject.as_setButtonsText(defaultButtonText, applyButtonText, cancelButtonText)

    def as_setButtonsTooltipsS(self, defaultButtonTooltip, applyButtonTooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_setButtonsTooltips(defaultButtonTooltip, applyButtonTooltip)

    def as_setDataS(self, data):
        """
        :param data: Represented by IntelligenceClanFilterVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\FortIntelligenceClanFilterPopoverMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:27 Støední Evropa (letní èas)
