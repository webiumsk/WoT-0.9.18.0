# 2017.05.04 15:28:35 Støední Evropa (letní èas)
# Embedded file name: scripts/common/ItemRestore.py


class RESTORE_VEHICLE_TYPE:
    PREMIUM = 0
    ACTION = 1


def getVehicleRestorePrice(defaultBuyPrice, exchangeRate, sellPriceFactor, sellToRestoreFactor):
    credits = defaultBuyPrice[0] + defaultBuyPrice[1] * exchangeRate
    return (int(credits * sellPriceFactor * sellToRestoreFactor), 0)


def getVehicleRestorePriceShort(vehTypeCompDescr, gameParams):
    if 'defaults' in gameParams and 'items' in gameParams['defaults'] and 'itemPrices' in gameParams['defaults']['items'] and vehTypeCompDescr in gameParams['defaults']['items']['itemPrices']:
        defaultBuyPrice = gameParams['defaults']['items']['itemPrices'][vehTypeCompDescr]
    else:
        defaultBuyPrice = gameParams['items']['itemPrices'][vehTypeCompDescr]
    exchangeRate = gameParams['economics']['exchangeRate']
    sellPriceFactor = gameParams['sellPriceFactor']
    sellToRestore = gameParams['restore_config']['vehicles']['sellToRestoreFactor']
    return getVehicleRestorePrice(defaultBuyPrice, exchangeRate, sellPriceFactor, sellToRestore)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\ItemRestore.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:35 Støední Evropa (letní èas)
