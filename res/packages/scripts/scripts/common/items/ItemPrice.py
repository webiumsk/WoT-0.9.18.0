# 2017.05.04 15:29:09 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/items/ItemPrice.py
from goodies.GoodieResources import Gold, Credits

class PRICE_TYPE:
    DEFAULT = (0,)
    PROMO = (1,)
    PERSONAL = (2,)


def getItemPrice(item, gameParams, goodies = None, goodieTarget = None):
    priceType = PRICE_TYPE.DEFAULT
    actualPrice = gameParams['items']['itemPrices'][item]
    defaultPrice = gameParams['defaults'].get('items', {}).get('itemPrices', {}).get(item, None)
    if not defaultPrice:
        defaultPrice = actualPrice
    else:
        priceType = PRICE_TYPE.PROMO
    if (actualPrice[0] == 0 or actualPrice[1] == 0) and goodies and goodieTarget:
        personalDiscounts = goodies.test(goodieTarget, {Credits(defaultPrice[0]), Gold(defaultPrice[1])})
        for _, discount in personalDiscounts.iteritems():
            if isinstance(discount, Gold) and discount.value <= actualPrice[1]:
                actualPrice = (0, discount.value)
                priceType = PRICE_TYPE.PERSONAL
            elif isinstance(discount, Credits) and discount.value <= actualPrice[0]:
                actualPrice = (discount.value, 0)
                priceType = PRICE_TYPE.PERSONAL

    return (defaultPrice, actualPrice, priceType)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\items\ItemPrice.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:29:09 St�edn� Evropa (letn� �as)
