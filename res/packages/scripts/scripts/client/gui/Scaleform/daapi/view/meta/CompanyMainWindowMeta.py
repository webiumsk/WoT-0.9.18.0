# 2017.05.04 15:24:21 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CompanyMainWindowMeta.py
from gui.Scaleform.daapi.view.lobby.rally.AbstractRallyWindow import AbstractRallyWindow

class CompanyMainWindowMeta(AbstractRallyWindow):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractRallyWindow
    """

    def getCompanyName(self):
        self._printOverrideError('getCompanyName')

    def showFAQWindow(self):
        self._printOverrideError('showFAQWindow')

    def getClientID(self):
        self._printOverrideError('getClientID')

    def as_setWindowTitleS(self, title, icon):
        if self._isDAAPIInited():
            return self.flashObject.as_setWindowTitle(title, icon)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\CompanyMainWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:21 Støední Evropa (letní èas)
