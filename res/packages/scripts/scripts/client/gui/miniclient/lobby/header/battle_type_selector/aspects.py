# 2017.05.04 15:21:50 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/miniclient/lobby/header/battle_type_selector/aspects.py
from helpers import aop
from helpers.i18n import makeString as _ms
from gui.Scaleform.locale.MENU import MENU
from gui.shared.formatters import text_styles, icons
from gui.prb_control.settings import PREBATTLE_ACTION_NAME, SELECTOR_BATTLE_TYPES
from gui.Scaleform.daapi.view.lobby.header.battle_selector_items import _DisabledSelectorItem

class _BattleTypeDisable(aop.Aspect):

    def __init__(self, battleTypeAttributes):
        self._battleTypeAttributes = battleTypeAttributes
        aop.Aspect.__init__(self)

    def atCall(self, cd):
        cd.avoid()
        items = cd.args[0]
        items.append(_DisabledSelectorItem(*self._battleTypeAttributes))


class CommandBattle(_BattleTypeDisable):

    def __init__(self):
        _BattleTypeDisable.__init__(self, (MENU.HEADERBUTTONS_BATTLE_TYPES_UNIT,
         PREBATTLE_ACTION_NAME.E_SPORT,
         2,
         SELECTOR_BATTLE_TYPES.UNIT))


class SortieBattle(_BattleTypeDisable):

    def __init__(self):
        _BattleTypeDisable.__init__(self, (MENU.HEADERBUTTONS_BATTLE_TYPES_STRONGHOLDS,
         PREBATTLE_ACTION_NAME.FORT2,
         4,
         SELECTOR_BATTLE_TYPES.SORTIE))


class TrainingBattle(_BattleTypeDisable):

    def __init__(self):
        _BattleTypeDisable.__init__(self, (MENU.HEADERBUTTONS_BATTLE_TYPES_TRAINING, PREBATTLE_ACTION_NAME.TRAININGS_LIST, 6))


class SpecialBattle(_BattleTypeDisable):

    def __init__(self):
        _BattleTypeDisable.__init__(self, (MENU.HEADERBUTTONS_BATTLE_TYPES_SPEC, PREBATTLE_ACTION_NAME.SPEC_BATTLES_LIST, 5))


class CompanyBattle(_BattleTypeDisable):

    def __init__(self):
        _BattleTypeDisable.__init__(self, (MENU.HEADERBUTTONS_BATTLE_TYPES_COMPANY, PREBATTLE_ACTION_NAME.COMPANIES_LIST, 3))


class FalloutBattle(_BattleTypeDisable):

    def __init__(self):
        _BattleTypeDisable.__init__(self, (MENU.HEADERBUTTONS_BATTLE_TYPES_FALLOUT, PREBATTLE_ACTION_NAME.FALLOUT, 2))


class StrongholdBattle(_BattleTypeDisable):

    def __init__(self):
        _BattleTypeDisable.__init__(self, (MENU.HEADERBUTTONS_BATTLE_TYPES_FALLOUT, PREBATTLE_ACTION_NAME.STRONGHOLDS_BATTLES_LIST, 4))


class OnBattleTypeSelectorPopulate(aop.Aspect):

    def atReturn(self, cd):
        cd.self.as_showMiniClientInfoS('{0} {1}'.format(icons.alert(-3), text_styles.main(_ms('#miniclient:battle_type_select_popover/message'))), _ms('#miniclient:personal_quests_welcome_view/continue_download'))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\miniclient\lobby\header\battle_type_selector\aspects.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:50 St�edn� Evropa (letn� �as)
