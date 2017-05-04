# 2017.05.04 15:24:22 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ContactsTreeComponentMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ContactsTreeComponentMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def onGroupSelected(self, mainGroup, groupData):
        self._printOverrideError('onGroupSelected')

    def searchLocalContact(self, flt):
        self._printOverrideError('searchLocalContact')

    def hasDisplayingContacts(self):
        self._printOverrideError('hasDisplayingContacts')

    def as_updateInfoMessageS(self, enableSearchInput, title, message, warn):
        if self._isDAAPIInited():
            return self.flashObject.as_updateInfoMessage(enableSearchInput, title, message, warn)

    def as_getMainDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getMainDP()

    def as_setInitDataS(self, val):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(val)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\ContactsTreeComponentMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:22 Støední Evropa (letní èas)
