# 2017.05.04 15:24:27 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortificationsViewMeta.py
from gui.Scaleform.framework.entities.View import View

class FortificationsViewMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    """

    def onFortCreateClick(self):
        self._printOverrideError('onFortCreateClick')

    def onDirectionCreateClick(self):
        self._printOverrideError('onDirectionCreateClick')

    def onEscapePress(self):
        self._printOverrideError('onEscapePress')

    def as_loadViewS(self, flashAlias, pyAlias):
        if self._isDAAPIInited():
            return self.flashObject.as_loadView(flashAlias, pyAlias)

    def as_setCommonDataS(self, data):
        """
        :param data: Represented by FortificationVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCommonData(data)

    def as_waitingDataS(self, data):
        """
        :param data: Represented by FortWaitingVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_waitingData(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\FortificationsViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:27 Støední Evropa (letní èas)
