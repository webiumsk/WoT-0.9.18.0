# 2017.05.04 15:21:49 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/miniclient/lobby/header/account_popover.py
from gui.Scaleform.locale.MINICLIENT import MINICLIENT
from gui.shared.utils.functions import makeTooltip
from helpers import aop
from helpers.i18n import makeString as _ms

class ClanBtnsUnavailableAspect(aop.Aspect):

    def __init__(self, config = {}):
        self.__config = config
        aop.Aspect.__init__(self)

    def atReturn(self, cd):
        original_return_value = cd.returned
        warnTooltip = makeTooltip(None, None, None, self.__config.get('sandbox_platform_message', MINICLIENT.ACCOUNTPOPOVER_WARNING))
        original_return_value['btnTooltip'] = warnTooltip
        original_return_value['requestInviteBtnTooltip'] = warnTooltip
        original_return_value['searchClanTooltip'] = warnTooltip
        original_return_value['isOpenInviteBtnEnabled'] = False
        original_return_value['isSearchClanBtnEnabled'] = False
        original_return_value['btnEnabled'] = False
        return original_return_value


class MyClanInvitesBtnUnavailableAspect(aop.Aspect):

    def __init__(self, config = {}):
        self.__config = config
        aop.Aspect.__init__(self)

    def atReturn(self, cd):
        original_return_value = cd.returned
        original_return_value['inviteBtnTooltip'] = makeTooltip(None, None, None, self.__config.get('sandbox_platform_message', MINICLIENT.ACCOUNTPOPOVER_WARNING))
        original_return_value['inviteBtnEnabled'] = False
        return original_return_value


class ClanBtnsUnavailable(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.header.AccountPopover', 'AccountPopover', '_getClanBtnsParams', aspects=(ClanBtnsUnavailableAspect,))


class MyClanInvitesBtnUnavailable(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.header.AccountPopover', 'AccountPopover', '_getMyInvitesBtnParams', aspects=(MyClanInvitesBtnUnavailableAspect,))


class CrewButtonStatusAspect(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        return {'isEnabled': False,
         'disabledTooltip': makeTooltip(attention='#menu:header/account/popover/crewButton/disabledTooltip')}


class CrewButtonStatusPointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.header.AccountPopover', 'AccountPopover', '_crewDataButtonStatus', aspects=(CrewButtonStatusAspect,))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\miniclient\lobby\header\account_popover.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:50 St�edn� Evropa (letn� �as)
