# 2017.05.04 15:24:16 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BaseRallyRoomViewMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyView import BaseRallyView

class BaseRallyRoomViewMeta(BaseRallyView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyView
    """

    def assignSlotRequest(self, slotIndex, playerId):
        self._printOverrideError('assignSlotRequest')

    def leaveSlotRequest(self, playerId):
        self._printOverrideError('leaveSlotRequest')

    def onSlotsHighlihgtingNeed(self, databaseID):
        self._printOverrideError('onSlotsHighlihgtingNeed')

    def chooseVehicleRequest(self):
        self._printOverrideError('chooseVehicleRequest')

    def inviteFriendRequest(self):
        self._printOverrideError('inviteFriendRequest')

    def toggleReadyStateRequest(self):
        self._printOverrideError('toggleReadyStateRequest')

    def ignoreUserRequest(self, slotIndex):
        self._printOverrideError('ignoreUserRequest')

    def editDescriptionRequest(self, description):
        self._printOverrideError('editDescriptionRequest')

    def showFAQWindow(self):
        self._printOverrideError('showFAQWindow')

    def as_updateRallyS(self, rally):
        """
        :param rally: Represented by IRallyVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateRally(rally)

    def as_setMembersS(self, hasRestrictions, slots):
        if self._isDAAPIInited():
            return self.flashObject.as_setMembers(hasRestrictions, slots)

    def as_setMemberStatusS(self, slotIndex, status):
        if self._isDAAPIInited():
            return self.flashObject.as_setMemberStatus(slotIndex, status)

    def as_setMemberOfflineS(self, slotIndex, isOffline):
        if self._isDAAPIInited():
            return self.flashObject.as_setMemberOffline(slotIndex, isOffline)

    def as_setMemberVehicleS(self, slotIdx, slotCost, veh):
        """
        :param veh: Represented by VehicleVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMemberVehicle(slotIdx, slotCost, veh)

    def as_setActionButtonStateS(self, data):
        """
        :param data: Represented by ActionButtonVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setActionButtonState(data)

    def as_setCommentS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setComment(value)

    def as_getCandidatesDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getCandidatesDP()

    def as_highlightSlotsS(self, slotsIdx):
        if self._isDAAPIInited():
            return self.flashObject.as_highlightSlots(slotsIdx)

    def as_setVehiclesTitleS(self, value, tooltip):
        """
        :param tooltip: Represented by TooltipDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setVehiclesTitle(value, tooltip)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BaseRallyRoomViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:17 St�edn� Evropa (letn� �as)
