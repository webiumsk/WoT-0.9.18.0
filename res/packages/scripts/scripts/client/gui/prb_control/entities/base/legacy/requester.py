# 2017.05.04 15:21:59 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/prb_control/entities/base/legacy/requester.py
import BigWorld
from PlayerEvents import g_playerEvents
from debug_utils import LOG_ERROR
from gui.prb_control.entities.base.requester import IPrbListRequester
from gui.prb_control.items.prb_seqs import RosterIterator

class LegacyRosterRequester(IPrbListRequester):
    """
    Legacy entity roster requester.
    """

    def __init__(self):
        self.__callback = None
        self.__prebattleID = 0
        self.__ctx = None
        return

    def start(self, callback):
        if callback is not None and callable(callback):
            self.__callback = callback
        else:
            LOG_ERROR('Callback is None or is not callable')
            return
        g_playerEvents.onPrebattleRosterReceived += self.__pe_onPrebattleRosterReceived
        return

    def stop(self):
        g_playerEvents.onPrebattleRosterReceived -= self.__pe_onPrebattleRosterReceived
        self.__callback = None
        if self.__ctx:
            self.__ctx.stopProcessing(False)
            self.__ctx = None
        return

    def request(self, ctx = None):
        self.__ctx = ctx
        BigWorld.player().requestPrebattleRoster(self.__ctx.getPrbID())

    def __pe_onPrebattleRosterReceived(self, prebattleID, roster):
        """
        Roster received event listener.
        Args:
            prebattleID: prebattle ID for which we've received roster
            roster: roster data
        """
        self.__callback(prebattleID, RosterIterator(roster))
        if self.__ctx:
            self.__ctx.stopProcessing(True)
            self.__ctx = None
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\base\legacy\requester.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:59 St�edn� Evropa (letn� �as)
