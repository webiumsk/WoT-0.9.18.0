# 2017.05.04 15:21:51 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/miniclient/personal_quests/aspects.py
from gui.shared.formatters import text_styles
from helpers import aop
from helpers.i18n import makeString as _ms
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES

class OnViewPopulate(aop.Aspect):

    def atReturn(self, cd):
        cd.self.as_showMiniClientInfoS(text_styles.alert(_ms('#miniclient:personal_quests_welcome_view/description')), _ms('#miniclient:personal_quests_welcome_view/continue_download'))


class PersonalQuestsTabSelect(aop.Aspect):

    def atCall(self, cd):
        if cd.args[0] == QUESTS_ALIASES.TAB_PERSONAL_QUESTS:
            cd.avoid()
            cd.self._showWelcomeView()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\miniclient\personal_quests\aspects.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:51 Støední Evropa (letní èas)
