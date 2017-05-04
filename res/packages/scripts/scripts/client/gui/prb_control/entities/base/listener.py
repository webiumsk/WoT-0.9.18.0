# 2017.05.04 15:21:57 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/prb_control/entities/base/listener.py
from gui.prb_control import prbDispatcherProperty, prbEntityProperty

class IPrbListener(object):
    """
    Base prebattle listener class.
    """

    @prbDispatcherProperty
    def prbDispatcher(self):
        return None

    @prbEntityProperty
    def prbEntity(self):
        return None

    def startPrbListening(self):
        """
        Start prebattle events listening.
        """
        self.prbEntity.addListener(self)

    def stopPrbListening(self):
        """
        Stop prebattle events listening.
        """
        if self.prbEntity is not None:
            self.prbEntity.removeListener(self)
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\base\listener.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:57 Støední Evropa (letní èas)
