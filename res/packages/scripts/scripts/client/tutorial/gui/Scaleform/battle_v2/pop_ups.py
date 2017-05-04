# 2017.05.04 15:27:58 Støední Evropa (letní èas)
# Embedded file name: scripts/client/tutorial/gui/Scaleform/battle_v2/pop_ups.py
from tutorial.gui.Scaleform.pop_ups import TutorialDialog

class ReplenishAmmoDialog(TutorialDialog):

    def _populate(self):
        self.app.enterGuiControlMode(self.uniqueName)
        super(ReplenishAmmoDialog, self)._populate()
        data = self._content
        self.as_setContentS({'title': data['title'],
         'message': data['message'],
         'submitLabel': data['_submitLabel'],
         'align': data['_align'],
         'offsetX': data['_popupOffsetX'],
         'offsetY': data['_popupOffsetY']})

    def _dispose(self):
        self.app.leaveGuiControlMode(self.uniqueName)
        super(ReplenishAmmoDialog, self)._dispose()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\tutorial\gui\Scaleform\battle_v2\pop_ups.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:58 Støední Evropa (letní èas)
