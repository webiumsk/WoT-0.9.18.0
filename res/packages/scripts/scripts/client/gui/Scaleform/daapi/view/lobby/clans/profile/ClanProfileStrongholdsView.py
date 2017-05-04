# 2017.05.04 15:23:05 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/clans/profile/ClanProfileStrongholdsView.py
import BigWorld
from adisp import process
from helpers import dependency
from gui.clans.clan_helpers import getStrongholdClanCardUrl, isStrongholdsEnabled
from gui.Scaleform.daapi.view.lobby.clans.profile.ClanProfileBaseView import ClanProfileBaseView
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.strongholds.web_handlers import createStrongholdsWebHandlers
from skeletons.gui.game_control import IBrowserController

class ClanProfileStrongholdsView(ClanProfileBaseView):
    browserCtrl = dependency.descriptor(IBrowserController)

    def __init__(self):
        super(ClanProfileStrongholdsView, self).__init__()
        self.__browserId = 0
        self.__size = None
        return

    @process
    def setClanDossier(self, clanDossier):
        if not isStrongholdsEnabled():
            self._dummyMustBeShown = True
            self._updateDummy()
            self._hideWaiting()
            return
        super(ClanProfileStrongholdsView, self).setClanDossier(clanDossier)
        self._showWaiting()
        url = getStrongholdClanCardUrl(clanDossier.getDbID())
        self.__browserId = yield self.browserCtrl.load(url=url, useBrowserWindow=False, showBrowserCallback=self.__showBrowser, browserSize=self.__size)
        browser = self.browserCtrl.getBrowser(self.__browserId)
        if browser:
            browser.ignoreKeyEvents = True
        self._hideWaiting()

    def viewSize(self, width, height):
        self.__size = (width, height)

    def _onRegisterFlashComponent(self, viewPy, alias):
        if alias == VIEW_ALIAS.BROWSER:
            viewPy.init(self.__browserId, createStrongholdsWebHandlers())

    def __showBrowser(self):
        BigWorld.callback(0.01, self.as_loadBrowserS)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\clans\profile\ClanProfileStrongholdsView.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:05 St�edn� Evropa (letn� �as)
