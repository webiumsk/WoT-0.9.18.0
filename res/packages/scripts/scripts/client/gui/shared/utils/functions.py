# 2017.05.04 15:26:23 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/utils/functions.py
import random
import re
import ArenaType
from adisp import async, process
from helpers import i18n
from ids_generators import SequenceIDGenerator
from helpers.i18n import makeString
from gui import GUI_SETTINGS, SystemMessages
from items import ITEM_TYPE_INDICES, vehicles
from debug_utils import LOG_DEBUG
from gui.shared.money import Currency
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES

def rnd_choice(*args):
    args = list(args)
    for i in xrange(len(args)):
        c = random.choice(args)
        yield c
        args.remove(c)


def rnd_choice_loop(*args):
    args = list(args)
    while True:
        for value in rnd_choice(*args):
            yield value


def clamp(value, minRange, maxRange):
    if value < minRange:
        return minRange
    if value > maxRange:
        return maxRange
    return value


def roundToMinOrZero(value, minValue):
    if value == 0:
        return value
    else:
        return max(minValue, value)


def getShortDescr(descr):
    """
    Retrieves first occurrence of short description from string.
    Short description can de added to string using <shortDesc></shortDesc> tags
    """
    res_str = ''
    res = re.findall('<shortDesc>(.*?)</shortDesc>', descr)
    if len(res) > 0:
        res_str = res[0]
    else:
        res_str = descr
    return res_str


def stripShortDescrTags(descr):
    """
    Strips short description tags from passed string
    """
    return re.sub('<shortDesc>|</shortDesc>', '', descr)


def stripShortDescr(descr):
    """
    Removes short description from passed string
    """
    return re.sub('<shortDesc>(.*?)</shortDesc>', '', descr)


def makeTooltip(header = None, body = None, note = None, attention = None):
    """
    Make complex tooltip from carrying params.
    This special formatted string will be parsed from Flash
    net.wargaming.managers.ToolTip.showComplex(str, props)
    """
    res_str = ''
    if header is not None:
        res_str += '{HEADER}%s{/HEADER}' % makeString(header)
    if body is not None:
        res_str += '{BODY}%s{/BODY}' % makeString(body)
    if note is not None:
        res_str += '{NOTE}%s{/NOTE}' % makeString(note)
    if attention is not None:
        res_str += '{ATTENTION}%s{/ATTENTION}' % makeString(attention)
    return res_str


@async
@process
def checkAmmoLevel(vehicles, callback):
    """
    Check ammo for current vehicle, if it is lower then 20% shows message dialog
    Example:
            isAmmoOk = yield checkAmmoLevel()
            if isAmmoOk:
                    do something...
    
    @return: True if ammo level is ok or user confirm, False otherwise
    """
    showAmmoWarning = False
    for vehicle in vehicles:
        if vehicle.isReadyToFight:
            if not vehicle.isAutoLoadFull() or not vehicle.isAutoEquipFull():
                from gui import SystemMessages
                from gui.shared.gui_items.processors.vehicle import VehicleLayoutProcessor
                shellsLayout = []
                eqsLayout = []
                for shell in vehicle.shells:
                    shellsLayout.extend(shell.defaultLayoutValue)

                for eq in vehicle.eqsLayout:
                    if eq is not None:
                        eqsLayout.extend(eq.defaultLayoutValue)
                    else:
                        eqsLayout.extend((0, 0))

                LOG_DEBUG('setVehicleLayouts', shellsLayout, eqsLayout)
                result = yield VehicleLayoutProcessor(vehicle, shellsLayout, eqsLayout).request()
                if result and result.auxData:
                    for m in result.auxData:
                        SystemMessages.pushI18nMessage(m.userMsg, type=m.sysMsgType)

                if result and len(result.userMsg):
                    SystemMessages.pushI18nMessage(result.userMsg, type=result.sysMsgType)
            showAmmoWarning = showAmmoWarning or not vehicle.isAmmoFull

    if showAmmoWarning:
        from gui import DialogsInterface
        success = yield DialogsInterface.showI18nConfirmDialog('lowAmmo')
        callback(success)
    else:
        yield lambda callback: callback(None)
        callback(True)
    return


def getModuleGoldStatus(price, money):
    """
    @param price: module price
    @param money: player's money
    @return: tuple(CouldBeBought, menuStatus, tooltipStatus)
    """
    currency = Currency.GOLD
    availableForCredits = 1
    availableForGold = 2
    couldBeBought = 0
    if price.credits and price.credits > money.credits:
        currency = Currency.CREDITS
    else:
        couldBeBought |= availableForCredits
    if price.gold and price.gold < money.gold:
        couldBeBought |= availableForGold
    if not couldBeBought:
        return (False, '#menu:moduleFits/%s_error' % currency, '#tooltips:moduleFits/%s_error' % currency)
    return (True, '', '')


def findConflictedEquipments(itemCompactDescr, itemTypeID, vehicle):
    conflictEqs = []
    if itemTypeID != ITEM_TYPE_INDICES['vehicleEngine']:
        return conflictEqs
    oldModule, = vehicle.descriptor.installComponent(itemCompactDescr)
    for equipmentDescr in vehicle.equipments:
        if equipmentDescr:
            equipment = vehicles.getDictDescr(equipmentDescr)
            installPossible, reason = equipment.checkCompatibilityWithVehicle(vehicle.descriptor)
            if not installPossible:
                conflictEqs.append(equipment)

    vehicle.descriptor.installComponent(oldModule)
    return conflictEqs


def findConflictedEquipmentForModule(module, vehicle):
    return findConflictedEquipments(module.compactDescr, ITEM_TYPE_INDICES[module.itemTypeName], vehicle)


def getArenaSubTypeID(arenaTypeID):
    return arenaTypeID >> 16


def getArenaSubTypeName(arenaTypeID):
    return ArenaType.g_cache[arenaTypeID].gameplayName


def getArenaGeomentryName(arenaTypeID):
    return ArenaType.g_cache[arenaTypeID].geometryName


def getArenaShortName(arenaTypeID):
    return ArenaType.g_cache[arenaTypeID].name


def getArenaFullName(arenaTypeID):
    arenaType = ArenaType.g_cache[arenaTypeID]
    arenaName = arenaType.name
    if arenaType.gameplayName != 'ctf':
        arenaName = '%s - %s' % (arenaName, makeString('#arenas:type/%s/name' % arenaType.gameplayName))
    return arenaName


def getBattleSubTypeWinText(arenaTypeID, teamID):
    key = 'type/%s/description' % ArenaType.g_cache[arenaTypeID].gameplayName
    winText = i18n.makeString('#arenas:%s' % key)
    if winText == key:
        return i18n.makeString('#arenas:%s%d' % (key, teamID))
    return winText


def getBattleSubTypeBaseNumder(arenaTypeID, team, baseID):
    teamBasePositions = ArenaType.g_cache[arenaTypeID].teamBasePositions
    if len(teamBasePositions) >= team:
        points = teamBasePositions[team - 1]
        if len(points) > 1:
            return ' %d' % (sorted(points.keys()).index(baseID) + 1)
    points = ArenaType.g_cache[arenaTypeID].controlPoints
    if points:
        if len(points) > 1:
            return ' %d' % baseID
    return ''


def isBaseExists(arenaTypeID, team):
    teamBasePositions = ArenaType.g_cache[arenaTypeID].teamBasePositions
    if len(teamBasePositions) >= team:
        points = teamBasePositions[team - 1]
        if len(points) > 0:
            return True
    return False


def isControlPointExists(arenaTypeID):
    controlPoint = ArenaType.g_cache[arenaTypeID].controlPoints
    if controlPoint:
        return True
    return False


def getAbsoluteUrl(url):
    return url.replace('../', 'img://gui/')


_viewIdsGen = None

def getViewName(viewAlias, *args):
    l = list(args)
    l.insert(0, viewAlias)
    return '_'.join(map(str, l))


def getUniqueViewName(viewAlias):
    global _viewIdsGen
    if _viewIdsGen is None:
        _viewIdsGen = SequenceIDGenerator()
    return getViewName(viewAlias, _viewIdsGen.nextSequenceID)


def getPostBattleUniqueSubUrl(svrPackedData, clientPackedData):
    return '%s/%s/%s ' % (GUI_SETTINGS.postBattleExchange.url, svrPackedData, clientPackedData)


def parsePostBattleUniqueSubUrl(uniqueSubUrl):
    return uniqueSubUrl.split('/')[1:]


def showSentInviteMessage(user = None):
    """
    This method adds the invite(in squad) message to system channel.
    @param user: user info
    """
    if user is not None:
        if user is not None:
            SystemMessages.pushI18nMessage(SYSTEM_MESSAGES.PREBATTLE_INVITES_SENDINVITE_NAME, type=SystemMessages.SM_TYPE.Information, name=user.getFullName())
        else:
            SystemMessages.pushI18nMessage(SYSTEM_MESSAGES.PREBATTLE_INVITES_SENDINVITE, type=SystemMessages.SM_TYPE.Information)
    return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\utils\functions.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:23 St�edn� Evropa (letn� �as)
