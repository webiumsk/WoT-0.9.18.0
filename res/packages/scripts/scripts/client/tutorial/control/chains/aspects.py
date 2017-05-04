# 2017.05.04 15:27:47 Støední Evropa (letní èas)
# Embedded file name: scripts/client/tutorial/control/chains/aspects.py
import weakref
from gui.Scaleform.daapi.view.dialogs import DIALOG_BUTTON_ID
from helpers import aop

class SimpleDialogResultAspect(aop.Aspect):

    def __init__(self, trigger):
        super(SimpleDialogResultAspect, self).__init__()
        self._trigger = weakref.proxy(trigger)

    def clear(self):
        self._trigger = None
        super(SimpleDialogResultAspect, self).clear()
        return

    def atCall(self, cd):
        if len(cd.args) > 1:
            _, submitID = cd.args[:2]
            result = submitID == DIALOG_BUTTON_ID.SUBMIT
        else:
            result = False
        self._trigger.setResult(result)


class SimpleDialogClosePointcut(aop.Pointcut):

    def __init__(self):
        super(SimpleDialogClosePointcut, self).__init__('gui.Scaleform.daapi.view.dialogs.SimpleDialog', 'SimpleDialog', '^_SimpleDialog__callHandler$')
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\tutorial\control\chains\aspects.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:47 Støední Evropa (letní èas)
