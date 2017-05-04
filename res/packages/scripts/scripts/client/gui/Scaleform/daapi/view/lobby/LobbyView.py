# 2017.05.04 15:22:53 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/LobbyView.py
import weakref
import constants
import gui
from PlayerEvents import g_playerEvents
from gui import SystemMessages
from gui.LobbyContext import g_lobbyContext
from gui.Scaleform.Waiting import Waiting
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.meta.LobbyPageMeta import LobbyPageMeta
from gui.Scaleform.framework import ViewTypes
from gui.Scaleform.framework.entities.View import View
from gui.Scaleform.genConsts.FORTIFICATION_ALIASES import FORTIFICATION_ALIASES
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES
from gui.prb_control.dispatcher import g_prbLoader
from gui.shared import EVENT_BUS_SCOPE, events
from gui.shared.ItemsCache import g_itemsCache
from gui.shared.utils import isPopupsWindowsOpenDisabled
from gui.shared.utils.HangarSpace import g_hangarSpace
from gui.shared.utils.functions import getViewName
from helpers import i18n, dependency
from messenger.m_constants import PROTO_TYPE
from messenger.proto import proto_getter
from skeletons.gui.game_control import IIGRController

class _LobbySubViewsCtrl(object):
    """
    The class encapsulate the logic related to controlling of lobby subviews loading.
    It's responsible for showing the Waiting pop-up when lobby subviews are being loaded.
    """
    __WAITING_LBL = 'loadPage'
    __SUB_VIEWS = (VIEW_ALIAS.LOBBY_HANGAR,
     VIEW_ALIAS.LOBBY_INVENTORY,
     VIEW_ALIAS.LOBBY_STORE,
     VIEW_ALIAS.LOBBY_PROFILE,
     VIEW_ALIAS.LOBBY_BARRACKS,
     PREBATTLE_ALIASES.TRAINING_LIST_VIEW_PY,
     PREBATTLE_ALIASES.TRAINING_ROOM_VIEW_PY,
     VIEW_ALIAS.LOBBY_CUSTOMIZATION,
     VIEW_ALIAS.VEHICLE_PREVIEW,
     VIEW_ALIAS.VEHICLE_COMPARE,
     VIEW_ALIAS.VEHICLE_COMPARE_MAIN_CONFIGURATOR,
     VIEW_ALIAS.LOBBY_RESEARCH,
     VIEW_ALIAS.LOBBY_TECHTREE,
     FORTIFICATION_ALIASES.FORTIFICATIONS_VIEW_ALIAS,
     VIEW_ALIAS.BATTLE_QUEUE,
     VIEW_ALIAS.LOBBY_ACADEMY)

    def __init__(self):
        super(_LobbySubViewsCtrl, self).__init__()
        self.__loaderManager = None
        self.__loadingSubViews = set()
        self.__isWaitingVisible = False
        return

    def start(self, loaderManager):
        self.__loaderManager = weakref.proxy(loaderManager)
        self.__loaderManager.onViewLoadInit += self.__onViewLoadInit
        self.__loaderManager.onViewLoaded += self.__onViewLoaded
        self.__loaderManager.onViewLoadCanceled += self.__onViewLoadCanceled
        self.__loaderManager.onViewLoadError += self.__onViewLoadError

    def stop(self):
        if self.__loaderManager is not None:
            self.__loaderManager.onViewLoadInit -= self.__onViewLoadInit
            self.__loaderManager.onViewLoaded -= self.__onViewLoaded
            self.__loaderManager.onViewLoadCanceled -= self.__onViewLoadCanceled
            self.__loaderManager.onViewLoadError -= self.__onViewLoadError
            self.__loaderManager = None
        self.__loadingSubViews.clear()
        self.__invalidateWaitingStatus()
        return

    def __onViewLoadInit(self, view):
        if view is not None and view.settings is not None:
            alias = view.settings.alias
            if alias in self.__SUB_VIEWS and alias not in self.__loadingSubViews:
                self.__loadingSubViews.add(alias)
                self.__invalidateWaitingStatus()
        return

    def __onViewLoaded(self, view):
        if view is not None and view.settings is not None:
            alias = view.settings.alias
            if alias in self.__SUB_VIEWS and alias in self.__loadingSubViews:
                self.__loadingSubViews.remove(alias)
                self.__invalidateWaitingStatus()
        return

    def __onViewLoadCanceled(self, key, item):
        if item is not None and item.pyEntity is not None:
            alias = item.pyEntity.alias
            if alias in self.__SUB_VIEWS and alias in self.__loadingSubViews:
                self.__loadingSubViews.remove(alias)
                self.__invalidateWaitingStatus()
        return

    def __onViewLoadError(self, key, msg, item):
        if item is not None and item.pyEntity is not None:
            alias = item.pyEntity.settings.alias
            if alias in self.__SUB_VIEWS and alias in self.__loadingSubViews:
                self.__loadingSubViews.remove(alias)
                self.__invalidateWaitingStatus()
        return

    def __invalidateWaitingStatus(self):
        if self.__loadingSubViews:
            if not self.__isWaitingVisible:
                self.__isWaitingVisible = True
                Waiting.show(self.__WAITING_LBL)
        elif self.__isWaitingVisible:
            self.__isWaitingVisible = False
            Waiting.hide(self.__WAITING_LBL)


class LobbyView(LobbyPageMeta):

    class COMPONENTS:
        HEADER = 'lobbyHeader'

    igrCtrl = dependency.descriptor(IIGRController)

    def __init__(self, ctx = None):
        super(LobbyView, self).__init__(ctx)
        self.__currIgrType = constants.IGR_TYPE.NONE
        self.__subViesCtrl = _LobbySubViewsCtrl()

    @proto_getter(PROTO_TYPE.BW_CHAT2)
    def bwProto(self):
        return None

    def getSubContainerType(self):
        return ViewTypes.LOBBY_SUB

    def _populate(self):
        View._populate(self)
        self.__currIgrType = self.igrCtrl.getRoomType()
        g_prbLoader.setEnabled(True)
        self.addListener(events.LobbySimpleEvent.SHOW_HELPLAYOUT, self.__showHelpLayout, EVENT_BUS_SCOPE.LOBBY)
        self.addListener(events.LobbySimpleEvent.CLOSE_HELPLAYOUT, self.__closeHelpLayout, EVENT_BUS_SCOPE.LOBBY)
        self.addListener(events.GameEvent.SCREEN_SHOT_MADE, self.__handleScreenShotMade, EVENT_BUS_SCOPE.GLOBAL)
        g_playerEvents.onVehicleBecomeElite += self.__onVehicleBecomeElite
        self.__subViesCtrl.start(self.app.loaderManager)
        self.igrCtrl.onIgrTypeChanged += self.__onIgrTypeChanged
        battlesCount = g_itemsCache.items.getAccountDossier().getTotalStats().getBattlesCount()
        g_lobbyContext.updateBattlesCount(battlesCount)
        self.fireEvent(events.GUICommonEvent(events.GUICommonEvent.LOBBY_VIEW_LOADED))
        self.bwProto.voipController.invalidateMicrophoneMute()

    def _invalidate(self):
        g_prbLoader.setEnabled(True)
        super(LobbyView, self)._invalidate()

    def _dispose(self):
        self.igrCtrl.onIgrTypeChanged -= self.__onIgrTypeChanged
        self.__subViesCtrl.stop()
        g_playerEvents.onVehicleBecomeElite -= self.__onVehicleBecomeElite
        self.removeListener(events.LobbySimpleEvent.SHOW_HELPLAYOUT, self.__showHelpLayout, EVENT_BUS_SCOPE.LOBBY)
        self.removeListener(events.LobbySimpleEvent.CLOSE_HELPLAYOUT, self.__closeHelpLayout, EVENT_BUS_SCOPE.LOBBY)
        self.removeListener(events.GameEvent.SCREEN_SHOT_MADE, self.__handleScreenShotMade, EVENT_BUS_SCOPE.GLOBAL)
        View._dispose(self)

    def __showHelpLayout(self, _):
        self.as_showHelpLayoutS()

    def __closeHelpLayout(self, _):
        self.as_closeHelpLayoutS()

    def __handleScreenShotMade(self, event):
        if 'path' not in event.ctx:
            return
        SystemMessages.pushMessage(i18n.makeString('#menu:screenshot/save') % {'path': event.ctx['path']}, SystemMessages.SM_TYPE.Information)

    def __onVehicleBecomeElite(self, vehTypeCompDescr):
        if not isPopupsWindowsOpenDisabled():
            self.fireEvent(events.LoadViewEvent(VIEW_ALIAS.ELITE_WINDOW, getViewName(VIEW_ALIAS.ELITE_WINDOW, vehTypeCompDescr), {'vehTypeCompDescr': vehTypeCompDescr}), EVENT_BUS_SCOPE.LOBBY)

    def moveSpace(self, dx, dy, dz):
        if g_hangarSpace.space:
            g_hangarSpace.space.handleMouseEvent(int(dx), int(dy), int(dz))

    def notifyCursorOver3dScene(self, isOver3dScene):
        self.fireEvent(events.LobbySimpleEvent(events.LobbySimpleEvent.NOTIFY_CURSOR_OVER_3DSCENE, ctx={'isOver3dScene': isOver3dScene}))

    def __onIgrTypeChanged(self, roomType, xpFactor):
        icon = gui.makeHtmlString('html_templates:igr/iconSmall', 'premium')
        if roomType == constants.IGR_TYPE.PREMIUM:
            SystemMessages.pushMessage(i18n.makeString(SYSTEM_MESSAGES.IGR_CUSTOMIZATION_BEGIN, igrIcon=icon), type=SystemMessages.SM_TYPE.Information)
        elif roomType in [constants.IGR_TYPE.BASE, constants.IGR_TYPE.NONE] and self.__currIgrType == constants.IGR_TYPE.PREMIUM:
            SystemMessages.pushMessage(i18n.makeString(SYSTEM_MESSAGES.IGR_CUSTOMIZATION_END, igrIcon=icon), type=SystemMessages.SM_TYPE.Information)
        self.__currIgrType = roomType
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\LobbyView.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:53 St�edn� Evropa (letn� �as)
