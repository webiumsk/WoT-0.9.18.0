# 2017.05.04 15:21:26 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/battle_results/templates/fallout.py
from gui.battle_results.components import base
from gui.battle_results.components import common
from gui.battle_results.components import personal
from gui.battle_results.components import shared
from gui.battle_results.templates import regular
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
regular.FINISH_RESULT_VO_META.bind(common.FalloutFinishResultBlock)
FALLOUT_COMMON_STATS_BLOCK = regular.REGULAR_COMMON_STATS_BLOCK.clone(0, 3, 7, 9, 10)
FALLOUT_COMMON_STATS_BLOCK.addComponent(0, shared.FalloutSortingBlock())
FALLOUT_COMMON_STATS_BLOCK.addComponent(3, common.FalloutArenaFullNameItem('arenaStr'))
FALLOUT_COMMON_STATS_BLOCK.addComponent(7, common.FalloutFinishResultBlock())
FALLOUT_COMMON_STATS_BLOCK.addComponent(9, personal.PersonalVehicleNamesBlock(base.ListMeta(), 'playerVehicleNames'))
FALLOUT_COMMON_STATS_BLOCK.addComponent(10, personal.FalloutVehiclesBlock(base.ListMeta(), 'playerVehicles', _RECORD.PERSONAL))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\battle_results\templates\fallout.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:26 Støední Evropa (letní èas)
