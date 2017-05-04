# 2017.05.04 15:25:43 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/formatters/currency.py
import BigWorld
from debug_utils import LOG_WARNING
from gui.shared.money import Currency
_CURRENCY_TO_BW_FORMATTER = {Currency.CREDITS: BigWorld.wg_getIntegralFormat,
 Currency.GOLD: BigWorld.wg_getGoldFormat}

def getBWFormatter(currency):
    if currency in _CURRENCY_TO_BW_FORMATTER:
        return _CURRENCY_TO_BW_FORMATTER[currency]
    LOG_WARNING('BW formatter is not set for the following currency: ', currency)
    return lambda v: v
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\formatters\currency.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:25:43 Støední Evropa (letní èas)
