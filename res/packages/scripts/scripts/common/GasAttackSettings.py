# 2017.05.04 15:28:34 Støední Evropa (letní èas)
# Embedded file name: scripts/common/GasAttackSettings.py
import Math

class GasAttackState(object):
    NO = 0
    PREPARE = 1
    ATTACK = 2
    DONE = 3


class GasAttackSettings:
    DEATH_DELAY = 10

    def __init__(self, attackLength, preparationPeriod, position, startRadius, endRadius, compressionTime):
        self.attackLength = attackLength
        self.preparationPeriod = preparationPeriod
        self.position = Math.Vector3(position)
        self.startRadius = startRadius
        self.endRadius = endRadius
        self.compressionTime = compressionTime
        if compressionTime == 0:
            self.compressionSpeed = 0
            self.startRadius = self.endRadius
        else:
            self.compressionSpeed = float(startRadius - endRadius) / compressionTime


def gasAttackStateFor(settings, timeFromActivation):
    if timeFromActivation <= settings.preparationPeriod:
        return (GasAttackState.PREPARE, (settings.position, settings.startRadius))
    currentRadius = settings.startRadius - (timeFromActivation - settings.preparationPeriod) * settings.compressionSpeed
    if currentRadius <= settings.endRadius:
        return (GasAttackState.DONE, (settings.position, settings.endRadius))
    return (GasAttackState.ATTACK, (settings.position, currentRadius))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\GasAttackSettings.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:34 Støední Evropa (letní èas)
