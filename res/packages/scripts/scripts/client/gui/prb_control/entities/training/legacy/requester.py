# 2017.05.04 15:22:16 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/prb_control/entities/training/legacy/requester.py
import BigWorld
from PlayerEvents import g_playerEvents
from constants import PREBATTLE_TYPE, PREBATTLE_CACHE_KEY
from debug_utils import LOG_ERROR
from gui.prb_control.entities.base.requester import IPrbListRequester
from gui.prb_control.items import prb_seqs

class TrainingListRequester(IPrbListRequester):
    """
    Trainings list requests
    """
    UPDATE_LIST_TIMEOUT = 5

    def __init__(self):
        super(TrainingListRequester, self).__init__()
        self.__callbackID = None
        self.__callback = None
        return

    def start(self, callback):
        if self.__callbackID is not None:
            LOG_ERROR('TrainingListRequester already started')
            return
        else:
            if callback is not None and callable(callback):
                g_playerEvents.onPrebattlesListReceived += self.__pe_onPrebattlesListReceived
                self.__callback = callback
                self.__request()
            else:
                LOG_ERROR('Callback is None or is not callable')
                return
            return

    def stop(self):
        g_playerEvents.onPrebattlesListReceived -= self.__pe_onPrebattlesListReceived
        self.__callback = None
        if self.__callbackID is not None:
            BigWorld.cancelCallback(self.__callbackID)
            self.__callbackID = None
        return

    def request(self, ctx = None):
        self.__request()

    def __request(self):
        """
        Send request to get list of trainings available
        """
        self.__callbackID = None
        if hasattr(BigWorld.player(), 'requestPrebattles'):
            BigWorld.player().requestPrebattles(PREBATTLE_TYPE.TRAINING, PREBATTLE_CACHE_KEY.CREATE_TIME, False, 0, 50)
        return

    def __setTimeout(self):
        """
        Sets operations timeout
        """
        self.__callbackID = BigWorld.callback(self.UPDATE_LIST_TIMEOUT, self.__request)

    def __pe_onPrebattlesListReceived(self, prbType, count, prebattles):
        """
        Listener for event of trainings list receive
        Args:
            prbType: items prebattle type
            count: items count
            prebattles: items, which are list of (sort key, prebattle ID, prebattle cache data like
                PREBATTLE_CACHE_KEY -> data
        """
        if prbType != PREBATTLE_TYPE.TRAINING:
            return
        self.__callback(prb_seqs.PrbListIterator(prebattles))
        self.__setTimeout()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\training\legacy\requester.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:16 St�edn� Evropa (letn� �as)
