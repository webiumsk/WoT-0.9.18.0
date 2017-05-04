# 2017.05.04 15:24:46 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/GameInputManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class GameInputManagerMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    """

    def handleGlobalKeyEvent(self, keyCode, eventType):
        self._printOverrideError('handleGlobalKeyEvent')

    def as_addKeyHandlerS(self, keyCode, eventType, ignoreText, cancelEventType):
        if self._isDAAPIInited():
            return self.flashObject.as_addKeyHandler(keyCode, eventType, ignoreText, cancelEventType)

    def as_clearKeyHandlerS(self, keyCode, eventType):
        if self._isDAAPIInited():
            return self.flashObject.as_clearKeyHandler(keyCode, eventType)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\entities\abstract\GameInputManagerMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:46 Støední Evropa (letní èas)
