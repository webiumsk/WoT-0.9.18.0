# 2017.05.04 15:22:32 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/damage_log_panel.py
import BigWorld
from gui.LobbyContext import g_lobbyContext
from helpers import dependency
from collections import defaultdict
from shared_utils import BitmaskHelper
from constants import SHELL_TYPES
from account_helpers.settings_core.options import DamageLogDetailsSetting as _VIEW_MODE, DamageLogEventPositionsSetting as _EVENT_POSITIONS, DamageLogEventTypesSetting as _DISPLAYED_EVENT_TYPES
from account_helpers.settings_core.settings_constants import DAMAGE_LOG, GRAPHICS
from gui.shared import events, EVENT_BUS_SCOPE
from gui.shared.gui_items.Vehicle import VEHICLE_CLASS_NAME
from gui.Scaleform.daapi.view.meta.BattleDamageLogPanelMeta import BattleDamageLogPanelMeta
from gui.battle_control.battle_constants import PERSONAL_EFFICIENCY_TYPE as _ETYPE
from BattleFeedbackCommon import BATTLE_EVENT_TYPE as _BET
from gui.Scaleform.genConsts.BATTLEDAMAGELOG_IMAGES import BATTLEDAMAGELOG_IMAGES as _IMAGES
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider
from helpers import i18n
from gui.Scaleform.locale.INGAME_GUI import INGAME_GUI
from gui.Scaleform.genConsts.DAMAGE_LOG_SHELL_BG_TYPES import DAMAGE_LOG_SHELL_BG_TYPES
_POSITIVE_EVENTS_MASK = _ETYPE.DAMAGE | _ETYPE.ASSIST_DAMAGE | _ETYPE.STUN
_NEGATIVE_EVENTS_MASK = _ETYPE.BLOCKED_DAMAGE | _ETYPE.RECEIVED_DAMAGE | _ETYPE.RECEIVED_CRITICAL_HITS
_ALL_EVENTS_MASK = _POSITIVE_EVENTS_MASK | _NEGATIVE_EVENTS_MASK
_EVENT_POSITIONS_TO_CONTENT_MASK = {_EVENT_POSITIONS.ALL_BOTTOM: (0, _ALL_EVENTS_MASK),
 _EVENT_POSITIONS.NEGATIVE_AT_TOP: (_NEGATIVE_EVENTS_MASK, _POSITIVE_EVENTS_MASK)}

class _RECORD_STYLE(object):
    """
    Enum of log record styles.
    """
    FULL = 0
    SHORT = 1


_EVENT_POSITIONS_TO_RECORD_STYLE = {_EVENT_POSITIONS.ALL_BOTTOM: (_RECORD_STYLE.FULL, _RECORD_STYLE.FULL),
 _EVENT_POSITIONS.NEGATIVE_AT_TOP: (_RECORD_STYLE.FULL, _RECORD_STYLE.SHORT)}
_DISPLAYED_EVENT_TYPES_TO_CONTENT_MASK = {_DISPLAYED_EVENT_TYPES.ALL: _ALL_EVENTS_MASK,
 _DISPLAYED_EVENT_TYPES.ONLY_NEGATIVE: _NEGATIVE_EVENTS_MASK,
 _DISPLAYED_EVENT_TYPES.ONLY_POSITIVE: _POSITIVE_EVENTS_MASK}
_TOTAL_DAMAGE_SETTINGS_TO_CONTENT_MASK = {DAMAGE_LOG.TOTAL_DAMAGE: _ETYPE.DAMAGE,
 DAMAGE_LOG.ASSIST_DAMAGE: _ETYPE.ASSIST_DAMAGE,
 DAMAGE_LOG.BLOCKED_DAMAGE: _ETYPE.BLOCKED_DAMAGE,
 DAMAGE_LOG.ASSIST_STUN: _ETYPE.STUN}
_LOGS_SETTINGS = (DAMAGE_LOG.SHOW_DETAILS, DAMAGE_LOG.EVENT_POSITIONS, DAMAGE_LOG.SHOW_EVENT_TYPES)
_VEHICLE_CLASS_TAGS_ICONS = {'lightTank': _IMAGES.WHITE_ICON_LIGHTTANK_16X16,
 'mediumTank': _IMAGES.WHITE_ICON_MEDIUM_TANK_16X16,
 'heavyTank': _IMAGES.WHITE_ICON_HEAVYTANK_16X16,
 'SPG': _IMAGES.WHITE_ICON_SPG_16X16,
 'AT-SPG': _IMAGES.WHITE_ICON_AT_SPG_16X16}
_SHELL_TYPES_TO_STR = {SHELL_TYPES.ARMOR_PIERCING: INGAME_GUI.DAMAGELOG_SHELLTYPE_ARMOR_PIERCING,
 SHELL_TYPES.HIGH_EXPLOSIVE: INGAME_GUI.DAMAGELOG_SHELLTYPE_HIGH_EXPLOSIVE,
 SHELL_TYPES.ARMOR_PIERCING_HE: INGAME_GUI.DAMAGELOG_SHELLTYPE_ARMOR_PIERCING_HE,
 SHELL_TYPES.ARMOR_PIERCING_CR: INGAME_GUI.DAMAGELOG_SHELLTYPE_ARMOR_PIERCING_CR,
 SHELL_TYPES.HOLLOW_CHARGE: INGAME_GUI.DAMAGELOG_SHELLTYPE_HOLLOW_CHARGE}

def _formatTotalValue(value):
    return BigWorld.wg_getIntegralFormat(value)


class _IVOBuilder(object):
    """
    Declares interface of a VO builder.
    """

    def buildVO(self, info, arenaDP):
        """
        Builds VO by using the given data (event) and the arena data provider.
        
        :param info: data to be used for VO construction
        :param arenaDP: battle-specific data provider, see ArenaDataProvider class.
        :return: Derived classes should return VO object, represented by dict.
        """
        raise NotImplementedError


class _LogRecordVOBuilder(_IVOBuilder):
    """
    Composer that is populated with several VO builders and is used for building composite VO
    object. The class to be used for describing content of a log record.
    """

    def __init__(self, *builders):
        """
        Constructor.
        :param builders: list of objects extending _IVOBuilder interface.
        """
        super(_LogRecordVOBuilder, self).__init__()
        self.__builders = builders

    def buildVO(self, info, arenaDP):
        vo = {}
        for b in self.__builders:
            vo.update(b.buildVO(info, arenaDP))

        return vo


class _VehicleVOBuilder(_IVOBuilder):
    """
    Builder of vehicle specific VO.
    """

    def buildVO(self, info, arenaDP):
        if arenaDP is not None:
            vTypeInfoVO = arenaDP.getVehicleInfo(info.getArenaVehicleID()).vehicleType
            vehicleTypeImg = _VEHICLE_CLASS_TAGS_ICONS.get(vTypeInfoVO.classTag, '')
            vehicleName = vTypeInfoVO.shortNameWithPrefix
        else:
            vehicleTypeImg = ''
            vehicleName = ''
        return {'vehicleTypeImg': vehicleTypeImg,
         'vehicleName': vehicleName}


class _ShellVOBuilder(_IVOBuilder):
    """
    Builder of shell specific VO.
    """

    def buildVO(self, info, arenaDP):
        return {'shellTypeStr': self._getShellTypeStr(info),
         'shellTypeBG': self._getShellTypeBg(info)}

    def _getShellTypeStr(self, info):
        shType = info.getShellType()
        if shType is not None and shType in _SHELL_TYPES_TO_STR:
            return _SHELL_TYPES_TO_STR[shType]
        else:
            return ''

    def _getShellTypeBg(self, info):
        if info.getShellType() is None:
            return DAMAGE_LOG_SHELL_BG_TYPES.EMPTY
        elif info.isShellGold():
            return DAMAGE_LOG_SHELL_BG_TYPES.GOLD
        else:
            return DAMAGE_LOG_SHELL_BG_TYPES.WHITE


class _EmptyShellVOBuilder(_ShellVOBuilder):
    """
    Builder of empty shell VO (for some kind of events VO should not include shell description).
    """

    def _getShellTypeStr(self, info):
        return ''

    def _getShellTypeBg(self, info):
        return DAMAGE_LOG_SHELL_BG_TYPES.EMPTY


class _DamageShellVOBuilder(_ShellVOBuilder):
    """
    Builder of shell specific VO for events related to damage.
    """

    def buildVO(self, info, arenaDP):
        if info.isShot():
            shellVOBuilder = _ShellVOBuilder()
        else:
            shellVOBuilder = _EmptyShellVOBuilder()
        return shellVOBuilder.buildVO(info, arenaDP)


class _CritsShellVOBuilder(_ShellVOBuilder):
    """
    Builder of shell specific VO for events related to damage.
    """

    def buildVO(self, info, arenaDP):
        if info.isShot():
            shellVOBuilder = _ShellVOBuilder()
        else:
            shellVOBuilder = _EmptyShellVOBuilder()
        return shellVOBuilder.buildVO(info, arenaDP)


class _ValueVOBuilder(_IVOBuilder):
    """
    Base builder of value specific VO.
    """

    def buildVO(self, info, arenaDP):
        return {'value': self._getValue(info)}

    def _getValue(self, info):
        return 0


class _CriticalHitValueVOBuilder(_ValueVOBuilder):
    """
    Crits count value builder.
    """

    def _getValue(self, info):
        return i18n.makeString(INGAME_GUI.DAMAGELOG_MULTIPLIER, multiplier=str(info.getCritsCount()))


class _DamageValueVOBuilder(_ValueVOBuilder):
    """
    Damage value builder.
    """

    def _getValue(self, info):
        return BigWorld.wg_getIntegralFormat(info.getDamage())


class _ActionImgVOBuilder(_IVOBuilder):
    """
    Builder of action (event) description VO.
    """

    def __init__(self, image):
        super(_ActionImgVOBuilder, self).__init__()
        self._image = image

    def buildVO(self, info, arenaDP):
        return {'actionTypeImg': self._getImage(info)}

    def _getImage(self, info):
        return self._image


class _DamageActionImgVOBuilder(_ActionImgVOBuilder):
    """
    Builder of damage action (damage related events) description VO.
    """

    def __init__(self, shotIcon, fireIcon, ramIcon, wcIcon):
        super(_DamageActionImgVOBuilder, self).__init__('')
        self._shotIcon = shotIcon
        self._fireIcon = fireIcon
        self._ramIcon = ramIcon
        self._wcIcon = wcIcon

    def _getImage(self, info):
        if info.isShot():
            return self._shotIcon
        if info.isFire():
            return self._fireIcon
        if info.isWorldCollision():
            return self._wcIcon
        return self._ramIcon


class _AssistActionImgVOBuilder(_ActionImgVOBuilder):
    """
    Builder of assist action (crits related events) description VO.
    """

    def __init__(self):
        super(_AssistActionImgVOBuilder, self).__init__('')

    def _getImage(self, info):
        if info.getBattleEventType() == _BET.TRACK_ASSIST:
            return _IMAGES.DAMAGELOG_IMMOBILIZED_16X16
        if info.getBattleEventType() == _BET.RADIO_ASSIST:
            return _IMAGES.DAMAGELOG_COORDINATE_16X16
        return super(_AssistActionImgVOBuilder, self)._getImage(info)


_DEFAULT_VEHICLE_VO_BUILDER = _VehicleVOBuilder()
_EMPTY_SHELL_VO_BUILDER = _EmptyShellVOBuilder()
_DAMAGE_VALUE_VO_BUILDER = _DamageValueVOBuilder()
_ETYPE_TO_RECORD_VO_BUILDER = {_ETYPE.DAMAGE: _LogRecordVOBuilder(_DEFAULT_VEHICLE_VO_BUILDER, _EMPTY_SHELL_VO_BUILDER, _DAMAGE_VALUE_VO_BUILDER, _DamageActionImgVOBuilder(shotIcon=_IMAGES.DAMAGELOG_DAMAGE_16X16, fireIcon=_IMAGES.DAMAGELOG_FIRE_16X16, ramIcon=_IMAGES.DAMAGELOG_RAM_16X16, wcIcon=_IMAGES.DAMAGELOG_ICON_WORLD_COLLISION)),
 _ETYPE.RECEIVED_DAMAGE: _LogRecordVOBuilder(_DEFAULT_VEHICLE_VO_BUILDER, _DamageShellVOBuilder(), _DAMAGE_VALUE_VO_BUILDER, _DamageActionImgVOBuilder(shotIcon=_IMAGES.DAMAGELOG_DAMAGE_ENEMY_16X16, fireIcon=_IMAGES.DAMAGELOG_BURN_ENEMY_16X16, ramIcon=_IMAGES.DAMAGELOG_RAM_ENEMY_16X16, wcIcon=_IMAGES.DAMAGELOG_DAMAGE_ENEMY_16X16)),
 _ETYPE.BLOCKED_DAMAGE: _LogRecordVOBuilder(_DEFAULT_VEHICLE_VO_BUILDER, _ShellVOBuilder(), _DAMAGE_VALUE_VO_BUILDER, _ActionImgVOBuilder(image=_IMAGES.DAMAGELOG_REFLECT_16X16)),
 _ETYPE.ASSIST_DAMAGE: _LogRecordVOBuilder(_DEFAULT_VEHICLE_VO_BUILDER, _EMPTY_SHELL_VO_BUILDER, _DAMAGE_VALUE_VO_BUILDER, _AssistActionImgVOBuilder()),
 _ETYPE.RECEIVED_CRITICAL_HITS: _LogRecordVOBuilder(_DEFAULT_VEHICLE_VO_BUILDER, _CritsShellVOBuilder(), _CriticalHitValueVOBuilder(), _ActionImgVOBuilder(image=_IMAGES.DAMAGELOG_CRITICAL_ENEMY_16X16)),
 _ETYPE.STUN: _LogRecordVOBuilder(_DEFAULT_VEHICLE_VO_BUILDER, _EMPTY_SHELL_VO_BUILDER, _DAMAGE_VALUE_VO_BUILDER, _ActionImgVOBuilder(image=_IMAGES.DAMAGELOG_STUN_16X16))}

class _LogViewComponent(object):
    """
    The class represents log component of the damage log panel (see DamageLogPanel description).
    """

    def __init__(self):
        super(_LogViewComponent, self).__init__()
        self.__setListProxy = None
        self.__addToListProxy = None
        self.__efficiencyCtrl = None
        self.__arenaDP = None
        self.__logViewMode = _VIEW_MODE.SHOW_ALWAYS
        self.__isVisible = True
        self.__contentMask = 0
        self.__recordStyle = _RECORD_STYLE.FULL
        return

    def initialize(self, setListProxyMethod, addToListProxyMethod, efficiencyCtrl, arenaDP):
        self.__setListProxy = setListProxyMethod
        self.__addToListProxy = addToListProxyMethod
        self.__efficiencyCtrl = efficiencyCtrl
        self.__arenaDP = arenaDP

    def dispose(self):
        self.__setListProxy = None
        self.__addToListProxy = None
        self.__efficiencyCtrl = None
        self.__arenaDP = None
        return

    def clear(self):
        self.__setListProxy(self.__isVisible, bool(self.__recordStyle == _RECORD_STYLE.SHORT), [])

    def invalidate(self):
        if self.__logViewMode == _VIEW_MODE.SHOW_ALWAYS:
            self.__isVisible = True
            messages = self._getLogMessages(self.__contentMask)
        elif self.__logViewMode == _VIEW_MODE.SHOW_BY_ALT_PRESS:
            self.__isVisible = False
            messages = self._getLogMessages(self.__contentMask)
        else:
            self.__isVisible = False
            messages = []
        self.__setListProxy(self.__isVisible, bool(self.__recordStyle == _RECORD_STYLE.SHORT), messages)

    def updateLog(self, contentMask = None, viewMode = None, recordStyle = _RECORD_STYLE.FULL):
        needUpdate = False
        if viewMode != self.__logViewMode:
            self.__logViewMode = viewMode
            needUpdate = True
        if contentMask != self.__contentMask:
            self.__contentMask = contentMask
            needUpdate = True
        if recordStyle != self.__recordStyle:
            self.__recordStyle = recordStyle
            needUpdate = True
        if needUpdate:
            self.invalidate()

    def addToLog(self, events):
        if self.__logViewMode == _VIEW_MODE.HIDE:
            return
        for e in events:
            if BitmaskHelper.hasAnyBitSet(self.__contentMask, e.getType()):
                vo = self._buildLogMessageVO(e)
                self.__addToListProxy(**vo)

    def _getLogMessages(self, contentMask):
        if self.__efficiencyCtrl is not None:
            records = self.__efficiencyCtrl.getLoogedEfficiency(contentMask)
            return [ self._buildLogMessageVO(r) for r in records ]
        else:
            return []

    def _buildLogMessageVO(self, info):
        builder = _ETYPE_TO_RECORD_VO_BUILDER[info.getType()]
        return builder.buildVO(info, self.__arenaDP)


class DamageLogPanel(BattleDamageLogPanelMeta):
    """
    Damage log panel represents UI component displaying damage related events. It consists of
    3 components:
    - total damage component: displays aggregated values by caused and assist damage and blocked
    damage (also see _TOTAL_DAMAGE_SETTINGS_TO_CONTENT_MASK mapping)
    - top and bottom log panels: display log of events, content of each panel depends on
      _EVENT_POSITIONS and _DISPLAYED_EVENT_TYPES settings (see _EVENT_POSITIONS_TO_CONTENT_MASK
      and _DISPLAYED_EVENT_TYPES_TO_CONTENT_MASK mappings).
    Each log panel is represented by _LogViewComponent class, that encapsulates logic related
    to log's view. DamageLogPanel listens efficiency events and settings changes and notifies log
    components about it in order to update logs' content.
    Content of log panel is described by a bit mask (see PERSONAL_EFFICIENCY_TYPE).
    """
    sessionProvider = dependency.descriptor(IBattleSessionProvider)
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self):
        super(DamageLogPanel, self).__init__()
        self.__efficiencyCtrl = None
        self.__arenaDP = self.sessionProvider.getCtx().getArenaDP()
        self.__vehStateCtrl = self.sessionProvider.shared.vehicleState
        self.__isVisible = False
        self.__logViewMode = _VIEW_MODE.SHOW_ALWAYS
        self.__isSPG = None
        self.__totalDamageContentMask = 0
        self.__totalValues = defaultdict(int)
        self._totalEvents = None
        self.__topLog = _LogViewComponent()
        self.__bottomLog = _LogViewComponent()
        return

    def _populate(self):
        super(DamageLogPanel, self)._populate()
        self.__efficiencyCtrl = self.sessionProvider.shared.personalEfficiencyCtrl
        self.__topLog.initialize(setListProxyMethod=self._updateTopLog, addToListProxyMethod=self._addToTopLog, efficiencyCtrl=self.__efficiencyCtrl, arenaDP=self.__arenaDP)
        self.__bottomLog.initialize(setListProxyMethod=self._updateBottomLog, addToListProxyMethod=self._addToBottomLog, efficiencyCtrl=self.__efficiencyCtrl, arenaDP=self.__arenaDP)
        self._totalEvents = ((_ETYPE.DAMAGE, self._updateTotalDamageValue),
         (_ETYPE.BLOCKED_DAMAGE, self._updateTotalBlockedDamageValue),
         (_ETYPE.ASSIST_DAMAGE, self._updateTotalAssistValue),
         (_ETYPE.STUN, self._updateTotalStunValue))
        self._invalidatePanelVisibility()
        if self.__efficiencyCtrl is not None:
            self._invalidateContent()
            self.__efficiencyCtrl.onTotalEfficiencyUpdated += self._onTotalEfficiencyUpdated
            self.__efficiencyCtrl.onPersonalEfficiencyReceived += self._onEfficiencyReceived
            self.__efficiencyCtrl.onPersonalEfficiencyLogSynced += self._onPersonalEfficiencyLogSynced
        self.settingsCore.onSettingsChanged += self._onSettingsChanged
        if self.__vehStateCtrl is not None:
            self.__vehStateCtrl.onPostMortemSwitched += self._onPostMortemSwitched
            self.__vehStateCtrl.onVehicleControlling += self._onVehicleControlling
        self.addListener(events.GameEvent.SHOW_EXTENDED_INFO, self._handleShowExtendedInfo, scope=EVENT_BUS_SCOPE.BATTLE)
        self.addListener(events.GameEvent.SHOW_CURSOR, self._handleShowCursor, EVENT_BUS_SCOPE.GLOBAL)
        self.addListener(events.GameEvent.HIDE_CURSOR, self._handleHideCursor, EVENT_BUS_SCOPE.GLOBAL)
        return

    def _dispose(self):
        self.removeListener(events.GameEvent.SHOW_EXTENDED_INFO, self._handleShowExtendedInfo, EVENT_BUS_SCOPE.BATTLE)
        self.removeListener(events.GameEvent.SHOW_CURSOR, self._handleShowCursor, EVENT_BUS_SCOPE.GLOBAL)
        self.removeListener(events.GameEvent.HIDE_CURSOR, self._handleHideCursor, EVENT_BUS_SCOPE.GLOBAL)
        if self.__vehStateCtrl is not None:
            self.__vehStateCtrl.onPostMortemSwitched -= self._onPostMortemSwitched
            self.__vehStateCtrl.onVehicleControlling -= self._onVehicleControlling
        self.settingsCore.onSettingsChanged -= self._onSettingsChanged
        if self.__efficiencyCtrl is not None:
            self.__efficiencyCtrl.onTotalEfficiencyUpdated -= self._onTotalEfficiencyUpdated
            self.__efficiencyCtrl.onPersonalEfficiencyReceived -= self._onEfficiencyReceived
            self.__efficiencyCtrl = None
        self.__vehStateCtrl = None
        self.__arenaDP = None
        self.__topLog.dispose()
        self.__bottomLog.dispose()
        self._totalEvents = None
        super(DamageLogPanel, self)._dispose()
        return

    def _invalidateContent(self):
        """
        Invalidates the content of the whole damage panel.
        """
        self._invalidateTotalDamages()
        self._invalidateLogs()

    def _invalidateLogs(self):
        """
        Updates contents of the top and bottom logs based on the user preferences.
        """
        settingGetter = self.settingsCore.getSetting
        self.__logViewMode = settingGetter(DAMAGE_LOG.SHOW_DETAILS)
        epos = settingGetter(DAMAGE_LOG.EVENT_POSITIONS)
        topLogContentMask, bottomLogContentMask = _EVENT_POSITIONS_TO_CONTENT_MASK[epos]
        topLogRecStyle, bottomLogRecStyle = _EVENT_POSITIONS_TO_RECORD_STYLE[epos]
        displayedEventsContentMask = _DISPLAYED_EVENT_TYPES_TO_CONTENT_MASK[settingGetter(DAMAGE_LOG.SHOW_EVENT_TYPES)]
        topLogContentMask &= displayedEventsContentMask
        bottomLogContentMask &= displayedEventsContentMask
        self.__topLog.updateLog(topLogContentMask, self.__logViewMode, topLogRecStyle)
        self.__bottomLog.updateLog(bottomLogContentMask, self.__logViewMode, bottomLogRecStyle)

    def _invalidateTotalDamages(self):
        """
        Updates the content of the total panel based on the user preferences.
        """
        contentMask = 0
        for settingName, bit in _TOTAL_DAMAGE_SETTINGS_TO_CONTENT_MASK.iteritems():
            if settingName == DAMAGE_LOG.ASSIST_STUN:
                if self._canShowStunAssist():
                    contentMask |= bit
            elif self.settingsCore.getSetting(settingName):
                contentMask |= bit

        if contentMask != self.__totalDamageContentMask:
            self.__totalDamageContentMask = contentMask
            getter = self.__efficiencyCtrl.getTotalEfficiency
            args = [ self._setTotalValue(e, getter(e))[1] for e, _ in self._totalEvents ]
            self.as_summaryStatsS(*args)

    def _canShowStunAssist(self):
        if self.__isSPG is None:
            if self.__arenaDP is None:
                return False
            vehicleType = self.__arenaDP.getVehicleInfo(None).vehicleType
            if vehicleType is None or vehicleType.classTag is None:
                return False
            self.__isSPG = vehicleType.classTag == VEHICLE_CLASS_NAME.SPG
        return self.__isSPG and g_lobbyContext.getServerSettings().spgRedesignFeatures.isStunEnabled()

    def _onTotalEfficiencyUpdated(self, diff):
        """
        Callback to handle change of total values coming from the efficiency controller.
        :param diff: dict of changed total values.
        """
        for e, updateMethod in self._totalEvents:
            if e in diff:
                isUpdated, value = self._setTotalValue(e, diff[e])
                if isUpdated:
                    updateMethod(value)

    def _onPersonalEfficiencyLogSynced(self):
        self.__topLog.invalidate()
        self.__bottomLog.invalidate()

    def _onEfficiencyReceived(self, events):
        self.__topLog.addToLog(events)
        self.__bottomLog.addToLog(events)

    def _invalidatePanelVisibility(self):
        """
        Updates common visibility. The damage panel is not displayed if the player observes
        another vehicle in Postmortem mode. The panel is always visible if the player is in
        Observer mode (first person view).
        """
        isVisible = True
        if self.sessionProvider.getCtx().isPlayerObserver():
            isVisible = True
        elif self.__vehStateCtrl is None:
            isVisible = self.__isVisible
        elif self.__vehStateCtrl.isInPostmortem:
            if self.__arenaDP is None:
                isVisible = self.__isVisible
            else:
                observedVehID = self.__vehStateCtrl.getControllingVehicleID()
                isVisible = self.__arenaDP.getPlayerVehicleID() == observedVehID
        if self.__isVisible != isVisible:
            self.__isVisible = isVisible
            self._setSettings(self.__isVisible, bool(self.settingsCore.getSetting(GRAPHICS.COLOR_BLIND)))
        return

    def _onSettingsChanged(self, diff):
        """
        Callback to handle change of user preferences. Updates content if damage panel related
        settings have been changed.
        :param diff: dict of changed settings
        """
        for key in _TOTAL_DAMAGE_SETTINGS_TO_CONTENT_MASK.iterkeys():
            if key in diff:
                self._invalidateTotalDamages()

        for key in _LOGS_SETTINGS:
            if key in diff:
                self._invalidateLogs()

        if GRAPHICS.COLOR_BLIND in diff:
            self._setSettings(self.__isVisible, bool(diff[GRAPHICS.COLOR_BLIND]))

    def _onPostMortemSwitched(self):
        """
        Callback to handle switching to postmortem mode. The panel should not be displayed if the
        player observes another vehicle.
        """
        self._invalidatePanelVisibility()

    def _onVehicleControlling(self, vehicle):
        """
        Callback to handle switching between vehicles observed by the player. The panel should
        not be displayed if the player observes another vehicle.
        :param vehicle:
        :return:
        """
        self._invalidatePanelVisibility()

    def _handleShowExtendedInfo(self, event):
        """
        Callback on Alt button press event. Shows/hides detailed damage log.
        :param isVisible: Is Alt button is pressed.
        """
        if self.__logViewMode == _VIEW_MODE.SHOW_BY_ALT_PRESS:
            self.as_isDownAltButtonS(event.ctx['isDown'])

    def _handleShowCursor(self, _):
        """
        Callback on Ctrl button press event. Enables scrolling of detailed damage log.
        """
        self.as_isDownCtrlButtonS(True)

    def _handleHideCursor(self, _):
        """
        Callback on Ctrl button release event. Disables scrolling of detailed damage log.
        """
        self.as_isDownCtrlButtonS(False)

    def _setTotalValue(self, etype, value):
        """
        Sets total value with the given efficiency type, taking into account user's preferences.
        
        :param etype: Efficiency type, see PERSONAL_EFFICIENCY_TYPE
        :param value: New value
        :return: tuple(bool, value), where bool - whether value is changed, v
                value - formatted value
        """
        if BitmaskHelper.hasAnyBitSet(self.__totalDamageContentMask, etype):
            value = _formatTotalValue(value)
        else:
            value = None
        if value != self.__totalValues[etype]:
            self.__totalValues[etype] = value
            return (True, value)
        else:
            return (False, value)
            return

    def _updateTopLog(self, isVisible, isShortMode, records):
        self.as_detailStatsTopS(isVisible, isShortMode, records)

    def _addToTopLog(self, value, actionTypeImg, vehicleTypeImg, vehicleName, shellTypeStr, shellTypeBG):
        self.as_addDetailMessageTopS(value, actionTypeImg, vehicleTypeImg, vehicleName, shellTypeStr, shellTypeBG)

    def _updateBottomLog(self, isVisible, isShortMode, records):
        self.as_detailStatsBottomS(isVisible, isShortMode, records)

    def _addToBottomLog(self, value, actionTypeImg, vehicleTypeImg, vehicleName, shellTypeStr, shellTypeBG):
        self.as_addDetailMessageBottomS(value, actionTypeImg, vehicleTypeImg, vehicleName, shellTypeStr, shellTypeBG)

    def _updateTotalDamageValue(self, value):
        self.as_updateSummaryDamageValueS(value)

    def _updateTotalBlockedDamageValue(self, value):
        self.as_updateSummaryBlockedValueS(value)

    def _updateTotalAssistValue(self, value):
        self.as_updateSummaryAssistValueS(value)

    def _updateTotalStunValue(self, value):
        self.as_updateSummaryStunValueS(value)

    def _setSettings(self, isVisible, isColorBlind):
        self.as_setSettingsDamageLogComponentS(isVisible, isColorBlind)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\battle\shared\damage_log_panel.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:32 St�edn� Evropa (letn� �as)
