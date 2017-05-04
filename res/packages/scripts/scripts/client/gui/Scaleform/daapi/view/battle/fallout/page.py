# 2017.05.04 15:22:29 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/fallout/page.py
from constants import ATTACK_REASON_INDICES
from gui.Scaleform.daapi.view.battle.fallout import markers2d
from gui.Scaleform.daapi.view.battle.shared import crosshair
from gui.Scaleform.daapi.view.meta.FalloutBattlePageMeta import FalloutBattlePageMeta
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES
from gui.Scaleform.locale.FALLOUT import FALLOUT
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from helpers import i18n
from messenger.gui import events_dispatcher as msg_events_dispatcher
_COMPONENTS_HIDE_DONT_REVEAL = {BATTLE_VIEW_ALIASES.RADIAL_MENU}
_COMPONENTS_HIDE_WHEN_RESPAWN = {BATTLE_VIEW_ALIASES.FALLOUT_CONSUMABLES_PANEL, BATTLE_VIEW_ALIASES.DAMAGE_PANEL}
_COMPONENTS_SHOW_WHEN_RESPAWN = {BATTLE_VIEW_ALIASES.FALLOUT_RESPAWN_VIEW}
_PERMANENT_COMPONENTS = {BATTLE_VIEW_ALIASES.DEBUG_PANEL, BATTLE_VIEW_ALIASES.FALLOUT_SCORE_PANEL, BATTLE_VIEW_ALIASES.BATTLE_TIMER}
_FALLOUT_COMPONENTS_TO_CTRLS = ((BATTLE_CTRL_ID.ARENA_PERIOD, (BATTLE_VIEW_ALIASES.BATTLE_TIMER, BATTLE_VIEW_ALIASES.PREBATTLE_TIMER)),
 (BATTLE_CTRL_ID.DEBUG, (BATTLE_VIEW_ALIASES.DEBUG_PANEL,)),
 (BATTLE_CTRL_ID.RESPAWN, (BATTLE_VIEW_ALIASES.FALLOUT_RESPAWN_VIEW,)),
 (BATTLE_CTRL_ID.FLAG_NOTS, (BATTLE_VIEW_ALIASES.FLAG_NOTIFICATION,)))
_VEHICLE_STATE_HANDLERS = {VEHICLE_VIEW_STATE.DESTROYED: '_updateDestroyed',
 VEHICLE_VIEW_STATE.SWITCHING: '_switching'}
_FALLOUT_EXTERNAL_COMPONENTS = (crosshair.CrosshairPanelContainer, markers2d.FalloutMarkersManager)

class FalloutBasePage(FalloutBattlePageMeta):

    def __init__(self, components = _FALLOUT_COMPONENTS_TO_CTRLS, external = _FALLOUT_EXTERNAL_COMPONENTS, fullStatsAlias = ''):
        super(FalloutBasePage, self).__init__(components=components, external=external, fullStatsAlias=fullStatsAlias)
        self.__isInRespawn = False
        self.__hasGasAttack = None
        return

    def _startBattleSession(self):
        super(FalloutBasePage, self)._startBattleSession()
        ctrl = self.sessionProvider.dynamic.respawn
        if ctrl is not None:
            ctrl.onRespawnVisibilityChanged += self.__onRespawnVisibility
        self.__hasGasAttack = self.sessionProvider.arenaVisitor.hasGasAttack()
        ctrl = self.sessionProvider.shared.vehicleState
        if ctrl is not None and self.__hasGasAttack:
            ctrl.onVehicleStateUpdated += self.__onVehicleStateUpdated
        self.__isGasAttackStarted = False
        ctrl = self.sessionProvider.dynamic.gasAttack
        if ctrl is not None and self.__hasGasAttack:
            ctrl.onPreparing += self.__onGasAttack
            ctrl.onStarted += self.__onGasAttack
        return

    def _stopBattleSession(self):
        ctrl = self.sessionProvider.dynamic.respawn
        if ctrl is not None:
            ctrl.onRespawnVisibilityChanged -= self.__onRespawnVisibility
        ctrl = self.sessionProvider.shared.vehicleState
        if ctrl is not None and self.__hasGasAttack:
            ctrl.onVehicleStateUpdated -= self.__onVehicleStateUpdated
        ctrl = self.sessionProvider.dynamic.gasAttack
        if ctrl is not None and self.__hasGasAttack:
            ctrl.onPreparing -= self.__onGasAttack
            ctrl.onStarted -= self.__onGasAttack
        super(FalloutBasePage, self)._stopBattleSession()
        return

    def _updateDestroyed(self, deathReasonID = None):
        if self.__isGasAttackStarted and deathReasonID is not None:
            if deathReasonID == ATTACK_REASON_INDICES['gas_attack']:
                self.as_setPostmortemGasAtackInfoS(i18n.makeString(FALLOUT.GASATTACK_POSTMORTEM_VEHICLEDESTROYED), i18n.makeString(FALLOUT.GASATTACK_POSTMORTEM_RESPAWNINFO), True)
            else:
                self.as_setPostmortemGasAtackInfoS(i18n.makeString(FALLOUT.GASATTACK_POSTMORTEM_VEHICLEDESTROYED), i18n.makeString(FALLOUT.GASATTACK_POSTMORTEM_RESPAWNINFO), False)
        return

    def _switchToPostmortem(self):
        alias = BATTLE_VIEW_ALIASES.FALLOUT_CONSUMABLES_PANEL
        if self.as_isComponentVisibleS(alias):
            self._setComponentsVisibility(hidden={alias})
        if self.as_isComponentVisibleS(BATTLE_VIEW_ALIASES.RADIAL_MENU):
            self._toggleRadialMenu(False)

    def _switching(self, _):
        self.as_hidePostmortemGasAtackInfoS()

    def _handleToggleFullStats(self, event):
        isDown = event.ctx['isDown']
        self._toggleFullStats(isDown, permanent=_PERMANENT_COMPONENTS)
        if not isDown and self.__isInRespawn:
            self.__onRespawnVisibility(True)

    def __onRespawnVisibility(self, isVisible):
        self.__isInRespawn = isVisible
        if isVisible:
            if not self.as_isComponentVisibleS(self._fullStatsAlias):
                self.app.enterGuiControlMode(BATTLE_VIEW_ALIASES.FALLOUT_RESPAWN_VIEW)
                msg_events_dispatcher.setMessageFadingEnabled(False)
                self._setComponentsVisibility(_COMPONENTS_SHOW_WHEN_RESPAWN, _COMPONENTS_HIDE_DONT_REVEAL.union(_COMPONENTS_HIDE_WHEN_RESPAWN))
        else:
            self.app.leaveGuiControlMode(BATTLE_VIEW_ALIASES.FALLOUT_RESPAWN_VIEW)
            msg_events_dispatcher.setMessageFadingEnabled(True)
            if not self.as_isComponentVisibleS(self._fullStatsAlias):
                self._setComponentsVisibility(_COMPONENTS_HIDE_WHEN_RESPAWN, _COMPONENTS_SHOW_WHEN_RESPAWN)
            else:
                self._toggling.update(_COMPONENTS_HIDE_WHEN_RESPAWN)
                self._toggling.difference_update(_COMPONENTS_SHOW_WHEN_RESPAWN)

    def __onVehicleStateUpdated(self, state, value):
        if not self.__hasGasAttack:
            raise AssertionError('onVehicleStateUpdated received, but there is no Gas Attack!')
            return state not in _VEHICLE_STATE_HANDLERS and None
        else:
            handler = getattr(self, _VEHICLE_STATE_HANDLERS[state], None)
            if handler is not None and callable(handler):
                if value is not None:
                    handler(value)
                else:
                    handler()
            return

    def __onGasAttack(self, _):
        self.__isGasAttackStarted = True


class FalloutClassicPage(FalloutBasePage):

    def __init__(self):
        super(FalloutClassicPage, self).__init__(fullStatsAlias=BATTLE_VIEW_ALIASES.FALLOUT_CLASSIC_STATS)


class FalloutMultiteamPage(FalloutBasePage):

    def __init__(self):
        super(FalloutMultiteamPage, self).__init__(fullStatsAlias=BATTLE_VIEW_ALIASES.FALLOUT_MULTITEAM_STATS)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\battle\fallout\page.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:29 St�edn� Evropa (letn� �as)
