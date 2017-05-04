# 2017.05.04 15:28:51 Støední Evropa (letní èas)
# Embedded file name: scripts/common/dossiers2/custom/fort_layout.py
from dossiers2.common.DossierBlockBuilders import *
_fortTotalBlockLayout = ['creationTime', 'production', 'reservedInt32']
_fortTotalBlockBuilder = StaticSizeBlockBuilder('total', _fortTotalBlockLayout, {}, [])
_fortBattlesBlockLayout = ['battlesCount',
 'reservedInt32',
 'attackCount',
 'defenceCount',
 'enemyBaseCaptureCount',
 'ownBaseLossCount',
 'combatCount',
 'combatWins',
 'successDefenceCount',
 'successAttackCount',
 'captureEnemyBuildingTotalCount',
 'lossOwnBuildingTotalCount',
 'resourceCaptureCount',
 'resourceLossCount']
_fortBattlesBlockBuilder = StaticSizeBlockBuilder('fortBattles', _fortBattlesBlockLayout, {}, [])
_fortSortiesBlockLayout = ['battlesCount',
 'wins',
 'losses',
 'middleBattlesCount',
 'championBattlesCount',
 'absoluteBattlesCount',
 'fortResourceInMiddle',
 'fortResourceInChampion',
 'fortResourceInAbsolute',
 'middleWins',
 'championWins',
 'absoluteWins']
_fortSortiesBlockBuilder = StaticSizeBlockBuilder('fortSorties', _fortSortiesBlockLayout, {}, [])
_fortAchievementsBlockLayout = ['citadel']
_fortAchievementsPopUps = ['citadel']
_fortAchievementsBlockBuilder = StaticSizeBlockBuilder('achievements', _fortAchievementsBlockLayout, {}, _fortAchievementsPopUps)
fortDossierLayout = (_fortTotalBlockBuilder,
 _fortBattlesBlockBuilder,
 _fortSortiesBlockBuilder,
 _fortAchievementsBlockBuilder)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\dossiers2\custom\fort_layout.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:51 Støední Evropa (letní èas)
