# 2017.05.04 15:24:32 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/NotificationsListMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class NotificationsListMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    """

    def onClickAction(self, typeID, entityID, action):
        self._printOverrideError('onClickAction')

    def getMessageActualTime(self, msTime):
        self._printOverrideError('getMessageActualTime')

    def onGroupChange(self, groupIdx):
        self._printOverrideError('onGroupChange')

    def as_setInitDataS(self, value):
        """
        :param value: Represented by NotificationViewInitVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(value)

    def as_setMessagesListS(self, value):
        """
        :param value: Represented by NotificationMessagesListVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMessagesList(value)

    def as_appendMessageS(self, messageData):
        """
        :param messageData: Represented by NotificationInfoVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_appendMessage(messageData)

    def as_updateMessageS(self, messageData):
        """
        :param messageData: Represented by NotificationInfoVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateMessage(messageData)

    def as_updateCountersS(self, counts):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCounters(counts)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\NotificationsListMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:32 St�edn� Evropa (letn� �as)
