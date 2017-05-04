# 2017.05.04 15:24:37 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SendInvitesWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class SendInvitesWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def showError(self, value):
        self._printOverrideError('showError')

    def setOnlineFlag(self, value):
        self._printOverrideError('setOnlineFlag')

    def sendInvites(self, accountsToInvite, comment):
        self._printOverrideError('sendInvites')

    def getAllAvailableContacts(self):
        self._printOverrideError('getAllAvailableContacts')

    def as_onReceiveSendInvitesCooldownS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_onReceiveSendInvitesCooldown(value)

    def as_setDefaultOnlineFlagS(self, onlineFlag):
        if self._isDAAPIInited():
            return self.flashObject.as_setDefaultOnlineFlag(onlineFlag)

    def as_setInvalidUserTagsS(self, tags):
        """
        :param tags: Represented by Vector.<String> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInvalidUserTags(tags)

    def as_setWindowTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setWindowTitle(value)

    def as_onContactUpdatedS(self, contact):
        if self._isDAAPIInited():
            return self.flashObject.as_onContactUpdated(contact)

    def as_onListStateChangedS(self, isEmpty):
        if self._isDAAPIInited():
            return self.flashObject.as_onListStateChanged(isEmpty)

    def as_enableDescriptionS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_enableDescription(isEnabled)

    def as_enableMassSendS(self, isEnabled, addAllTooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_enableMassSend(isEnabled, addAllTooltip)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\SendInvitesWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:37 Støední Evropa (letní èas)
