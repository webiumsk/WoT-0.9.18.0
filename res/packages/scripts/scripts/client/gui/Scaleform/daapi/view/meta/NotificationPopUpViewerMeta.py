# 2017.05.04 15:24:32 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/NotificationPopUpViewerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class NotificationPopUpViewerMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def setListClear(self):
        self._printOverrideError('setListClear')

    def onMessageHidden(self, byTimeout, wasNotified, typeID, entityID):
        self._printOverrideError('onMessageHidden')

    def onClickAction(self, typeID, entityID, action):
        self._printOverrideError('onClickAction')

    def getMessageActualTime(self, msTime):
        self._printOverrideError('getMessageActualTime')

    def as_hasPopUpIndexS(self, typeID, entityID):
        if self._isDAAPIInited():
            return self.flashObject.as_hasPopUpIndex(typeID, entityID)

    def as_appendMessageS(self, data):
        """
        :param data: Represented by PopUpNotificationInfoVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_appendMessage(data)

    def as_updateMessageS(self, data):
        """
        :param data: Represented by PopUpNotificationInfoVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateMessage(data)

    def as_removeMessageS(self, typeID, entityID):
        if self._isDAAPIInited():
            return self.flashObject.as_removeMessage(typeID, entityID)

    def as_removeAllMessagesS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_removeAllMessages()

    def as_initInfoS(self, maxMessagessCount, padding):
        if self._isDAAPIInited():
            return self.flashObject.as_initInfo(maxMessagessCount, padding)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\NotificationPopUpViewerMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:32 Støední Evropa (letní èas)
