# 2017.05.04 15:23:00 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/clans/clan_cm_handlers.py
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuHandler
from gui.Scaleform.locale.MENU import MENU
from gui.clans import formatters as clans_fmts
from gui.shared import event_dispatcher, utils
from shared_utils import CONST_CONTAINER

class CLAN_CM_OPTIONS(CONST_CONTAINER):
    CLAN_PROFILE = 'clanProfile'
    COPY_TO_CB = 'copyToClipboard'


class BaseClanCMHandler(AbstractContextMenuHandler, EventSystemEntity):

    def __init__(self, cmProxy, ctx = None):
        super(BaseClanCMHandler, self).__init__(cmProxy, ctx, {CLAN_CM_OPTIONS.CLAN_PROFILE: 'showClanProfile',
         CLAN_CM_OPTIONS.COPY_TO_CB: 'copyToClipboard'})
        self.__clanDbID = int(ctx.dbID)
        self.__clanName = ctx.clanName
        self.__clanAbbrev = ctx.clanAbbrev

    def showClanProfile(self):
        event_dispatcher.showClanProfileWindow(self.__clanDbID, self.__clanAbbrev)

    def copyToClipboard(self):
        utils.copyToClipboard(clans_fmts.getClanFullName(self.__clanName, self.__clanAbbrev))

    def _generateOptions(self, ctx = None):
        return [self._makeItem(CLAN_CM_OPTIONS.CLAN_PROFILE, MENU.contextmenu('viewClanProfile')), self._makeItem(CLAN_CM_OPTIONS.COPY_TO_CB, MENU.contextmenu('copyClanName'))]
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\clans\clan_cm_handlers.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:01 St�edn� Evropa (letn� �as)
