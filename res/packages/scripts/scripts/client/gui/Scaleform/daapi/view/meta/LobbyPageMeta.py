# 2017.05.04 15:24:31 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/LobbyPageMeta.py
from gui.Scaleform.framework.entities.View import View

class LobbyPageMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    """

    def moveSpace(self, x, y, delta):
        self._printOverrideError('moveSpace')

    def getSubContainerType(self):
        self._printOverrideError('getSubContainerType')

    def notifyCursorOver3dScene(self, isOver3dScene):
        self._printOverrideError('notifyCursorOver3dScene')

    def as_showHelpLayoutS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showHelpLayout()

    def as_closeHelpLayoutS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_closeHelpLayout()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\LobbyPageMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:31 Støední Evropa (letní èas)
