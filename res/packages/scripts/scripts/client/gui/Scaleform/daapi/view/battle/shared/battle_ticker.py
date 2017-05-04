# 2017.05.04 15:22:30 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/battle_ticker.py
from gui.Scaleform.daapi.view.common.BaseTicker import BaseTicker

class BattleTicker(BaseTicker):

    def __init__(self):
        super(BattleTicker, self).__init__()

    def _handleBrowserLink(self, link):
        """
        Battle ticker should not display a browser, so we will do nothing
        :param link: link to show
        """
        pass
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\battle\shared\battle_ticker.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:30 Støední Evropa (letní èas)
