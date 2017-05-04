# 2017.05.04 15:22:27 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/fallout/consumables_panel.py
import rage
from gui.Scaleform.daapi.view.meta.FalloutConsumablesPanelMeta import FalloutConsumablesPanelMeta
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class FalloutConsumablesPanel(FalloutConsumablesPanelMeta):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(FalloutConsumablesPanel, self).__init__()
        self.__hasRage = False
        self.__currentValue = 0

    def _populate(self):
        super(FalloutConsumablesPanel, self)._populate()
        self.__hasRage = self.sessionProvider.arenaVisitor.hasRage()
        if self.__hasRage:
            self._startRage()

    def _dispose(self):
        if self.__hasRage:
            self._stopRage()
        super(FalloutConsumablesPanel, self)._dispose()

    def _startRage(self):
        vehicleCtrl = self.sessionProvider.shared.vehicleState
        if vehicleCtrl is not None:
            vehicleCtrl.onRespawnBaseMoving += self.__onRespawnBaseMoving
        avatarStatsCtrl = self.sessionProvider.shared.privateStats
        if avatarStatsCtrl is not None:
            avatarStatsCtrl.onUpdated += self.__onAvatarStatsUpdated
            self.__currentValue = avatarStatsCtrl.getStats().get('ragePoints', 0)
            barProps = {'maxValue': rage.g_cache.pointsLimit,
             'curValue': self.__currentValue}
            self.as_initializeRageProgressS(True, barProps)
        return

    def _stopRage(self):
        avatarStatsCtrl = self.sessionProvider.shared.privateStats
        if avatarStatsCtrl is not None:
            avatarStatsCtrl.onUpdated -= self.__onAvatarStatsUpdated
        vehicleCtrl = self.sessionProvider.shared.vehicleState
        if vehicleCtrl is not None:
            vehicleCtrl.onRespawnBaseMoving -= self.__onRespawnBaseMoving
        return

    def __onRespawnBaseMoving(self):
        raise self.__hasRage or AssertionError('Unexpected event')
        self.as_updateProgressBarValueS(self.__currentValue)

    def __onAvatarStatsUpdated(self, stats):
        if not self.__hasRage:
            raise AssertionError('Unexpected event')
            newValue = stats.get('ragePoints', 0)
            if newValue == self.__currentValue:
                return
            delta = newValue - self.__currentValue
            delta < 0 and self.as_updateProgressBarValueS(newValue)
        else:
            self.as_updateProgressBarValueByDeltaS(delta)
        self.__currentValue = newValue
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\battle\fallout\consumables_panel.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:27 St�edn� Evropa (letn� �as)
