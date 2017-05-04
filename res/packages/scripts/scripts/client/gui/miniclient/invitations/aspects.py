# 2017.05.04 15:21:49 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/miniclient/invitations/aspects.py
from gui import makeHtmlString
from helpers import aop
from helpers.i18n import makeString as _ms
from constants import PREBATTLE_TYPE_NAMES
from notification.settings import NOTIFICATION_BUTTON_STATE

class DisableAccept(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        return False


class InvitationNote(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        battle_type = PREBATTLE_TYPE_NAMES[cd.args[0].type]
        return makeHtmlString('html_templates:lobby/prebattle', 'inviteNote', {'note': _ms('#miniclient:invitation/note/{0}'.format(battle_type))})


class DisableAcceptButton(aop.Aspect):

    def atReturn(self, cd):
        original_return_value = cd.returned
        original_buttons = original_return_value['message']['buttonsStates']
        original_buttons['submit'] = original_buttons['submit'] & ~NOTIFICATION_BUTTON_STATE.ENABLED
        return original_return_value
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\miniclient\invitations\aspects.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:49 Støední Evropa (letní èas)
