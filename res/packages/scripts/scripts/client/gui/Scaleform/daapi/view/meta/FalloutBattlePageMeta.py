# 2017.05.04 15:24:24 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FalloutBattlePageMeta.py
from gui.Scaleform.daapi.view.battle.classic.page import ClassicPage

class FalloutBattlePageMeta(ClassicPage):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends ClassicPage
    """

    def as_setPostmortemGasAtackInfoS(self, infoStr, respawnStr, showDeadIcon):
        if self._isDAAPIInited():
            return self.flashObject.as_setPostmortemGasAtackInfo(infoStr, respawnStr, showDeadIcon)

    def as_hidePostmortemGasAtackInfoS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hidePostmortemGasAtackInfo()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\FalloutBattlePageMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:24 Støední Evropa (letní èas)
