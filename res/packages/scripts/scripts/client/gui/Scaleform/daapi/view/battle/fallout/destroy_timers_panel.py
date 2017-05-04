# 2017.05.04 15:22:27 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/fallout/destroy_timers_panel.py
from constants import DEATH_ZONES
from gui.Scaleform.daapi.view.battle.shared import destroy_times_mapping as _mapping
from gui.Scaleform.daapi.view.meta.FalloutDestroyTimersPanelMeta import FalloutDestroyTimersPanelMeta
from gui.Scaleform.genConsts.BATTLE_DESTROY_TIMER_STATES import BATTLE_DESTROY_TIMER_STATES

class FalloutDestroyTimersPanel(FalloutDestroyTimersPanelMeta):

    def __init__(self):
        deathZonesCodes = _mapping.getDefaultDeathZonesCodes()
        deathZonesCodes[DEATH_ZONES.GAS_ATTACK] = BATTLE_DESTROY_TIMER_STATES.GAS_ATTACK
        deathZonesSoundIDs = {(DEATH_ZONES.GAS_ATTACK, 'warning'): 'fallout_gaz_sphere_warning',
         (DEATH_ZONES.GAS_ATTACK, 'critical'): 'fallout_gaz_sphere_timer'}
        super(FalloutDestroyTimersPanel, self).__init__(mapping=_mapping.FrontendMapping(deathZonesCodes=deathZonesCodes, deathZonesSoundIDs=deathZonesSoundIDs))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\battle\fallout\destroy_timers_panel.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:27 St�edn� Evropa (letn� �as)
