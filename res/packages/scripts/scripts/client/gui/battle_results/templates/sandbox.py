# 2017.05.04 15:21:26 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/battle_results/templates/sandbox.py
from gui.battle_results.components import base
from gui.battle_results.components import personal
from gui.battle_results.components import shared
from gui.battle_results.templates import regular
_SANDBOX_NO_INCOME_ALERT_VO_META = base.PropertyMeta((('icon', '', 'icon'), ('text', '', 'text')))
_SANDBOX_NO_INCOME_ALERT_VO_META.bind(personal.SandboxNoIncomeAlert)
SANDBOX_PERSONAL_STATS_BLOCK = regular.REGULAR_PERSONAL_STATS_BLOCK.clone()
SANDBOX_PERSONAL_STATS_BLOCK.addComponent(17, shared.TrueFlag('showNoIncomeAlert'))
SANDBOX_PERSONAL_STATS_BLOCK.addComponent(18, personal.SandboxNoIncomeAlert(field='noIncomeAlert'))
SANDBOX_TEAM_ITEM_STATS_ENABLE = shared.FalseFlag('closingTeamMemberStatsEnabled')
SANDBOX_PERSONAL_ACCOUNT_DB_ID = personal.PersonalAccountDBID('selectedTeamMemberId')
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\battle_results\templates\sandbox.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:26 St�edn� Evropa (letn� �as)
