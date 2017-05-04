# 2017.05.04 15:24:37 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SettingsWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class SettingsWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def applySettings(self, settings, isCloseWnd):
        self._printOverrideError('applySettings')

    def autodetectQuality(self):
        self._printOverrideError('autodetectQuality')

    def startVOIPTest(self, isVoiceTestStarted):
        self._printOverrideError('startVOIPTest')

    def updateCaptureDevices(self):
        self._printOverrideError('updateCaptureDevices')

    def onSettingsChange(self, controlID, controlVal):
        self._printOverrideError('onSettingsChange')

    def altVoicesPreview(self):
        self._printOverrideError('altVoicesPreview')

    def altBulbPreview(self, sampleID):
        self._printOverrideError('altBulbPreview')

    def isSoundModeValid(self):
        self._printOverrideError('isSoundModeValid')

    def showWarningDialog(self, dialogID, settings, isCloseWnd):
        self._printOverrideError('showWarningDialog')

    def onTabSelected(self, tabId):
        self._printOverrideError('onTabSelected')

    def onCounterTargetVisited(self, itemName):
        self._printOverrideError('onCounterTargetVisited')

    def autodetectAcousticType(self):
        self._printOverrideError('autodetectAcousticType')

    def canSelectAcousticType(self, index):
        self._printOverrideError('canSelectAcousticType')

    def as_setDataS(self, settingsData):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(settingsData)

    def as_setCaptureDevicesS(self, captureDeviceIdx, devicesData):
        if self._isDAAPIInited():
            return self.flashObject.as_setCaptureDevices(captureDeviceIdx, devicesData)

    def as_onVibroManagerConnectS(self, isConnect):
        if self._isDAAPIInited():
            return self.flashObject.as_onVibroManagerConnect(isConnect)

    def as_updateVideoSettingsS(self, videoSettings):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVideoSettings(videoSettings)

    def as_confirmWarningDialogS(self, isOk, dialogID):
        if self._isDAAPIInited():
            return self.flashObject.as_confirmWarningDialog(isOk, dialogID)

    def as_ConfirmationOfApplicationS(self, isApplied):
        if self._isDAAPIInited():
            return self.flashObject.as_ConfirmationOfApplication(isApplied)

    def as_openTabS(self, tabIndex):
        if self._isDAAPIInited():
            return self.flashObject.as_openTab(tabIndex)

    def as_setGraphicsPresetS(self, presetNum):
        if self._isDAAPIInited():
            return self.flashObject.as_setGraphicsPreset(presetNum)

    def as_isPresetAppliedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_isPresetApplied()

    def as_setCountersDataS(self, tabsList):
        if self._isDAAPIInited():
            return self.flashObject.as_setCountersData(tabsList)

    def as_onSoundSpeakersPresetApplyS(self, isApply):
        if self._isDAAPIInited():
            return self.flashObject.as_onSoundSpeakersPresetApply(isApply)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\SettingsWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:37 St�edn� Evropa (letn� �as)
