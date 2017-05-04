# 2017.05.04 15:20:20 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/account_helpers/__init__.py
import datetime
import BigWorld
from constants import ACCOUNT_ATTR
from account_helpers.AccountSettings import AccountSettings, GOLD_FISH_LAST_SHOW_TIME
from shared_utils.account_helpers import BattleResultsCache, ClientClubs
from shared_utils.account_helpers import ClientInvitations
from helpers.time_utils import getCurrentTimestamp

def __checkAccountAttr(attrs, attrID):
    return attrs is not None and attrs & attrID != 0


def isPremiumAccount(attrs):
    return __checkAccountAttr(attrs, ACCOUNT_ATTR.PREMIUM)


def isMoneyTransfer(attrs):
    return __checkAccountAttr(attrs, ACCOUNT_ATTR.TRADING)


def isDemonstrator(attrs):
    return __checkAccountAttr(attrs, ACCOUNT_ATTR.ARENA_CHANGE)


def isRoamingEnabled(attrs):
    return __checkAccountAttr(attrs, ACCOUNT_ATTR.ROAMING)


def isOutOfWallet(attrs):
    return __checkAccountAttr(attrs, ACCOUNT_ATTR.OUT_OF_SESSION_WALLET)


def isClanEnabled(attrs):
    return __checkAccountAttr(attrs, ACCOUNT_ATTR.CLAN)


def getPremiumExpiryDelta(expiryTime):
    check = datetime.datetime.utcfromtimestamp(expiryTime)
    now = datetime.datetime.utcnow()
    return check - now


def convertGold(gold):
    return gold


def getPlayerID():
    return getattr(BigWorld.player(), 'id', 0)


def getAccountDatabaseID():
    return getattr(BigWorld.player(), 'databaseID', 0)


def isLongDisconnectedFromCenter():
    return getattr(BigWorld.player(), 'isLongDisconnectedFromCenter', False)


def getAccountHelpersConfig(manager):
    """ Configures services for package gui.
    :param manager: helpers.dependency.DependencyManager.
    """
    from account_helpers import settings_core
    manager.install(settings_core.getSettingsCoreConfig)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\account_helpers\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:20:20 St�edn� Evropa (letn� �as)
