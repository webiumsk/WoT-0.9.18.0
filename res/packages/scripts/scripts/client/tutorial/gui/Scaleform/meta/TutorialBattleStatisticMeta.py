# 2017.05.04 15:28:00 Støední Evropa (letní èas)
# Embedded file name: scripts/client/tutorial/gui/Scaleform/meta/TutorialBattleStatisticMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class TutorialBattleStatisticMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def restart(self):
        self._printOverrideError('restart')

    def showVideoDialog(self):
        self._printOverrideError('showVideoDialog')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\tutorial\gui\Scaleform\meta\TutorialBattleStatisticMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:00 Støední Evropa (letní èas)
