# 2017.05.04 15:24:18 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BrowserMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BrowserMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def browserAction(self, action):
        self._printOverrideError('browserAction')

    def browserMove(self, x, y, z):
        self._printOverrideError('browserMove')

    def browserDown(self, x, y, z):
        self._printOverrideError('browserDown')

    def browserUp(self, x, y, z):
        self._printOverrideError('browserUp')

    def browserFocusOut(self):
        self._printOverrideError('browserFocusOut')

    def onBrowserShow(self, needRefresh):
        self._printOverrideError('onBrowserShow')

    def onBrowserHide(self):
        self._printOverrideError('onBrowserHide')

    def setBrowserSize(self, width, height):
        self._printOverrideError('setBrowserSize')

    def as_loadingStartS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_loadingStart()

    def as_loadingStopS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_loadingStop()

    def as_showServiceViewS(self, header, description):
        if self._isDAAPIInited():
            return self.flashObject.as_showServiceView(header, description)

    def as_hideServiceViewS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideServiceView()

    def as_changeTitleS(self, title):
        if self._isDAAPIInited():
            return self.flashObject.as_changeTitle(title)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BrowserMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:18 St�edn� Evropa (letn� �as)
