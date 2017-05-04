# 2017.05.04 15:23:17 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/fortifications/FortClanListWindow.py
import BigWorld
from gui.Scaleform.daapi.view.lobby.fortifications.fort_utils.FortViewHelper import FortViewHelper
from gui.Scaleform.daapi.view.lobby.rally import vo_converters
from gui.Scaleform.daapi.view.meta.FortClanListWindowMeta import FortClanListWindowMeta
from gui.Scaleform.genConsts.TEXT_ALIGN import TEXT_ALIGN
from gui.Scaleform.locale.FORTIFICATIONS import FORTIFICATIONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.clans.formatters import getClanRoleString
from gui.shared.ClanCache import g_clanCache
from gui.shared.formatters import icons, text_styles
from gui.shared.fortifications.settings import CLIENT_FORT_STATE
from helpers import i18n, dependency
from skeletons.gui.game_control import IGameSessionController

class FortClanListWindow(FortClanListWindowMeta, FortViewHelper):
    gameSession = dependency.descriptor(IGameSessionController)

    def __init__(self, _ = None):
        super(FortClanListWindow, self).__init__()

    def _populate(self):
        super(FortClanListWindow, self)._populate()
        self.startFortListening()
        self.gameSession.onNewDayNotify += self.__gameSession_onNewDayNotify
        self._update()

    def _dispose(self):
        self.stopFortListening()
        self.gameSession.onNewDayNotify -= self.__gameSession_onNewDayNotify
        super(FortClanListWindow, self)._dispose()

    def _update(self):
        initData = {'windowTitle': i18n.makeString(FORTIFICATIONS.FORTCLANLISTWINDOW_TITLE, clanName=g_clanCache.clanTag),
         'members': self._getClanMembers(),
         'tableHeader': [self._createHeader(FORTIFICATIONS.CLANLISTWINDOW_TABLE_MEMBERNAME, 'userName', 181, 0, TOOLTIPS.FORTIFICATION_FIXEDPLAYERS_NIC, TEXT_ALIGN.LEFT, sortType='string'),
                         self._createHeader(FORTIFICATIONS.CLANLISTWINDOW_TABLE_ROLE, 'playerRoleID', 203, 1, TOOLTIPS.FORTIFICATION_FIXEDPLAYERS_FORTROLE, TEXT_ALIGN.LEFT),
                         self._createHeader(i18n.makeString(FORTIFICATIONS.FIXEDPLAYERS_LISTHEADER_FIELDWEEK, icon=icons.nut()), 'intWeekMining', 137, 2, TOOLTIPS.FORTIFICATION_FIXEDPLAYERS_WEEK, TEXT_ALIGN.RIGHT),
                         self._createHeader(i18n.makeString(FORTIFICATIONS.FIXEDPLAYERS_LISTHEADER_FIELDALLTIME, icon=icons.nut()), 'intTotalMining', 147, 3, TOOLTIPS.FORTIFICATION_FIXEDPLAYERS_ALLTIME, TEXT_ALIGN.CENTER)]}
        self.as_setDataS(initData)

    def _createHeader(self, label, iconId, buttonWidth, sortOrder, toolTip, textAlign, sortType = 'numeric'):
        return {'label': label,
         'id': iconId,
         'sortOrder': sortOrder,
         'buttonWidth': buttonWidth,
         'toolTip': toolTip,
         'textAlign': textAlign,
         'sortType': sortType,
         'defaultSortDirection': 'descending'}

    def _getClanMembers(self):
        clanMembers = []
        for member in g_clanCache.clanMembers:
            intTotalMining, intWeekMining = self.fortCtrl.getFort().getPlayerContributions(member.getID())
            role = self._getClanRole(member)
            roleID = self.CLAN_MEMBER_ROLES.index(member.getClanRole())
            vo = vo_converters.makeSimpleClanListRenderVO(member, intTotalMining, intWeekMining, role, roleID)
            clanMembers.append(vo)

        return clanMembers

    def __gameSession_onNewDayNotify(self, _):
        self._update()

    def _getClanRole(self, member):
        return text_styles.standard(i18n.makeString(getClanRoleString(member.getClanRole())))

    def _getWeekMiningStr(self, weekMining):
        randWeek = BigWorld.wg_getIntegralFormat(weekMining)
        return text_styles.defRes(randWeek)

    def _getTotalMiningStr(self, totalMining):
        allTime = BigWorld.wg_getIntegralFormat(totalMining)
        return text_styles.defRes(allTime)

    def onWindowClose(self):
        self.destroy()

    def onClanMembersListChanged(self):
        self._update()

    def onUpdated(self, isFullUpdate):
        self._update()

    def onClientStateChanged(self, state):
        if state.getStateID() == CLIENT_FORT_STATE.DISABLED:
            self.onWindowClose()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\fortifications\FortClanListWindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:18 St�edn� Evropa (letn� �as)
