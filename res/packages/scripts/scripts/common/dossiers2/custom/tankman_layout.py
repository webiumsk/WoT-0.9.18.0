# 2017.05.04 15:29:02 Støední Evropa (letní èas)
# Embedded file name: scripts/common/dossiers2/custom/tankman_layout.py
from dossiers2.common.DossierBlockBuilders import *
_tmanTotalBlockLayout = ['battlesCount']
_tmanTotalBlockBuilder = StaticSizeBlockBuilder('total', _tmanTotalBlockLayout, {}, [])
TMAN_ACHIEVEMENTS_BLOCK_LAYOUT = ['warrior',
 'invader',
 'sniper',
 'defender',
 'steelwall',
 'supporter',
 'scout',
 'evileye',
 'medalWittmann',
 'medalOrlik',
 'medalOskin',
 'medalHalonen',
 'medalBurda',
 'medalBillotte',
 'medalKolobanov',
 'medalFadin',
 'medalRadleyWalters',
 'medalBrunoPietro',
 'medalTarczay',
 'medalPascucci',
 'medalDumitru',
 'medalLehvaslaiho',
 'medalNikolas',
 'medalLafayettePool',
 'heroesOfRassenay',
 'medalDeLanglade',
 'medalTamadaYoshio',
 'huntsman',
 'sniper2',
 'mainGun']
_tankmanAchievementsBlockBuilder = StaticSizeBlockBuilder('achievements', TMAN_ACHIEVEMENTS_BLOCK_LAYOUT, {}, [])
tmanDossierLayout = (_tmanTotalBlockBuilder, _tankmanAchievementsBlockBuilder)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\dossiers2\custom\tankman_layout.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:29:02 Støední Evropa (letní èas)
