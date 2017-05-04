# 2017.05.04 15:22:30 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/battle_timers.py
import SoundGroups
from gui.Scaleform.daapi.view.meta.BattleTimerMeta import BattleTimerMeta
from gui.Scaleform.daapi.view.meta.PrebattleTimerMeta import PrebattleTimerMeta
from gui.battle_control.battle_constants import COUNTDOWN_STATE
from helpers import dependency
from helpers import i18n
from skeletons.gui.battle_session import IBattleSessionProvider
from BattleReplay import g_replayCtrl

class _WWISE_EVENTS:
    BATTLE_ENDING_SOON = 'time_buzzer_02'
    COUNTDOWN_TICKING = 'time_countdown'
    BATTLE_END = 'time_over'
    STOP_TICKING = 'time_countdown_stop'


_BATTLE_END_SOUND_TIME = 2
_BATTLE_END_TIME = 0
_STATE_TO_MESSAGE = {COUNTDOWN_STATE.WAIT: i18n.makeString('#ingame_gui:timer/waiting'),
 COUNTDOWN_STATE.START: i18n.makeString('#ingame_gui:timer/starting'),
 COUNTDOWN_STATE.STOP: i18n.makeString('#ingame_gui:timer/started')}

class PreBattleTimer(PrebattleTimerMeta):

    def __init__(self):
        super(PreBattleTimer, self).__init__()

    def setWinConditionText(self, text):
        self.as_setWinConditionTextS(text)

    def setCountdown(self, state, timeLeft):
        self.as_setMessageS(_STATE_TO_MESSAGE[state])
        if state == COUNTDOWN_STATE.WAIT:
            self.as_hideTimerS()
        else:
            self.as_setTimerS(timeLeft)

    def hideCountdown(self, state, speed):
        self.as_setMessageS(_STATE_TO_MESSAGE[state])
        self.as_hideAllS(speed)


class BattleTimer(BattleTimerMeta):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(BattleTimer, self).__init__()
        self.__isTicking = False
        self.__state = COUNTDOWN_STATE.UNDEFINED
        self.__roundLength = self.arenaVisitor.type.getRoundLength()
        self.__endingSoonTime = self._getEndingSoonTime()
        self.__endWarningIsEnabled = self.__checkEndWarningStatus()
        self.__sounds = dict()

    def destroy(self):
        for sound in self.__sounds.values():
            sound.stop()

        self.__sounds.clear()
        super(BattleTimer, self).destroy()

    @property
    def arenaVisitor(self):
        return self.sessionProvider.arenaVisitor

    def setTotalTime(self, totalTime):
        minutes, seconds = divmod(int(totalTime), 60)
        if self.__endWarningIsEnabled and self.__state == COUNTDOWN_STATE.STOP:
            if _BATTLE_END_TIME < totalTime <= self.__endingSoonTime:
                if not self.__isTicking:
                    self.__startTicking()
                if totalTime == self.__endingSoonTime:
                    self._callWWISE(_WWISE_EVENTS.BATTLE_ENDING_SOON)
            elif self.__isTicking:
                self.__stopTicking()
            playBattleEnd = not g_replayCtrl.isPlaying if g_replayCtrl is not None else True
            if totalTime == _BATTLE_END_SOUND_TIME and playBattleEnd:
                self._callWWISE(_WWISE_EVENTS.BATTLE_END)
        self.as_setTotalTimeS('{:02d}'.format(minutes), '{:02d}'.format(seconds))
        return

    def setState(self, state):
        self.__state = state

    def hideTotalTime(self):
        self.as_showBattleTimerS(False)

    def showTotalTime(self):
        self.as_showBattleTimerS(True)

    def _callWWISE(self, wwiseEventName):
        """
        Method is used to play or stop sounds.
        
        Pretected for testing purposes.
        """
        sound = SoundGroups.g_instance.getSound2D(wwiseEventName)
        if sound is not None:
            sound.play()
            self.__sounds[wwiseEventName] = sound
        return

    def _getEndingSoonTime(self):
        return self.arenaVisitor.type.getBattleEndingSoonTime()

    def __startTicking(self):
        self._callWWISE(_WWISE_EVENTS.COUNTDOWN_TICKING)
        self.__isTicking = True
        self.as_setColorS(self.__isTicking)

    def __stopTicking(self):
        self._callWWISE(_WWISE_EVENTS.STOP_TICKING)
        self.__isTicking = False
        self.as_setColorS(self.__isTicking)

    def __validateEndingSoonTime(self):
        return 0 < self.__endingSoonTime < self.__roundLength

    def __checkEndWarningStatus(self):
        endingSoonTimeIsValid = self.__validateEndingSoonTime()
        return self.arenaVisitor.isBattleEndWarningEnabled() and endingSoonTimeIsValid
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\battle\shared\battle_timers.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:30 St�edn� Evropa (letn� �as)
