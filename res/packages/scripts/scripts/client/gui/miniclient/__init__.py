# 2017.05.04 15:21:48 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/miniclient/__init__.py
import ResMgr
from constants import CONTENT_TYPE, IS_SANDBOX
from gui.Scaleform.locale.MINICLIENT import MINICLIENT
import contacts as _contacts
import continue_download as _continue_download
import dynamic_squads as _dynamic_squads
import event as _event
import fallout_controller as _fallout_controller
import preview as _preview
import promo_controller as _promo_controller
import shop as _shop
from .fortified_regions import configure_pointcuts as _configure_fort_pointcuts
from .notifications import configure_pointcuts as _notifications_configure_pointcuts
from .invitations import configure_pointcuts as _configure_invitation_pointcuts
from .lobby import configure_pointcuts as _configure_lobby_pointcuts
from .login import configure_pointcuts as _configure_login_pointcuts
from .personal_quests import configure_pointcuts as _configure_personal_quests_pointcuts
from .tech_tree import configure_pointcuts as _configure_tech_tree_pointcuts
from .vehicle_compare import configure_pointcuts as _configure_vehicle_compare_pointcuts

def configure_state():
    content_type = ResMgr.activeContentType()
    is_sandbox = IS_SANDBOX
    is_tutorial = content_type == CONTENT_TYPE.TUTORIAL
    is_miniclient = content_type == CONTENT_TYPE.SANDBOX
    config = _get_config(is_miniclient, is_tutorial, is_sandbox)
    if is_sandbox:
        _enable_sandbox_platform_pointcuts(config)
    elif is_miniclient:
        _enable_all_pointcuts(config)


def _get_config(is_miniclient, is_tutorial, is_sandbox):

    def vehicle_filter(vehicle_item):
        extraCondition = not vehicle_item.isOnlyForEventBattles
        min_vehicle_level = 1
        max_vehicle_level = 10
        if is_miniclient:
            max_vehicle_level = 2
            extraCondition = extraCondition and not vehicle_item.isExcludedFromSandbox
        elif is_tutorial:
            max_vehicle_level = 1
        else:
            extraCondition = True
        if is_sandbox:
            extraCondition = not vehicle_item.isHidden
        return min_vehicle_level <= vehicle_item.level <= max_vehicle_level and extraCondition

    config = {'vehicle_is_available': vehicle_filter}
    if is_sandbox:
        config['sandbox_platform_message'] = MINICLIENT.HANGAR_SABDBOX_PLATFORM_MESSAGE
    return config


def _enable_all_pointcuts(config):
    _shop.OnShopItemWrapPointcut(config)
    _continue_download.OnHyperlinkClickPointcut()
    _continue_download.OnSquadHyperlinkClickPointcut()
    _continue_download.PrepareLibrariesListPointcut()
    _continue_download.OnBrowserHyperlinkClickPointcut()
    _continue_download.OnFailLoadingFramePointcut()
    _contacts.CreateSquadPointcut()
    _configure_lobby_pointcuts(config)
    _configure_login_pointcuts()
    _notifications_configure_pointcuts()
    _configure_fort_pointcuts()
    _configure_tech_tree_pointcuts(config)
    _configure_invitation_pointcuts()
    _configure_personal_quests_pointcuts()
    _dynamic_squads.ParametrizeInitPointcut()
    _dynamic_squads.DisableGameSettingPointcut()
    _dynamic_squads.InviteReceivedMessagePointcut()
    _promo_controller.ShowPromoBrowserPointcut()
    _fallout_controller.InitFalloutPointcut()
    _event.InitEventPointcut()
    _preview.ChangeVehicleIsPreviewAllowed(config)
    _configure_vehicle_compare_pointcuts()


def _enable_sandbox_platform_pointcuts(config):
    from .lobby.header.fight_button_ import DisableFightButtonPointcut
    from .lobby.header.battle_type_selector.pointcuts import CommandBattle
    from .lobby.header.account_popover import MyClanInvitesBtnUnavailable, ClanBtnsUnavailable
    from .lobby.profile.pointcuts import MakeClanBtnUnavailable, MakeClubProfileButtonUnavailable
    from .lobby.tank_carousel import configure_pointcuts as _configure_carousel_pointcuts
    from .lobby.hangar.pointcuts import DisableTankServiceButtons, MaintenanceButtonFlickering, DeviceButtonsFlickering, TankModelHangarVisibility, TankHangarStatus
    from .lobby.profile.pointcuts import MakeClanBtnUnavailable
    DisableFightButtonPointcut(config)
    CommandBattle()
    MakeClanBtnUnavailable()
    ClanBtnsUnavailable()
    MyClanInvitesBtnUnavailable()
    MakeClubProfileButtonUnavailable()
    _shop.OnShopItemWrapPointcut(config)
    DisableTankServiceButtons(config)
    MaintenanceButtonFlickering(config)
    DeviceButtonsFlickering(config)
    TankModelHangarVisibility(config)
    TankHangarStatus(config)
    _configure_carousel_pointcuts(config)
    _preview.ChangeVehicleIsPreviewAllowed(config)


__all__ = ('configure_state',)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\miniclient\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:48 St�edn� Evropa (letn� �as)
