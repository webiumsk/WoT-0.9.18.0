# 2017.05.04 15:21:50 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/miniclient/lobby/header/battle_type_selector/pointcuts.py
from helpers import aop
import aspects

class _BattleItemSelector(aop.Pointcut):

    def __init__(self, battleTypeBuilderMethod, aspects_):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.header', 'battle_selector_items', battleTypeBuilderMethod, aspects=aspects_)


class CommandBattle(_BattleItemSelector):

    def __init__(self):
        _BattleItemSelector.__init__(self, '_addCommandBattleType', (aspects.CommandBattle,))


class SortieBattle(_BattleItemSelector):

    def __init__(self):
        _BattleItemSelector.__init__(self, '_addSortieBattleType', (aspects.SortieBattle,))


class TrainingBattle(_BattleItemSelector):

    def __init__(self):
        _BattleItemSelector.__init__(self, '_addTrainingBattleType', (aspects.TrainingBattle,))


class SpecialBattle(_BattleItemSelector):

    def __init__(self):
        _BattleItemSelector.__init__(self, '_addSpecialBattleType', (aspects.SpecialBattle,))


class CompanyBattle(_BattleItemSelector):

    def __init__(self):
        _BattleItemSelector.__init__(self, '_addCompanyBattleType', (aspects.CompanyBattle,))


class FalloutBattle(_BattleItemSelector):

    def __init__(self):
        _BattleItemSelector.__init__(self, '_addFalloutBattleType', (aspects.FalloutBattle,))


class StrongholdBattle(_BattleItemSelector):

    def __init__(self):
        _BattleItemSelector.__init__(self, '_addStrongholdsBattleType', (aspects.StrongholdBattle,))


class OnBattleTypeSelectorPopulate(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.header.BattleTypeSelectPopover', 'BattleTypeSelectPopover', '_populate', aspects=(aspects.OnBattleTypeSelectorPopulate,))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\miniclient\lobby\header\battle_type_selector\pointcuts.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:50 Støední Evropa (letní èas)
