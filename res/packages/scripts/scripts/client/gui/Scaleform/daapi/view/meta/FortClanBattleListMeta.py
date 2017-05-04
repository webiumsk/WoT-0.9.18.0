# 2017.05.04 15:24:26 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortClanBattleListMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyListView import BaseRallyListView

class FortClanBattleListMeta(BaseRallyListView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyListView
    """

    def as_setClanBattleDataS(self, data):
        """
        :param data: Represented by ClanBattleListVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClanBattleData(data)

    def as_upateClanBattlesCountS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_upateClanBattlesCount(value)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\FortClanBattleListMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:26 Støední Evropa (letní èas)
