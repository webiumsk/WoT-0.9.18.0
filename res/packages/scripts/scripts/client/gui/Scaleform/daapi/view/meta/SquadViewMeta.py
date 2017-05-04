# 2017.05.04 15:24:38 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SquadViewMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyRoomView import BaseRallyRoomView

class SquadViewMeta(BaseRallyRoomView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyRoomView
    """

    def leaveSquad(self):
        self._printOverrideError('leaveSquad')

    def as_updateBattleTypeS(self, data):
        """
        :param data: Represented by SquadViewHeaderVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateBattleType(data)

    def as_isFalloutS(self, isFallout):
        if self._isDAAPIInited():
            return self.flashObject.as_isFallout(isFallout)

    def as_updateInviteBtnStateS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_updateInviteBtnState(isEnabled)

    def as_setCoolDownForReadyButtonS(self, timer):
        if self._isDAAPIInited():
            return self.flashObject.as_setCoolDownForReadyButton(timer)

    def as_setSimpleTeamSectionDataS(self, data):
        """
        :param data: Represented by SimpleSquadTeamSectionVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSimpleTeamSectionData(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\SquadViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:38 Støední Evropa (letní èas)
