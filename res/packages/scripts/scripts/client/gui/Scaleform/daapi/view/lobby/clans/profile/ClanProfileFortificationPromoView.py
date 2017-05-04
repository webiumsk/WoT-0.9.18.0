# 2017.05.04 15:23:04 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/clans/profile/ClanProfileFortificationPromoView.py
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.clans.clan_profile_event import ClanProfileEvent
from gui.Scaleform.daapi.view.meta.ClanProfileFortificationPromoViewMeta import ClanProfileFortificationPromoViewMeta
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.fortifications.settings import CLIENT_FORT_STATE

class ClanProfileFortificationPromoView(ClanProfileFortificationPromoViewMeta):

    def __init__(self):
        super(ClanProfileFortificationPromoView, self).__init__()
        self.__clanDossier = None
        self.__fortWelcomeView = None
        self.__proxy = None
        return

    def setProxy(self, proxy, clanDossier):
        self.__proxy = proxy
        self.__clanDossier = clanDossier
        self.__updateViewClanInfo()

    def updateData(self):
        self.__updateViewClanInfo()

    def _dispose(self):
        self.__clanDossier = None
        self.__fortWelcomeView = None
        self.__proxy = None
        super(ClanProfileFortificationPromoView, self)._dispose()
        return

    def _onRegisterFlashComponent(self, viewPy, alias):
        if alias == VIEW_ALIAS.FORT_WELCOME_INFO:
            self.__fortWelcomeView = viewPy
            viewPy.onFortCreationRequested += self.__fortCreationRequestedHandler
            viewPy.onFortCreationDone += self.__fortCreationDoneHandler
            self.__updateViewClanInfo()

    def _onUnregisterFlashComponent(self, viewPy, alias):
        if alias == VIEW_ALIAS.FORT_WELCOME_INFO:
            viewPy.onFortCreationRequested -= self.__fortCreationRequestedHandler
            viewPy.onFortCreationDone -= self.__fortCreationDoneHandler
        super(ClanProfileFortificationPromoView, self)._onUnregisterFlashComponent(viewPy, alias)

    def __fortCreationRequestedHandler(self):
        fortDP = self.__proxy.fortDP
        if fortDP is not None:
            fortDP.createFort()
        return

    def __fortCreationDoneHandler(self):
        self.fireEvent(ClanProfileEvent(ClanProfileEvent.CLOSE_CLAN_PROFILE), EVENT_BUS_SCOPE.LOBBY)

    def __updateViewClanInfo(self):
        if self.__fortWelcomeView and self.__clanDossier and self.__proxy.fortState.getStateID() != CLIENT_FORT_STATE.UNSUBSCRIBED:
            self.__proxy.showWaiting()
            self.__fortWelcomeView.setMyClan(self.__clanDossier.isMyClan())
            self.__proxy.hideWaiting()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\clans\profile\ClanProfileFortificationPromoView.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:04 St�edn� Evropa (letn� �as)
