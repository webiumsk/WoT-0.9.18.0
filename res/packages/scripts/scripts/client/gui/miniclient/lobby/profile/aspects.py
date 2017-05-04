# 2017.05.04 15:21:50 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/miniclient/lobby/profile/aspects.py
from gui.Scaleform.locale.MINICLIENT import MINICLIENT
from gui.shared.utils.functions import makeTooltip
from helpers import aop

class MakeClanBtnUnavailable(aop.Aspect):

    def __init__(self, config = {}):
        self.__config = config
        aop.Aspect.__init__(self)

    def atReturn(self, cd):
        original_return_value = cd.returned
        original_return_value['btnEnabled'] = False
        original_return_value['btnTooltip'] = makeTooltip(None, None, None, self.__config.get('sandbox_platform_message', MINICLIENT.ACCOUNTPOPOVER_WARNING))
        return original_return_value


class MakeClubProfileButtonUnavailable(aop.Aspect):

    def atCall(self, cd):
        cd.change()
        return ([False], {})
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\miniclient\lobby\profile\aspects.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:50 Støední Evropa (letní èas)
