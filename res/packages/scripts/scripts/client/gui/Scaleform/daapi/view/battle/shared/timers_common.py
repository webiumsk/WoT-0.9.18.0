# 2017.05.04 15:22:37 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/timers_common.py
import BigWorld
from gui.shared.utils.TimeInterval import TimeInterval

class TimerComponent(object):
    __slots__ = ('_panel', '_typeID', '_viewID', '_totalTime', '_startTime', '_finishTime')

    def __init__(self, panel, typeID, viewID, totalTime):
        super(TimerComponent, self).__init__()
        self._panel = panel
        self._typeID = typeID
        self._viewID = viewID
        self._totalTime = totalTime
        self._startTime = BigWorld.serverTime()
        self._finishTime = self._startTime + totalTime if totalTime else 0

    def __repr__(self):
        return 'TimerComponent(typeID = {}, viewID = {}, totalTime = {})'.format(self._typeID, self._viewID, self._totalTime)

    def clear(self):
        self._panel = None
        return

    def show(self, isBubble = True):
        self._showView(isBubble)
        self._startTick()

    def hide(self):
        self._stopTick()
        self._hideView()

    @property
    def typeID(self):
        return self._typeID

    @property
    def viewID(self):
        return self._viewID

    @property
    def finishTime(self):
        return self._finishTime

    @property
    def totalTime(self):
        return self._totalTime

    def _startTick(self):
        raise NotImplementedError

    def _stopTick(self):
        raise NotImplementedError

    def _hideView(self):
        raise NotImplementedError

    def _showView(self, isBubble):
        raise NotImplementedError


class PythonTimer(TimerComponent):
    __slots__ = ('_timeInterval', '__weakref__')

    def __init__(self, panel, typeID, viewID, totalTime):
        super(PythonTimer, self).__init__(panel, typeID, viewID, totalTime)
        self._timeInterval = TimeInterval(1.0, self, '_tick')

    def clear(self):
        self._timeInterval.stop()
        super(PythonTimer, self).clear()

    def _startTick(self):
        if self._totalTime:
            timeLeft = max(0, self._finishTime - BigWorld.serverTime())
            if timeLeft:
                self._setViewSnapshot(timeLeft)
                self._timeInterval.start()

    def _stopTick(self):
        self._timeInterval.stop()

    def _tick(self):
        timeLeft = self._finishTime - BigWorld.serverTime()
        if timeLeft >= 0:
            self._setViewSnapshot(timeLeft)
        else:
            self.hide()

    def _setViewSnapshot(self, timeLeft):
        raise NotImplementedError
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\battle\shared\timers_common.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:37 St�edn� Evropa (letn� �as)
