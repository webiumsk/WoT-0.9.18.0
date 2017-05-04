# 2017.05.04 15:24:17 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleEndWarningPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleEndWarningPanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_setTotalTimeS(self, minutes, seconds):
        if self._isDAAPIInited():
            return self.flashObject.as_setTotalTime(minutes, seconds)

    def as_setTextInfoS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setTextInfo(text)

    def as_setStateS(self, isShow):
        if self._isDAAPIInited():
            return self.flashObject.as_setState(isShow)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BattleEndWarningPanelMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:17 Støední Evropa (letní èas)
