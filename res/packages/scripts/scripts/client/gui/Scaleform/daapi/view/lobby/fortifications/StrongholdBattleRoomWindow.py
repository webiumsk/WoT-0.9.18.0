# 2017.05.04 15:23:25 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/fortifications/StrongholdBattleRoomWindow.py
import BigWorld
from UnitBase import UNIT_OP
from constants import PREBATTLE_TYPE
from debug_utils import LOG_ERROR
from gui import SystemMessages
from gui.Scaleform.daapi.view.meta.FortBattleRoomWindowMeta import FortBattleRoomWindowMeta
from gui.Scaleform.genConsts.CYBER_SPORT_ALIASES import CYBER_SPORT_ALIASES
from gui.Scaleform.genConsts.FORTIFICATION_ALIASES import FORTIFICATION_ALIASES
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES as I18N_SYSTEM_MESSAGES
from gui.Scaleform.managers.windows_stored_data import stored_window, DATA_TYPE, TARGET_ID
from gui.prb_control import settings, prbPeripheriesHandlerProperty
from gui.prb_control.events_dispatcher import g_eventDispatcher
from gui.prb_control.formatters import messages
from gui.prb_control.entities.base.unit.listener import IStrongholdListener
from gui.prb_control.items.sortie_items import getDivisionNameByUnit
from gui.prb_control.settings import SELECTOR_BATTLE_TYPES, PREBATTLE_ACTION_NAME
from gui.shared import events
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.fortifications.settings import CLIENT_FORT_STATE
from gui.shared.utils import getPlayerDatabaseID, SelectorBattleTypesUtils as selectorUtils
from helpers import i18n
from messenger.storage import storage_getter
from gui.prb_control.entities.base.unit.ctx import AutoSearchUnitCtx, DeclineSearchUnitCtx, BattleQueueUnitCtx
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.shared.formatters import icons, text_styles
from gui.clans import formatters as clans_fmts
from gui.Scaleform.locale.FORTIFICATIONS import FORTIFICATIONS
from gui.Scaleform.daapi.view.lobby.fortifications.StrongholdBattleRoom import StrongholdBattleRoom

@stored_window(DATA_TYPE.UNIQUE_WINDOW, TARGET_ID.CHANNEL_CAROUSEL)

class StrongholdBattleRoomWindow(FortBattleRoomWindowMeta, IStrongholdListener):

    def __init__(self, ctx = None):
        super(StrongholdBattleRoomWindow, self).__init__()

    @prbPeripheriesHandlerProperty
    def prbPeripheriesHandler(self):
        return None

    def onWindowMinimize(self):
        g_eventDispatcher.showUnitProgressInCarousel(self.getPrbType())
        self.destroy()

    def getBrowserViewAlias(self, prbType):
        return FORTIFICATION_ALIASES.STRONGHOLD_BATTLE_ROOM_LIST_VIEW_UI

    def getRoomViewAlias(self, prbType):
        return FORTIFICATION_ALIASES.STRONGHOLD_BATTLE_ROOM_VIEW_UI

    def getFlashAliases(self):
        return FORTIFICATION_ALIASES.FLASH_ALIASES

    def getPythonAliases(self):
        return FORTIFICATION_ALIASES.PYTHON_ALIASES

    def getPrbType(self):
        return PREBATTLE_TYPE.EXTERNAL

    def autoSearchCancel(self, value):
        self.currentState = value
        if value in (CYBER_SPORT_ALIASES.AUTO_SEARCH_COMMANDS_STATE, CYBER_SPORT_ALIASES.AUTO_SEARCH_ERROR_STATE, CYBER_SPORT_ALIASES.AUTO_SEARCH_WAITING_PLAYERS_STATE):
            self.prbEntity.request(AutoSearchUnitCtx(action=0))
        elif value == CYBER_SPORT_ALIASES.AUTO_SEARCH_CONFIRMATION_STATE:
            self.prbEntity.request(DeclineSearchUnitCtx())
        elif value == CYBER_SPORT_ALIASES.AUTO_SEARCH_ENEMY_STATE:
            self.prbEntity.request(BattleQueueUnitCtx(action=0))

    def onUnitPlayerAdded(self, pInfo):
        if not pInfo.isInvite():
            self.__addPlayerNotification(settings.UNIT_NOTIFICATION_KEY.PLAYER_ADDED, pInfo)

    def onUnitPlayerRemoved(self, pInfo):
        if not pInfo.isInvite():
            self.__addPlayerNotification(settings.UNIT_NOTIFICATION_KEY.PLAYER_REMOVED, pInfo)

    def onUnitFlagsChanged(self, flags, timeLeft):
        if self.prbEntity.hasLockedState():
            if flags.isInQueue():
                self.as_enableWndCloseBtnS(False)
                self.currentState = CYBER_SPORT_ALIASES.AUTO_SEARCH_ENEMY_STATE
            else:
                LOG_ERROR('View for modal state is not resolved', flags)
            self.__initState(timeLeft=timeLeft)
        else:
            self.__clearState()

    def onUnitErrorReceived(self, errorCode):
        self.as_autoSearchEnableBtnS(True)

    def onUnitAutoSearchFinished(self):
        self.__clearState()

    def onUnitPlayerRolesChanged(self, pInfo, pPermissions):
        if pInfo.isCurrentPlayer():
            self.as_changeAutoSearchBtnsStateS(pPermissions.canInvokeAutoSearch(), pPermissions.canStopBattleQueue())
        self.prbEntity.strongholdDataChanged()

    def onUnitPlayerOnlineStatusChanged(self, pInfo):
        super(StrongholdBattleRoomWindow, self).onUnitPlayerOnlineStatusChanged(pInfo)
        if pInfo.isOffline():
            key = settings.UNIT_NOTIFICATION_KEY.PLAYER_OFFLINE
        else:
            key = settings.UNIT_NOTIFICATION_KEY.PLAYER_ONLINE
        self.__addPlayerNotification(key, pInfo)

    def onUnitRejoin(self):
        self.__clearState()

    def onUnitPlayerBecomeCreator(self, pInfo):
        if pInfo.isCurrentPlayer():
            self._showLeadershipNotification()
        super(StrongholdBattleRoomWindow, self).onUnitPlayerBecomeCreator(pInfo)

    def onUnitRosterChanged(self):
        super(StrongholdBattleRoomWindow, self).onUnitRosterChanged()
        chat = self.chat
        if chat:
            _, unit = self.prbEntity.getUnit()
            commanderID = unit.getCommanderDBID()
            if commanderID != getPlayerDatabaseID():
                getter = storage_getter('users')
                commander = getter().getUser(commanderID)
                if commander is None:
                    return
                division = getDivisionNameByUnit(unit)
                divisionName = i18n.makeString(I18N_SYSTEM_MESSAGES.unit_notification_divisiontype(division))
                key = I18N_SYSTEM_MESSAGES.UNIT_NOTIFICATION_CHANGEDIVISION
                txt = i18n.makeString(key, name=commander.getName(), division=divisionName)
                chat.addNotification(txt)
        return

    def onUnitSettingChanged(self, opCode, value):
        if opCode == UNIT_OP.CHANGE_DIVISION:
            unitMgrID = self.prbEntity.getID()
            if unitMgrID > 0:
                self._loadRoomView(self.prbEntity.getEntityType())

    def refresh(self):
        self.as_setInfoS(False, '', '')
        self.showStrongholdWaiting(True)
        self.prbEntity.requestUpdateStronghold()

    def onStrongholdOnReadyStateChanged(self):
        g_eventDispatcher.updateUI()

    def showStrongholdWaiting(self, visible):
        self.as_setWaitingS(visible, '#waiting:prebattle/change_settings')
        g_eventDispatcher.updateUI()

    def onStrongholdMaintenance(self):
        text = str().join((icons.makeImageTag(RES_ICONS.MAPS_ICONS_LIBRARY_ALERTBIGICON, 24, 24, -6, 0),
         text_styles.middleTitle(i18n.makeString(FORTIFICATIONS.MAINWINDOW_MAINTENANCE_HEADER)),
         clans_fmts.getHtmlLineDivider(10),
         text_styles.main(i18n.makeString(FORTIFICATIONS.MAINWINDOW_MAINTENANCE_BODY))))
        self.as_setInfoS(True, text, FORTIFICATIONS.MAINWINDOW_MAINTENANCE_BUTTON)
        self.as_enableWndCloseBtnS(True)
        g_eventDispatcher.updateUI()

    def onStrongholdRequestTextMessage(self, textType, textString):
        SystemMessages.pushMessage(textString, type=textType)

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(StrongholdBattleRoomWindow, self)._onRegisterFlashComponent(viewPy, alias)
        if isinstance(viewPy, StrongholdBattleRoom):
            viewPy.setProxy(self)

    def _populate(self):
        selectorUtils.setBattleTypeAsKnown(SELECTOR_BATTLE_TYPES.SORTIE)
        self.addListener(events.HideWindowEvent.HIDE_UNIT_WINDOW, self.__handleUnitWindowHide, scope=EVENT_BUS_SCOPE.LOBBY)
        self.addListener(events.RenameWindowEvent.RENAME_WINDOW, self.__handleWindowRename, scope=EVENT_BUS_SCOPE.LOBBY)
        super(StrongholdBattleRoomWindow, self)._populate()
        self.prbEntity.initEvents(self)
        g_eventDispatcher.hideUnitProgressInCarousel(self.getPrbType())

    def _dispose(self):
        self.removeListener(events.HideWindowEvent.HIDE_UNIT_WINDOW, self.__handleUnitWindowHide, scope=EVENT_BUS_SCOPE.LOBBY)
        self.removeListener(events.RenameWindowEvent.RENAME_WINDOW, self.__handleWindowRename, scope=EVENT_BUS_SCOPE.LOBBY)
        super(StrongholdBattleRoomWindow, self)._dispose()

    def __handleUnitWindowHide(self, _):
        self.destroy()

    def __handleWindowRename(self, event):
        title = event.ctx['data']
        self.as_setWindowTitleS(title)

    def __initState(self, timeLeft = 0, acceptDelta = 0):
        model = None
        if self.isPlayerInSlot():
            if self.currentState == CYBER_SPORT_ALIASES.AUTO_SEARCH_ENEMY_STATE:
                model = self.__createAutoUpdateModel(self.currentState, timeLeft, '', [])
            elif self.currentState == CYBER_SPORT_ALIASES.AUTO_SEARCH_ERROR_STATE:
                model = self.__createAutoUpdateModel(self.currentState, 0, '', [])
        if model is not None:
            self.as_changeAutoSearchStateS(model)
        return

    def __clearState(self):
        self.currentState = ''
        self.as_enableWndCloseBtnS(True)
        self.as_hideAutoSearchS()

    def __createAutoUpdateModel(self, state, countDownSeconds, ctxMessage, playersReadiness):
        permissions = self.prbEntity.getPermissions(unitIdx=self.prbEntity.getUnitIdx())
        model = {'state': state,
         'countDownSeconds': countDownSeconds,
         'contextMessage': ctxMessage,
         'playersReadiness': playersReadiness,
         'canInvokeAutoSearch': permissions.canInvokeAutoSearch(),
         'canInvokeBattleQueue': permissions.canStopBattleQueue()}
        return model

    def __addPlayerNotification(self, key, pInfo):
        chat = self.chat
        if chat and not pInfo.isCurrentPlayer():
            chat.as_addMessageS(messages.getUnitPlayerNotification(key, pInfo))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\fortifications\StrongholdBattleRoomWindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:25 St�edn� Evropa (letn� �as)
