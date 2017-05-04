# 2017.05.04 15:23:42 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/prb_windows/CompanyMainWindow.py
import weakref
from adisp import process
from constants import PREBATTLE_COMPANY_DIVISION
from debug_utils import LOG_ERROR
from gui.Scaleform.daapi.view.meta.CompanyMainWindowMeta import CompanyMainWindowMeta
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES
from gui.Scaleform.locale.CHAT import CHAT
from gui.prb_control import formatters
from gui.prb_control.entities.base.legacy.listener import ILegacyListener
from gui.prb_control.entities.company.legacy.ctx import CompanySettingsCtx, JoinCompanyCtx
from gui.prb_control.settings import CTRL_ENTITY_TYPE
from gui.shared import events
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.events import FocusEvent
from messenger.gui.Scaleform.view.lobby import MESSENGER_VIEW_ALIAS

class CompanyMainWindow(CompanyMainWindowMeta, ILegacyListener):

    def __init__(self, ctx):
        super(CompanyMainWindow, self).__init__()
        self.updateCtxParams(ctx)
        self.__clientID = None
        try:
            self.__clientID = ctx['clientID']
        except KeyError:
            LOG_ERROR('Strict condition, clientID have to be passed!!!')

        return

    def onTeamStatesReceived(self, entity, team1State, team2State):
        self.as_enableWndCloseBtnS(not team1State.isInQueue())

    def getFlashAliases(self):
        return PREBATTLE_ALIASES.FLASH_ALIASES

    def getPythonAliases(self):
        return PREBATTLE_ALIASES.PYTHON_ALIASES

    def destroy(self):
        super(CompanyMainWindow, self).destroy()

    def onFocusIn(self, alias):
        self.fireEvent(FocusEvent(FocusEvent.COMPONENT_FOCUSED, {'clientID': self.__clientID}))

    def updateWindowState(self, ctx):
        self.updateCtxParams(ctx)
        self.updateView()

    def updateCtxParams(self, ctx):
        self._isInvitesOpen = ctx.get('isInvitesOpen', False)
        if self.__isCompanyPreBattleAlreadyExists():
            self._currentView = PREBATTLE_ALIASES.COMPANY_ROOM_VIEW_PY
        else:
            self._currentView = PREBATTLE_ALIASES.COMPANY_LIST_VIEW_PY

    def updateView(self):
        if self._currentView == PREBATTLE_ALIASES.COMPANY_LIST_VIEW_PY:
            self._requestViewLoad(PREBATTLE_ALIASES.COMPANY_LIST_VIEW_UI, None)
            self.as_setWindowTitleS(CHAT.CHANNELS_COMPANY, 'teamList')
        elif self._currentView == PREBATTLE_ALIASES.COMPANY_ROOM_VIEW_PY:
            self._requestViewLoad(PREBATTLE_ALIASES.COMPANY_ROOM_VIEW_UI, None)
            self.as_setWindowTitleS(self.getCompanyName(), 'team')
            if self._isInvitesOpen:
                self.showPrebattleSendInvitesWindow()
        return

    def showPrebattleSendInvitesWindow(self):
        if self.canSendInvite():
            self.fireEvent(events.LoadViewEvent(PREBATTLE_ALIASES.SEND_INVITES_WINDOW_PY, ctx={'prbName': 'company',
             'ctrlType': CTRL_ENTITY_TYPE.LEGACY}), scope=EVENT_BUS_SCOPE.LOBBY)

    def onWindowMinimize(self):
        self.minimizing()
        self.destroy()

    def getCompanyName(self):
        return formatters.getCompanyName()

    def showFAQWindow(self):
        self.fireEvent(events.LoadViewEvent(MESSENGER_VIEW_ALIAS.FAQ_WINDOW), scope=EVENT_BUS_SCOPE.LOBBY)

    def getClientID(self):
        return self.__clientID

    def canSendInvite(self):
        return self.prbEntity.getPermissions().canSendInvite()

    def onBrowseRallies(self):
        self._currentView = PREBATTLE_ALIASES.COMPANY_LIST_VIEW_PY
        self.updateView()

    def onCreateRally(self):
        self.__requestToCreate()

    def onJoinRally(self, rallyId, slotIndex = None, peripheryID = None):
        self.__requestToJoin(rallyId)

    def _populate(self):
        super(CompanyMainWindow, self)._populate()
        self.addListener(events.HideWindowEvent.HIDE_COMPANY_WINDOW, self.__handleWindowHide, scope=EVENT_BUS_SCOPE.LOBBY)
        self.startPrbListening()
        self.updateView()

    def _dispose(self):
        self.removeListener(events.HideWindowEvent.HIDE_COMPANY_WINDOW, self.__handleWindowHide, scope=EVENT_BUS_SCOPE.LOBBY)
        self.stopPrbListening()
        super(CompanyMainWindow, self)._dispose()

    def _onRegisterFlashComponent(self, viewPy, alias):
        if alias == PREBATTLE_ALIASES.COMPANY_LIST_VIEW_PY:
            self.as_showWaitingS('#waiting:Flash', {})
            viewPy.setProxy(weakref.proxy(self))

    def __handleWindowHide(self, _):
        self.destroy()

    def __isCompanyPreBattleAlreadyExists(self):
        return self.prbEntity.getID() != 0

    @process
    def __requestToCreate(self):
        yield self.prbDispatcher.create(CompanySettingsCtx(waitingID='prebattle/create', division=PREBATTLE_COMPANY_DIVISION.CHAMPION))

    @process
    def __requestToJoin(self, prbID):
        yield self.prbDispatcher.join(JoinCompanyCtx(prbID, waitingID='prebattle/join'))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\prb_windows\CompanyMainWindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:42 St�edn� Evropa (letn� �as)
