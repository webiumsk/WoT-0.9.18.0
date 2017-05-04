# 2017.05.04 15:24:31 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/IntroPageMeta.py
from gui.Scaleform.framework.entities.View import View

class IntroPageMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    """

    def stopVideo(self):
        self._printOverrideError('stopVideo')

    def handleError(self, data):
        self._printOverrideError('handleError')

    def as_playVideoS(self, data):
        """
        :param data: Represented by IntroInfoVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_playVideo(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\IntroPageMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:31 Støední Evropa (letní èas)
