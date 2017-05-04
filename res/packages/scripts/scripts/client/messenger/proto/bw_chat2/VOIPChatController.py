# 2017.05.04 15:27:17 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/messenger/proto/bw_chat2/VOIPChatController.py
import BigWorld
import BattleReplay
import VOIP
import CommandMapping
from VOIP.voip_constants import VOIP_SUPPORTED_API
from debug_utils import LOG_WARNING
from adisp import async, process
from gui import GUI_SETTINGS
from helpers import dependency
from messenger.proto.events import g_messengerEvents
from messenger.proto.interfaces import IVOIPChatController
from account_helpers.settings_core.settings_constants import SOUND
from skeletons.account_helpers.settings_core import ISettingsCore

class VOIPChatController(IVOIPChatController):
    """
    This class represents VOIP chat controller.
    The main purpose for this class is to make the bridge between VOIPManager and GUI.
    It raises events using g_messengerEvents (VOIP shared events) depending on GUI settings
    and allows to request, check or invalidate some states.
    """
    __slots__ = ('__callbacks', '__captureDevicesCallbacks')
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self):
        """
        Constructor. Only create empty lists.
        """
        self.__callbacks = []
        self.__captureDevicesCallbacks = []

    def start(self):
        """
        Subscribe on VOIP manager events and initialize VOIP manager, internal variables.
        """
        voipMgr = VOIP.getVOIPManager()
        voipMgr.onInitialized += self.__initResponse
        voipMgr.onFailedToConnect += self.__failedResponse
        voipMgr.onCaptureDevicesUpdated += self.__captureDevicesResponse
        voipMgr.onPlayerSpeaking += self.__onPlayerSpeaking
        voipMgr.onStateToggled += self.__onStateToggled
        voipMgr.onJoinedChannel += self.__onJoinedChannel
        self.__initialize()

    def stop(self):
        """
        Tell the controller to stop working.
        It will unsubscribe from VOIP manager events and reset flags, internal variables
        """
        voipMgr = VOIP.getVOIPManager()
        voipMgr.onInitialized -= self.__initResponse
        voipMgr.onFailedToConnect -= self.__failedResponse
        voipMgr.onCaptureDevicesUpdated -= self.__captureDevicesResponse
        voipMgr.onPlayerSpeaking -= self.__onPlayerSpeaking
        voipMgr.onStateToggled -= self.__onStateToggled
        voipMgr.onJoinedChannel -= self.__onJoinedChannel
        self.__callbacks = []
        self.__captureDevicesCallbacks = []

    def isReady(self):
        """
        Implements IVOIPChatController interface, see its description.
        :return: bool
        """
        return VOIP.getVOIPManager().isInitialized()

    def isPlayerSpeaking(self, accountDBID):
        """
        Implement IVOIPChatController interface, see its description.
        :param accountDBID: player dbID
        :return: bool
        """
        if self.isVOIPEnabled():
            return bool(VOIP.getVOIPManager().isParticipantTalking(accountDBID))
        return False

    def isVOIPEnabled(self):
        """
        Implement IVOIPChatController interface, see its description.
        :return: bool
        """
        return GUI_SETTINGS.voiceChat

    def isVivox(self):
        """
        Implement IVOIPChatController interface, see its description.
        :return: bool
        """
        return VOIP.getVOIPManager().getAPI() == VOIP_SUPPORTED_API.VIVOX

    def isYY(self):
        """
        Implement IVOIPChatController interface, see its description.
        :return: bool
        """
        return VOIP.getVOIPManager().getAPI() == VOIP_SUPPORTED_API.YY

    def invalidateInitialization(self):
        """
        Raise the event (onVoiceChatInitFailed) only if all conditions are equal:
         1) voip is enabled
         2) a replay is not playing
         3) VOIP manager is not ready (not initialized)
        """
        if self.isVOIPEnabled() and not BattleReplay.isPlaying() and not self.isReady():
            g_messengerEvents.voip.onVoiceChatInitFailed()

    def setMicrophoneMute(self, isMuted, force = False):
        """ Sets local microphone mute.
        :param isMuted: is muted.
        :param force: is necessary to check whether EchoTest in progress and currentChannel exists
        """
        voipMgr = VOIP.getVOIPManager()
        if voipMgr is not None:
            if force or voipMgr.getCurrentChannel() and not voipMgr.isInTesting():
                voipMgr.setMicMute(muted=isMuted)
        return

    def invalidateMicrophoneMute(self):
        """
        This method checks if CMD_VOICECHAT_MUTE is not pressed to disable a MIC.
        Usually this method is called after switching from Hangar->Battle, Battle->Hangar, etc
        """
        keyCode = CommandMapping.g_instance.get('CMD_VOICECHAT_MUTE')
        if not BigWorld.isKeyDown(keyCode):
            self.setMicrophoneMute(isMuted=True, force=True)

    @async
    def requestCaptureDevices(self, firstTime = False, callback = None):
        """
        Request sound devices which can capture sound.
        This method is used by SettingsWindow to show devices in a drop-down list.
        :param firstTime: is it the first time? (the controller itself passes True during initialization
        another external classes should pass False or nothing)
        :param callback: the list of devices will come in the callback
        """
        voipMgr = VOIP.getVOIPManager()
        if voipMgr.getVOIPDomain() == '':
            LOG_WARNING('RequestCaptureDevices. Vivox is not supported')
            callback([])
            return
        if not self.isReady():
            LOG_WARNING('RequestCaptureDevices. Vivox has not been initialized')
            callback([])
            return
        options = self.settingsCore.options

        def resetCapturedDevice(devices, firstTime = firstTime):
            if firstTime:
                option = options.getSetting(SOUND.CAPTURE_DEVICES)
                option.apply(option.get(), firstTime)
            callback(devices)

        self.__captureDevicesCallbacks.append(resetCapturedDevice)
        voipMgr.requestCaptureDevices()

    @process
    def __initialize(self):
        """
        The method will initialize VOIP manager and request sound capture devices.
        It is done every time after user login.
        """
        serverSettings = getattr(BigWorld.player(), 'serverSettings', None)
        if serverSettings is not None and 'voipDomain' in serverSettings:
            domain = serverSettings['voipDomain']
        else:
            domain = ''
        yield self.__initializeSettings(domain)
        yield self.requestCaptureDevices(True)
        return

    @async
    def __initializeSettings(self, domain, callback):
        """
        Check if VOIP is enabled in client and initialize manager if necessary.
        :param domain: voip server URL
        :param callback: pass callback to get results
        """
        if self.isReady():
            vOIPSetting = self.settingsCore.options.getSetting('enableVoIP')
            vOIPSetting.initFromPref()
            callback(True)
            return
        if domain == '':
            LOG_WARNING('Initialize. Vivox is not supported')
            return
        self.__callbacks.append(callback)
        voipMgr = VOIP.getVOIPManager()
        if voipMgr.isNotInitialized():
            voipMgr.initialize(domain)
        vOIPSetting = self.settingsCore.options.getSetting('enableVoIP')
        vOIPSetting.initFromPref()

    def __initResponse(self, _):
        """
        This is callback for VOIPManager's 'onInitialized' event.
        Just proxy this event to g_messengerEvents and call callbacks.
        :param _: unused parameter
        """
        if self.isVOIPEnabled() and self.isReady():
            g_messengerEvents.voip.onVoiceChatInitSucceeded()
        while self.__callbacks:
            self.__callbacks.pop(0)(self.isReady())

    def __failedResponse(self):
        """
        This is callback for VOIPManager's 'onFailedToConnect' event.
        We just call invalidating to proxy this event for g_messengerEvents
        """
        self.invalidateInitialization()

    def __captureDevicesResponse(self):
        """
        This is callback for VOIPManager's 'onCaptureDevicesUpdated' event.
        We will notify subscribers with device list.
        """
        devices = VOIP.getVOIPManager().getCaptureDevices()
        while self.__captureDevicesCallbacks:
            self.__captureDevicesCallbacks.pop(0)(devices)

    def __onPlayerSpeaking(self, accountDBID, isSpeak):
        """
        Proxy of 'onPlayerSpeaking' event. But only if voip is enabled in settings.
        :param accountDBID: user db ID
        :param isSpeak: is the user speaking
        """
        if self.isVOIPEnabled():
            g_messengerEvents.voip.onPlayerSpeaking(accountDBID, bool(isSpeak))

    def __onStateToggled(self, isEnabled, _):
        """
        This is callback for VOIPManager's 'onStateToggled' event.
        Proxy this event to g_messengerEvents if voip is enabled.
        :param isEnabled: is VOIPManager enabled
        :param _: not used parameter
        """
        if self.isVOIPEnabled():
            g_messengerEvents.voip.onStateToggled(isEnabled)

    def __onJoinedChannel(self, data):
        """
        This is callback for VOIPManager's 'onJoinedChannel' event.
        After joining at channel, check if user presses PTY button to enable a MIC.
        For example, after echo-test, user can still pressing a button, enable mic in this case
        @param data: channel data
        """
        if self.isVOIPEnabled():
            keyCode = CommandMapping.g_instance.get('CMD_VOICECHAT_MUTE')
            if BigWorld.isKeyDown(keyCode):
                VOIP.getVOIPManager().setMicMute(False)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\messenger\proto\bw_chat2\VOIPChatController.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:17 St�edn� Evropa (letn� �as)
