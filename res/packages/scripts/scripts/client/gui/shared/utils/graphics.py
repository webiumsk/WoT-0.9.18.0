# 2017.05.04 15:26:23 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/utils/graphics.py
import BigWorld
import math
from collections import namedtuple
from debug_utils import LOG_WARNING
from shared_utils import CONST_CONTAINER, findFirst
import GUI
MIN_SCREEN_WIDTH = 1024
MIN_SCREEN_HEIGHT = 768
MIN_COLOR_DEPTH = 23
VideoMode = namedtuple('VideoMode', 'index width height colorDepth label refreshRate')
WindowSize = namedtuple('WindowSize', 'width height refreshRate')
BorderlessSize = namedtuple('BorderlessSize', 'behaviour posX posY width height monitor')
SCALE_PREFIX = ('auto', 'x%d')

class GRAPHICS_SETTINGS(CONST_CONTAINER):
    pass


class GRAPHICS_SETTINGS_STATUS(CONST_CONTAINER):
    NONE = 0
    MAJOR_CHANGED = 1
    MINOR_CHANGED = 2


class _GraphicsStatus(object):

    def __init__(self, value):
        self.__value = value

    def isReset(self):
        return self.__value == GRAPHICS_SETTINGS_STATUS.MAJOR_CHANGED

    def isShowWarning(self):
        return self.__value == GRAPHICS_SETTINGS_STATUS.MINOR_CHANGED

    @classmethod
    def markProcessed(cls):
        BigWorld.resetGraphicsSettingsStatus()


def getStatus():
    return _GraphicsStatus(BigWorld.graphicsSettingsStatus())


def isVideoModeSuitable(mode):
    return mode.width >= MIN_SCREEN_WIDTH and mode.height >= MIN_SCREEN_HEIGHT and mode.colorDepth >= MIN_COLOR_DEPTH


def getSuitableVideoModes():
    result = []
    currentVideoMode = BigWorld.videoModeIndex()
    for monitorModes in BigWorld.listVideoModesAllMonitors():
        modes = []
        for mode in monitorModes:
            m = VideoMode(*mode)
            if isVideoModeSuitable(m) or m.index == currentVideoMode:
                modes.append(m)

        result.append(modes)

    return tuple(result)


def getSuitableWindowSizes():
    result = []
    for idx, monitorModes in enumerate(getSuitableVideoModes()):
        maxSize = WindowSize(*BigWorld.wg_getMaxWindowedResolution(idx))
        modes = []
        for mode in monitorModes:
            if mode.width <= maxSize.width and mode.height <= maxSize.height:
                modes.append(WindowSize(mode.width, mode.height, mode.refreshRate))

        if maxSize not in modes:
            modes.append(maxSize)
        result.append(modes)

    return tuple(result)


GraphicSetting = namedtuple('GraphicSetting', 'label value options hint advanced needRestart isArray delayed')

def getGraphicsSetting(settingName):
    setting = BigWorld.graphicSetting(settingName)
    if setting is None:
        return
    else:
        return GraphicSetting(*setting)
        return


def getGraphicsPresets(presetIdx = None):
    if presetIdx is not None:
        return BigWorld.getGraphicsPreset(presetIdx)
    else:
        return BigWorld.getGraphicsPresets()


def getGraphicsPresetsIndices():
    return BigWorld.getGraphicsPresetsIndices()


def getGraphicSettingImages(settingName):
    result = {}
    data = getGraphicsSetting(settingName)
    if data is not None:
        for idx, (label, supported, _, _) in enumerate(data.options):
            if supported:
                result[idx] = '../maps/icons/settings/%s/%s.png' % (settingName, str(label).replace(' ', '_'))

    return result


def getResolution():
    currWindowSize = g_monitorSettings.currentWindowSize
    width = currWindowSize.width if currWindowSize.width > 0 else MIN_SCREEN_WIDTH
    height = currWindowSize.height if currWindowSize.height > 0 else MIN_SCREEN_HEIGHT
    return WindowSize(min(width, MIN_SCREEN_WIDTH), min(height, MIN_SCREEN_HEIGHT), currWindowSize.refreshRate)


def getInterfaceScalesList(size, powerOfTwo = True):
    result = [SCALE_PREFIX[0]]
    if powerOfTwo:
        scale = max(min(int(math.log(max(size[0] / getResolution().width, 1.0), 2)), int(math.log(max(size[1] / getResolution().height, 1.0), 2))), 0)
        for size in xrange(scale + 1):
            result.append(SCALE_PREFIX[1] % 2 ** size)

    else:
        scale = min(int(size[0] / MIN_SCREEN_WIDTH), int(size[1] / MIN_SCREEN_HEIGHT))
        for i in xrange(1, scale):
            result.append(SCALE_PREFIX[1] % i)

    return result


class MonitorSettings(object):

    def __init__(self):
        self.__suitableVideoModes = getSuitableVideoModes()
        self.__suitableWindowSizes = getSuitableWindowSizes()
        self.__monitorChanged = False
        self.__currentMonitorIdx = self.activeMonitor

    @property
    def windowSizes(self):
        return self.__suitableWindowSizes[self.activeMonitor]

    @property
    def currentWindowSize(self):
        return WindowSize(*map(int, BigWorld.wg_getCurrentResolution(BigWorld.WindowModeWindowed)))

    @property
    def borderlessSizes(self):
        return self.__suitableVideoModes[self.activeMonitor]

    @property
    def currentBorderlessSize(self):
        if self.windowMode == BigWorld.WindowModeBorderless:
            return BorderlessSize(*map(int, BigWorld.getBorderlessParameters()))
        else:
            return VideoMode(*BigWorld.listBorderlessResolutionsAllMonitors()[self.currentMonitor][0])

    @property
    def videoModes(self):
        return self.videoModesForAdapterOutputIndex(self.activeMonitor)

    def videoModesForAdapterOutputIndex(self, adapterOutputIndex):
        return self.__suitableVideoModes[adapterOutputIndex]

    @property
    def currentVideoMode(self):
        for videoMode in self.videoModes:
            if videoMode.index == BigWorld.videoModeIndex():
                return videoMode

        return findFirst(None, self.videoModes)

    def changeMonitor(self, monitorIdx):
        if self.__currentMonitorIdx != monitorIdx:
            self.__monitorChanged = True
        self.__currentMonitorIdx = monitorIdx
        BigWorld.setActiveMonitorIndex(monitorIdx, BigWorld.WindowModeWindowed)
        BigWorld.setActiveMonitorIndex(monitorIdx, BigWorld.WindowModeBorderless)
        BigWorld.setActiveMonitorIndex(monitorIdx, BigWorld.WindowModeExclusiveFullscreen)

    def setWindowed(self):
        if self.windowMode != BigWorld.WindowModeWindowed:
            BigWorld.changeVideoMode(-1, BigWorld.WindowModeWindowed)

    def setBorderless(self):
        if self.windowMode != BigWorld.WindowModeBorderless:
            BigWorld.changeVideoMode(-1, BigWorld.WindowModeBorderless)

    def changeWindowSize(self, width, height):
        if not self.isMonitorChanged and self.windowMode != BigWorld.WindowModeWindowed:
            self.setWindowed()
        curWindowSize = self.currentWindowSize
        if curWindowSize.width != width or curWindowSize.height != height:
            BigWorld.resizeWindow(width, height)

    def changeBorderlessSize(self, width, height):
        curBorderlessSize = self.currentBorderlessSize
        if curBorderlessSize.width != width or curBorderlessSize.height != height:
            BigWorld.setBorderlessFixedSize(width, height)
        BigWorld.changeVideoMode(-1, BigWorld.WindowModeBorderless)

    def setGlyphCache(self, scale = 1):
        textureSize = 1024 * math.ceil(scale)
        raise hasattr(GUI, 'wg_setGlyphCacheParams') or AssertionError('GUI.wg_setGlyphCacheParams() is not defined')
        GUI.wg_setGlyphCacheParams(1, textureSize, textureSize)

    @property
    def activeMonitor(self):
        return BigWorld.getActiveMonitorIndex(BigWorld.getWindowMode())

    @property
    def currentMonitor(self):
        return self.__currentMonitorIdx

    @property
    def isMonitorChanged(self):
        return self.__monitorChanged

    @property
    def windowMode(self):
        return BigWorld.getWindowMode()

    @property
    def noRestartExclusiveFullscreenMonitorIndex(self):
        return BigWorld.getExclusiveFullscreenMonitorIndex()

    def maxParams(self):
        maxWdth = 640
        maxHght = 480
        vmodes = getSuitableVideoModes()
        for monitorModes in vmodes:
            for mode in monitorModes:
                maxWdth = max(maxWdth, mode.width)
                maxHght = max(maxHght, mode.height)

        return (maxWdth, maxHght)

    def isFullscreen(self):
        return BigWorld.getWindowMode() == BigWorld.WindowModeExclusiveFullscreen

    def isWindowed(self):
        return BigWorld.getWindowMode() == BigWorld.WindowModeWindowed

    def isBorderless(self):
        return BigWorld.getWindowMode() == BigWorld.WindowModeBorderless


g_monitorSettings = MonitorSettings()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\utils\graphics.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:23 St�edn� Evropa (letn� �as)
