# 2017.05.04 15:22:37 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/__init__.py
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.battle.shared.page import SharedPage
from gui.Scaleform.framework import ViewSettings, ViewTypes, ScopeTemplates
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES
from gui.app_loader.settings import APP_NAME_SPACE
from gui.shared import EVENT_BUS_SCOPE, events
__all__ = ('SharedPage',)

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.battle.shared import battle_loading
    from gui.Scaleform.daapi.view.battle.shared import battle_timers
    from gui.Scaleform.daapi.view.battle.shared import consumables_panel
    from gui.Scaleform.daapi.view.battle.shared import damage_info_panel
    from gui.Scaleform.daapi.view.battle.shared import damage_panel
    from gui.Scaleform.daapi.view.battle.shared import debug_panel
    from gui.Scaleform.daapi.view.battle.shared import indicators
    from gui.Scaleform.daapi.view.battle.shared import ingame_help
    from gui.Scaleform.daapi.view.battle.shared import ingame_menu
    from gui.Scaleform.daapi.view.battle.shared import messages
    from gui.Scaleform.daapi.view.battle.shared import radial_menu
    from gui.Scaleform.daapi.view.battle.shared import ribbons_panel
    from gui.Scaleform.daapi.view.battle.shared import battle_ticker
    from gui.Scaleform.daapi.view.dialogs import deserter_dialog
    from gui.Scaleform.daapi.view.battle.shared import postmortem_panel
    from gui.Scaleform.daapi.view.battle.shared import damage_log_panel
    from gui.Scaleform.daapi.view.battle.shared import battle_loading_minimap
    return (ViewSettings(VIEW_ALIAS.INGAME_MENU, ingame_menu.IngameMenu, 'ingameMenu.swf', ViewTypes.TOP_WINDOW, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(VIEW_ALIAS.INGAME_DESERTER, deserter_dialog.IngameDeserterDialog, 'deserterDialog.swf', ViewTypes.TOP_WINDOW, None, ScopeTemplates.DYNAMIC_SCOPE),
     ViewSettings(BATTLE_VIEW_ALIASES.BATTLE_DAMAGE_LOG_PANEL, damage_log_panel.DamageLogPanel, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(VIEW_ALIAS.INGAME_HELP, ingame_help.IngameHelpWindow, 'ingameHelpWindow.swf', ViewTypes.WINDOW, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(BATTLE_VIEW_ALIASES.DAMAGE_PANEL, damage_panel.DamagePanel, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(BATTLE_VIEW_ALIASES.DEBUG_PANEL, debug_panel.DebugPanel, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(BATTLE_VIEW_ALIASES.CONSUMABLES_PANEL, consumables_panel.ConsumablesPanel, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(BATTLE_VIEW_ALIASES.PREBATTLE_TIMER, battle_timers.PreBattleTimer, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(BATTLE_VIEW_ALIASES.VEHICLE_MESSAGES, messages.VehicleMessages, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(BATTLE_VIEW_ALIASES.VEHICLE_ERROR_MESSAGES, messages.VehicleErrorMessages, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(BATTLE_VIEW_ALIASES.PLAYER_MESSAGES, messages.PlayerMessages, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(BATTLE_VIEW_ALIASES.RADIAL_MENU, radial_menu.RadialMenu, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(BATTLE_VIEW_ALIASES.DAMAGE_INFO_PANEL, damage_info_panel.DamageInfoPanel, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(BATTLE_VIEW_ALIASES.SIXTH_SENSE, indicators.SixthSenseIndicator, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(BATTLE_VIEW_ALIASES.RIBBONS_PANEL, ribbons_panel.BattleRibbonsPanel, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(BATTLE_VIEW_ALIASES.TICKER, battle_ticker.BattleTicker, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(BATTLE_VIEW_ALIASES.POSTMORTEM_PANEL, postmortem_panel.PostmortemPanel, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(VIEW_ALIAS.MINIMAP_ON_BATTLE_LOADING, battle_loading_minimap.BattleLoadingMinimapComponent, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(BATTLE_VIEW_ALIASES.SIEGE_MODE_INDICATOR, indicators.SiegeModeIndicator, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE))


def getBusinessHandlers():
    return (BattlePackageBusinessHandler(), BattleDialogHandler())


class BattlePackageBusinessHandler(PackageBusinessHandler):
    __slots__ = ()

    def __init__(self):
        listeners = ((VIEW_ALIAS.ACOUSTIC_POPOVER, self.loadViewByCtxEvent), (VIEW_ALIAS.INGAME_MENU, self.__handleIngameMenuEvent), (events.GameEvent.HELP, self.__handleHelpEvent))
        super(BattlePackageBusinessHandler, self).__init__(listeners, APP_NAME_SPACE.SF_BATTLE, EVENT_BUS_SCOPE.BATTLE)

    def __handleIngameMenuEvent(self, event):
        window = self.findViewByAlias(ViewTypes.WINDOW, VIEW_ALIAS.INGAME_MENU)
        if window is not None:
            window.destroy()
        else:
            self.loadViewByCtxEvent(event)
        return

    def __handleHelpEvent(self, _):
        window = self.findViewByAlias(ViewTypes.WINDOW, VIEW_ALIAS.INGAME_HELP)
        if window is not None:
            window.destroy()
        elif self._app is None or not self._app.isModalViewShown():
            self.loadViewWithDefName(VIEW_ALIAS.INGAME_HELP)
        return


class BattleDialogHandler(PackageBusinessHandler):
    __slots__ = ()

    def __init__(self):
        listeners = ((events.ShowDialogEvent.SHOW_DESERTER_DLG, self.__showDeserterDialog),)
        super(BattleDialogHandler, self).__init__(listeners, APP_NAME_SPACE.SF_BATTLE, EVENT_BUS_SCOPE.GLOBAL)

    def __showDeserterDialog(self, event):
        self.loadViewWithGenName(VIEW_ALIAS.INGAME_DESERTER, event.meta, event.handler)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\battle\shared\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:38 St�edn� Evropa (letn� �as)
