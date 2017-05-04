# 2017.05.04 15:24:26 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortClanBattleRoomMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyRoomView import BaseRallyRoomView

class FortClanBattleRoomMeta(BaseRallyRoomView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyRoomView
    """

    def onTimerAlert(self):
        self._printOverrideError('onTimerAlert')

    def openConfigureWindow(self):
        self._printOverrideError('openConfigureWindow')

    def toggleRoomStatus(self):
        self._printOverrideError('toggleRoomStatus')

    def as_updateTeamHeaderTextS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTeamHeaderText(value)

    def as_setBattleRoomDataS(self, data):
        """
        :param data: Represented by FortClanBattleRoomVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setBattleRoomData(data)

    def as_updateReadyStatusS(self, mineValue, enemyValue):
        if self._isDAAPIInited():
            return self.flashObject.as_updateReadyStatus(mineValue, enemyValue)

    def as_setConfigureButtonStateS(self, data):
        """
        :param data: Represented by ActionButtonVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setConfigureButtonState(data)

    def as_setTimerDeltaS(self, data):
        """
        :param data: Represented by ClanBattleTimerVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTimerDelta(data)

    def as_updateDirectionsS(self, data):
        """
        :param data: Represented by ConnectedDirectionsVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateDirections(data)

    def as_setDirectionS(self, value, animationNotAvailable):
        if self._isDAAPIInited():
            return self.flashObject.as_setDirection(value, animationNotAvailable)

    def as_setReservesEnabledS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setReservesEnabled(data)

    def as_setReservesDataS(self, reservesData):
        """
        :param reservesData: Represented by Vector.<DeviceSlotVO> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setReservesData(reservesData)

    def as_setOpenedS(self, buttonLabel, statusLabel, tooltipLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_setOpened(buttonLabel, statusLabel, tooltipLabel)

    def as_setTableHeaderS(self, data):
        """
        :param data: Represented by Vector.<NormalSortingBtnVO> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTableHeader(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\FortClanBattleRoomMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:26 St�edn� Evropa (letn� �as)
