# 2017.05.04 15:29:16 Støední Evropa (letní èas)
# Embedded file name: scripts/common/items/vehicle_config_types.py
from collections import namedtuple
LodSettings = namedtuple('LodSettings', ['maxLodDistance', 'maxPriority'])
LeveredSuspensionConfig = namedtuple('LeveredSuspensionConfig', ['levers', 'interpolationSpeedMul', 'lodSettings'])
SuspensionLever = namedtuple('SuspensionLever', ['startNodeName',
 'jointNodeName',
 'trackNodeName',
 'minAngle',
 'maxAngle'])
SoundSiegeModeStateChange = namedtuple('SoundSiegeModeStateChange', ['on', 'off'])
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\items\vehicle_config_types.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:29:16 Støední Evropa (letní èas)
