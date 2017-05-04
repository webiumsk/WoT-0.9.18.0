# 2017.05.04 15:22:33 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/debug_panel.py
from gui.Scaleform.daapi.view.meta.DebugPanelMeta import DebugPanelMeta
from gui.battle_control.controllers.debug_ctrl import IDebugPanel

class DebugPanel(DebugPanelMeta, IDebugPanel):

    def __init__(self):
        super(DebugPanel, self).__init__()
        self._fps = 0
        self._ping = 0
        self._isLaggingNow = False

    def updateDebugInfo(self, ping, fps, isLaggingNow, fpsReplay = -1):
        if fpsReplay > 0:
            fps = '{0}({1})'.format(fpsReplay, fps)
        else:
            fps = str(fps)
        if self._isLaggingNow != isLaggingNow:
            self.as_updatePingFPSLagInfoS(ping, fps, isLaggingNow)
        else:
            self.as_updatePingFPSInfoS(ping, fps)
        self._ping, self._fps, self._isLaggingNow = ping, fps, isLaggingNow
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\battle\shared\debug_panel.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:33 Støední Evropa (letní èas)
