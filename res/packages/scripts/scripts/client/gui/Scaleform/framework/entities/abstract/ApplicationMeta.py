# 2017.05.04 15:24:46 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/ApplicationMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class ApplicationMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    """

    def setLoaderMgr(self, mgr):
        """
        :param mgr: Represented by ILoaderManagerMeta (AS)
        """
        self._printOverrideError('setLoaderMgr')

    def setGlobalVarsMgr(self, mgr):
        """
        :param mgr: Represented by IGlobalVarsMgrMeta (AS)
        """
        self._printOverrideError('setGlobalVarsMgr')

    def setSoundMgr(self, mgr):
        """
        :param mgr: Represented by ISoundManager (AS)
        """
        self._printOverrideError('setSoundMgr')

    def setContainerMgr(self, mgr):
        """
        :param mgr: Represented by IContainerManager (AS)
        """
        self._printOverrideError('setContainerMgr')

    def setContextMenuMgr(self, mgr):
        """
        :param mgr: Represented by IContextMenuManager (AS)
        """
        self._printOverrideError('setContextMenuMgr')

    def setPopoverMgr(self, mgr):
        """
        :param mgr: Represented by IPopoverManager (AS)
        """
        self._printOverrideError('setPopoverMgr')

    def setColorSchemeMgr(self, mgr):
        """
        :param mgr: Represented by IColorSchemeManager (AS)
        """
        self._printOverrideError('setColorSchemeMgr')

    def setEventLogMgr(self, mgr):
        """
        :param mgr: Represented by IEventLogManager (AS)
        """
        self._printOverrideError('setEventLogMgr')

    def setTooltipMgr(self, mgr):
        """
        :param mgr: Represented by ITooltipMgr (AS)
        """
        self._printOverrideError('setTooltipMgr')

    def setVoiceChatMgr(self, mgr):
        """
        :param mgr: Represented by IVoiceChatManager (AS)
        """
        self._printOverrideError('setVoiceChatMgr')

    def setUtilsMgr(self, mgr):
        """
        :param mgr: Represented by IUtilsManagerMeta (AS)
        """
        self._printOverrideError('setUtilsMgr')

    def setTweenMgr(self, mgr):
        """
        :param mgr: Represented by ITweenManager (AS)
        """
        self._printOverrideError('setTweenMgr')

    def setGameInputMgr(self, mgr):
        """
        :param mgr: Represented by IGameInputManagerMeta (AS)
        """
        self._printOverrideError('setGameInputMgr')

    def setCacheMgr(self, mgr):
        """
        :param mgr: Represented by ICacheManagerMeta (AS)
        """
        self._printOverrideError('setCacheMgr')

    def setTextMgr(self, mgr):
        """
        :param mgr: Represented by ITextManager (AS)
        """
        self._printOverrideError('setTextMgr')

    def setTutorialMgr(self, mgr):
        """
        :param mgr: Represented by ITutorialManager (AS)
        """
        self._printOverrideError('setTutorialMgr')

    def setImageManager(self, mgr):
        """
        :param mgr: Represented by IImageManager (AS)
        """
        self._printOverrideError('setImageManager')

    def handleGlobalKeyEvent(self, command):
        self._printOverrideError('handleGlobalKeyEvent')

    def onAsInitializationCompleted(self):
        self._printOverrideError('onAsInitializationCompleted')

    def as_isDAAPIInitedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_isDAAPIInited()

    def as_populateS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_populate()

    def as_disposeS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_dispose()

    def as_registerManagersS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_registerManagers()

    def as_setLibrariesListS(self, list):
        """
        :param list: Represented by Vector.<String> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setLibrariesList(list)

    def as_updateStageS(self, w, h, scale):
        if self._isDAAPIInited():
            return self.flashObject.as_updateStage(w, h, scale)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\entities\abstract\ApplicationMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:46 St�edn� Evropa (letn� �as)
