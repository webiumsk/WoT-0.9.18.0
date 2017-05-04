# 2017.05.04 15:24:34 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/QuestRecruitWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class QuestRecruitWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def onApply(self, data):
        self._printOverrideError('onApply')

    def as_setInitDataS(self, data):
        """
        :param data: Represented by TankmanCardVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\QuestRecruitWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:34 Støední Evropa (letní èas)
