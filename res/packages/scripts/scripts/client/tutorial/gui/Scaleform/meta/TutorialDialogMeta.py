# 2017.05.04 15:28:00 Støední Evropa (letní èas)
# Embedded file name: scripts/client/tutorial/gui/Scaleform/meta/TutorialDialogMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class TutorialDialogMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def submit(self):
        """
        :return :
        """
        self._printOverrideError('submit')

    def cancel(self):
        """
        :return :
        """
        self._printOverrideError('cancel')

    def as_setContentS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setContent(data)

    def as_updateContentS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateContent(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\tutorial\gui\Scaleform\meta\TutorialDialogMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:00 Støední Evropa (letní èas)
