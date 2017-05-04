# 2017.05.04 15:22:21 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/prb_control/storages/sandbox_storage.py
from account_helpers.AccountSettings import AccountSettings, DEFAULT_QUEUE
from constants import QUEUE_TYPE
from gui.LobbyContext import g_lobbyContext
from gui.prb_control.settings import BATTLES_TO_SELECT_RANDOM_MIN_LIMIT
from gui.prb_control.storages.local_storage import LocalStorage
from gui.shared import g_itemsCache
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA
from shared_utils import findFirst

class SandboxStorage(LocalStorage):
    __slots__ = ('_isSelected',)

    def __init__(self):
        super(SandboxStorage, self).__init__()
        self._isSelected = False

    def clear(self):
        self._isSelected = False

    def swap(self):
        if AccountSettings.getSettings(DEFAULT_QUEUE) == QUEUE_TYPE.SANDBOX:
            isSelected = True
            dossier = g_itemsCache.items.getAccountDossier()
            criteria = REQ_CRITERIA.INVENTORY | REQ_CRITERIA.VEHICLE.LEVELS(range(3, 10)) | ~REQ_CRITERIA.VEHICLE.EXPIRED_RENT | ~REQ_CRITERIA.VEHICLE.EVENT_BATTLE
            vehicles = sorted(g_itemsCache.items.getVehicles(criteria=criteria).values(), key=lambda item: item.level)
            vehicle = findFirst(None, vehicles)
            if vehicle is not None:
                AccountSettings.setSettings(DEFAULT_QUEUE, QUEUE_TYPE.RANDOMS)
                isSelected = False
            if dossier is not None and isSelected:
                count = dossier.getRandomStats().getBattlesCount()
                if count >= BATTLES_TO_SELECT_RANDOM_MIN_LIMIT:
                    AccountSettings.setSettings(DEFAULT_QUEUE, QUEUE_TYPE.RANDOMS)
                    isSelected = False
        else:
            isSelected = False
        self._isSelected = isSelected
        return

    def release(self):
        self._isSelected = True

    def suspend(self):
        AccountSettings.setSettings(DEFAULT_QUEUE, QUEUE_TYPE.RANDOMS)
        self.clear()

    def isModeSelected(self):
        return self._isSelected and g_lobbyContext.getServerSettings().isSandboxEnabled()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\storages\sandbox_storage.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:21 St�edn� Evropa (letn� �as)
