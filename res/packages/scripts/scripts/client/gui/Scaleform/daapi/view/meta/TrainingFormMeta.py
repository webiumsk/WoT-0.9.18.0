# 2017.05.04 15:24:40 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TrainingFormMeta.py
from gui.Scaleform.framework.entities.View import View

class TrainingFormMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    """

    def joinTrainingRequest(self, id):
        self._printOverrideError('joinTrainingRequest')

    def createTrainingRequest(self):
        self._printOverrideError('createTrainingRequest')

    def onEscape(self):
        self._printOverrideError('onEscape')

    def onLeave(self):
        self._printOverrideError('onLeave')

    def as_setListS(self, data):
        """
        :param data: Represented by TrainingFormVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setList(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\TrainingFormMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:40 Støední Evropa (letní èas)
