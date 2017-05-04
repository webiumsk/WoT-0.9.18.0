# 2017.05.04 15:28:00 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/tutorial/gui/Scaleform/offbattle/pop_ups.py
from tutorial.gui.Scaleform.meta.TutorialBattleNoResultsMeta import TutorialBattleNoResultsMeta
from tutorial.gui.Scaleform.meta.TutorialBattleStatisticMeta import TutorialBattleStatisticMeta
from tutorial.gui.Scaleform.pop_ups import TutorialDialog, TutorialWindow

class TutorialConfirmRefuseDialog(TutorialDialog):

    def __init__(self, content):
        super(TutorialConfirmRefuseDialog, self).__init__(content)
        self._cache.setStartOnNextLogin(True)
        self._content['doStartOnNextLogin'] = True

    def setStartOnNextLogin(self, value):
        self._cache.setStartOnNextLogin(value)

    def _populate(self):
        super(TutorialConfirmRefuseDialog, self)._populate()
        data = self._content
        self.as_setContentS({'title': data['title'],
         'message': data['message'],
         'checkBoxLabel': data['checkBoxLabel'],
         'doStartOnNextLogin': data['doStartOnNextLogin']})


class TutorialBattleStatisticWindow(TutorialWindow, TutorialBattleStatisticMeta):

    def _populate(self):
        super(TutorialBattleStatisticWindow, self)._populate()
        self.as_setDataS(self._content.copy())

    def restart(self):
        self._onMouseClicked('restartID')

    def showVideoDialog(self):
        self._onMouseClicked('showVideoID')


class TutorialBattleNoResultWindow(TutorialWindow, TutorialBattleNoResultsMeta):

    def _populate(self):
        super(TutorialBattleNoResultWindow, self)._populate()
        self.as_setDataS(self._content.copy())
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\tutorial\gui\Scaleform\offbattle\pop_ups.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:00 St�edn� Evropa (letn� �as)
