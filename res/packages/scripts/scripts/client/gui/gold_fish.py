# 2017.05.04 15:20:59 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/gold_fish.py
from account_helpers.AccountSettings import AccountSettings, GOLD_FISH_LAST_SHOW_TIME
import constants
from gui import GUI_SETTINGS
from helpers.time_utils import getCurrentTimestamp

def isGoldFishActionActive():
    from gui.LobbyContext import g_lobbyContext
    from gui.shared.ItemsCache import g_itemsCache
    outOfSessionWallet = constants.ACCOUNT_ATTR.OUT_OF_SESSION_WALLET
    return not g_itemsCache.items.stats.isGoldFishBonusApplied and g_lobbyContext.getServerSettings().isGoldFishEnabled() and not g_itemsCache.items.stats.attributes & outOfSessionWallet != 0


def isTimeToShowGoldFishPromo():
    return getCurrentTimestamp() - AccountSettings.getFilter(GOLD_FISH_LAST_SHOW_TIME) >= GUI_SETTINGS.goldFishActionShowCooldown
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\gold_fish.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:20:59 St�edn� Evropa (letn� �as)
