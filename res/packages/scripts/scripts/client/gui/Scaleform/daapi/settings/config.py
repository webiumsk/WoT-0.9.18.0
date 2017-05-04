# 2017.05.04 15:22:23 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/settings/config.py
from constants import HAS_DEV_RESOURCES, ARENA_GUI_TYPE
_COMMON_RELEASE_PACKAGES = ('gui.Scaleform.daapi.view.common',)
_COMMON_DEBUG_PACKAGES = ('gui.development.ui.GUIEditor',)
_LOBBY_RELEASE_PACKAGES = ('gui.Scaleform.daapi.view.lobby', 'gui.Scaleform.daapi.view.lobby.barracks', 'gui.Scaleform.daapi.view.lobby.boosters', 'gui.Scaleform.daapi.view.lobby.clans', 'gui.Scaleform.daapi.view.lobby.crewOperations', 'gui.Scaleform.daapi.view.lobby.customization', 'gui.Scaleform.daapi.view.lobby.cyberSport', 'gui.Scaleform.daapi.view.lobby.exchange', 'gui.Scaleform.daapi.view.lobby.fortifications', 'gui.Scaleform.daapi.view.lobby.hangar', 'gui.Scaleform.daapi.view.lobby.header', 'gui.Scaleform.daapi.view.lobby.inputChecker', 'gui.Scaleform.daapi.view.lobby.messengerBar', 'gui.Scaleform.daapi.view.lobby.prb_windows', 'gui.Scaleform.daapi.view.lobby.profile', 'gui.Scaleform.daapi.view.lobby.server_events', 'gui.Scaleform.daapi.view.lobby.store', 'gui.Scaleform.daapi.view.lobby.techtree', 'gui.Scaleform.daapi.view.lobby.trainings', 'gui.Scaleform.daapi.view.lobby.vehiclePreview', 'gui.Scaleform.daapi.view.lobby.vehicle_compare', 'gui.Scaleform.daapi.view.lobby.wgnc', 'gui.Scaleform.daapi.view.login', 'messenger.gui.Scaleform.view.lobby')
_LOBBY_DEBUG_PACKAGES = ('gui.development.ui.messenger.view.lobby',)
_BATTLE_RELEASE_PACKAGES = ('gui.Scaleform.daapi.view.battle.shared', 'messenger.gui.Scaleform.view.battle')
_BATTLE_DEBUG_PACKAGES = ('gui.development.ui.battle',)
LOBBY_PACKAGES = _LOBBY_RELEASE_PACKAGES
BATTLE_PACKAGES = _BATTLE_RELEASE_PACKAGES
COMMON_PACKAGES = _COMMON_RELEASE_PACKAGES
BATTLE_PACKAGES_BY_ARENA_TYPE = {ARENA_GUI_TYPE.FALLOUT_CLASSIC: ('gui.Scaleform.daapi.view.battle.fallout',),
 ARENA_GUI_TYPE.FALLOUT_MULTITEAM: ('gui.Scaleform.daapi.view.battle.fallout',),
 ARENA_GUI_TYPE.TUTORIAL: ('gui.Scaleform.daapi.view.battle.tutorial',),
 ARENA_GUI_TYPE.EVENT_BATTLES: ('gui.Scaleform.daapi.view.battle.event',)}
BATTLE_PACKAGES_BY_DEFAULT = ('gui.Scaleform.daapi.view.battle.classic',)
if HAS_DEV_RESOURCES:
    LOBBY_PACKAGES += _LOBBY_DEBUG_PACKAGES
    BATTLE_PACKAGES += _BATTLE_DEBUG_PACKAGES
    COMMON_PACKAGES += _COMMON_DEBUG_PACKAGES
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\settings\config.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:23 St�edn� Evropa (letn� �as)
