# 2017.05.04 15:24:17 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleDamageLogPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleDamageLogPanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_setSettingsDamageLogComponentS(self, isVisible, isColorBlind):
        if self._isDAAPIInited():
            return self.flashObject.as_setSettingsDamageLogComponent(isVisible, isColorBlind)

    def as_summaryStatsS(self, damage, blocked, assist, stun):
        if self._isDAAPIInited():
            return self.flashObject.as_summaryStats(damage, blocked, assist, stun)

    def as_updateSummaryDamageValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSummaryDamageValue(value)

    def as_updateSummaryBlockedValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSummaryBlockedValue(value)

    def as_updateSummaryAssistValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSummaryAssistValue(value)

    def as_updateSummaryStunValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSummaryStunValue(value)

    def as_detailStatsTopS(self, isVisible, isShortMode, messages):
        """
        :param messages: Represented by Vector.<MessageRenderModel> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_detailStatsTop(isVisible, isShortMode, messages)

    def as_addDetailMessageTopS(self, value, actionTypeImg, vehicleTypeImg, vehicleName, shellTypeStr, shellTypeBG):
        if self._isDAAPIInited():
            return self.flashObject.as_addDetailMessageTop(value, actionTypeImg, vehicleTypeImg, vehicleName, shellTypeStr, shellTypeBG)

    def as_detailStatsBottomS(self, isVisible, isShortMode, messages):
        """
        :param messages: Represented by Vector.<MessageRenderModel> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_detailStatsBottom(isVisible, isShortMode, messages)

    def as_addDetailMessageBottomS(self, value, actionTypeImg, vehicleTypeImg, vehicleName, shellTypeStr, shellTypeBG):
        if self._isDAAPIInited():
            return self.flashObject.as_addDetailMessageBottom(value, actionTypeImg, vehicleTypeImg, vehicleName, shellTypeStr, shellTypeBG)

    def as_isDownCtrlButtonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_isDownCtrlButton(value)

    def as_isDownAltButtonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_isDownAltButton(value)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BattleDamageLogPanelMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:17 St�edn� Evropa (letn� �as)
