# 2017.05.04 15:27:05 Støední Evropa (letní èas)
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/BaseManageContactViewMeta.py
from messenger.gui.Scaleform.view.lobby.BaseContactView import BaseContactView

class BaseManageContactViewMeta(BaseContactView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseContactView
    """

    def checkText(self, txt):
        self._printOverrideError('checkText')

    def as_setLabelS(self, msg):
        if self._isDAAPIInited():
            return self.flashObject.as_setLabel(msg)

    def as_setInputTextS(self, msg):
        if self._isDAAPIInited():
            return self.flashObject.as_setInputText(msg)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\messenger\gui\Scaleform\meta\BaseManageContactViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:05 Støední Evropa (letní èas)
