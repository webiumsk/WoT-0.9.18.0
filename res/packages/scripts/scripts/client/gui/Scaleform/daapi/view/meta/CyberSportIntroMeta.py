# 2017.05.04 15:24:23 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CyberSportIntroMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyIntroView import BaseRallyIntroView

class CyberSportIntroMeta(BaseRallyIntroView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyIntroView
    """

    def requestVehicleSelection(self):
        self._printOverrideError('requestVehicleSelection')

    def startAutoMatching(self):
        self._printOverrideError('startAutoMatching')

    def showSelectorPopup(self):
        self._printOverrideError('showSelectorPopup')

    def showStaticTeamStaff(self):
        self._printOverrideError('showStaticTeamStaff')

    def as_setSelectedVehicleS(self, data):
        """
        :param data: Represented by IntroVehicleVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedVehicle(data)

    def as_setTextsS(self, data):
        """
        :param data: Represented by CSIntroViewTextsVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTexts(data)

    def as_setNoVehiclesS(self, warnTooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_setNoVehicles(warnTooltip)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\CyberSportIntroMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:23 Støední Evropa (letní èas)
