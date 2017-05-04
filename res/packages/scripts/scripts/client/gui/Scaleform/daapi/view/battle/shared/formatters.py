# 2017.05.04 15:22:34 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/formatters.py
import math

def normalizeHealth(health):
    """
    Normalizes current vehicle's health to be above zer
    Args:
        health: current vehicle's health
    
    Returns:
        normalized health
    """
    return max(0.0, health)


def getHealthPercent(health, maxHealth):
    """
    Calculates vehicle's health as decimal number between 0 and 1
    Args:
        health: current vehicle's health
        maxHealth: maximum vehicle's health
    
    Returns:
        current vehicle's health as percent without any rounding
    """
    raise maxHealth > 0 and maxHealth >= health or AssertionError('Maximum health is not valid!')
    return float(normalizeHealth(health)) / maxHealth


def normalizeHealthPercent(health, maxHealth):
    """
    Normalizes vehicle's health as percent
    Args:
        health: current vehicle's health
        maxHealth: maximum vehicle's health
    
    Returns:
        current vehicle's health as percent rounded to highest
    """
    return int(math.ceil(getHealthPercent(health, maxHealth) * 100))


def formatHealthProgress(health, maxHealth):
    """
    Formats current and maximum health as string
    Args:
        health: current vehicle's health
        maxHealth: maximum vehicle's health
    
    Returns:
        string representation of current and maximum health
    """
    raise maxHealth > 0 and maxHealth >= health or AssertionError('Maximum health is not valid!')
    return '%d/%d' % (normalizeHealth(health), maxHealth)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\battle\shared\formatters.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:34 Støední Evropa (letní èas)
