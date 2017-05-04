# 2017.05.04 15:28:01 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/vehicle_systems/appearance_cache.py
import BigWorld
import weakref
from debug_utils import *
from functools import partial
from vehicle_systems import vehicle_assembler
from collections import namedtuple
_ENABLE_CACHE_TRACKER = False
_ENABLE_PRECACHE = True
_g_cache = None
d_cacheInfo = None
_VehicleInfo = namedtuple('_VehicleInfo', ['typeDescr',
 'health',
 'isCrewActive',
 'isTurretDetached'])
_AssemblerData = namedtuple('_AssemblerData', ['compoundAssembler',
 'assembler',
 'info',
 'prereqsNames'])

class _AppearanceCache(object):
    __slots__ = ('__arena', '__appearanceCache', '__assemblersCache', '__spaceLoaded')

    @property
    def cache(self):
        return self.__appearanceCache

    def __init__(self, arena):
        global d_cacheInfo
        self.__arena = weakref.proxy(arena)
        self.__appearanceCache = dict()
        self.__assemblersCache = dict()
        self.__spaceLoaded = False
        self.__arena.onNewVehicleListReceived += self.onVehicleListReceived
        self.__arena.onVehicleAdded += self.onVehicleAddedUpdate
        if _ENABLE_CACHE_TRACKER:
            d_cacheInfo = dict()

    def destroy(self):
        global d_cacheInfo
        self.__arena.onVehicleAdded -= self.onVehicleAddedUpdate
        self.__arena.onNewVehicleListReceived -= self.onVehicleListReceived
        for vId, appearance in self.__appearanceCache.iteritems():
            appearance[0].destroy()

        self.__arena = None
        self.__appearanceCache = None
        self.__assemblersCache = None
        if _ENABLE_CACHE_TRACKER:
            d_cacheInfo = None
        return

    def onVehicleListReceived(self):
        if not self.__spaceLoaded or not _ENABLE_PRECACHE:
            return
        for vId, vInfo in self.__arena.vehicles.iteritems():
            cacheApperance(vId, vInfo)

    def onVehicleAddedUpdate(self, vId):
        if _ENABLE_PRECACHE:
            vInfo = self.__arena.vehicles[vId]
            cacheApperance(vId, vInfo)

    def onSpaceLoaded(self):
        self.__spaceLoaded = True
        if _ENABLE_PRECACHE:
            for vId, vInfo in self.__arena.vehicles.iteritems():
                cacheApperance(vId, vInfo)

    def cacheApperance(self, vId, info):
        if vId in self.__assemblersCache or vId in self.__appearanceCache:
            return
        else:
            typeDescriptor = info['vehicleType']
            if typeDescriptor is None:
                return
            isAlive = info['isAlive']
            self.__cacheApperance(vId, _VehicleInfo(typeDescriptor, 1 if isAlive else 0, True if isAlive else False, False))
            return

    def createAppearance(self, vId, vInfo):
        appearance = self.__appearanceCache.get(vId, None)
        compoundAssembler = None
        prereqsNames = []
        if appearance is None or not self.__validate(appearance[1], vInfo):
            assemblerData = self.__assemblersCache.get(vId, None)
            if assemblerData is None or not self.__validate(assemblerData.info, vInfo):
                compoundAssembler, prereqsNames = self.__cacheApperance(vId, vInfo)
            else:
                compoundAssembler = assemblerData.compoundAssembler
                prereqsNames = assemblerData.prereqsNames
        else:
            appearance, info = appearance
        return (appearance, compoundAssembler, prereqsNames)

    def getAppearance(self, vId, resourceRefs):
        appearance, info = self.__appearanceCache.get(vId, (None, None))
        if appearance is None:
            return self.constructAppearance(vId, resourceRefs)
        else:
            return appearance

    def constructAppearance(self, vId, resourceRefs):
        assemblerData = self.__assemblersCache.get(vId, None)
        if assemblerData is None:
            return
        else:
            assembler = assemblerData.assembler
            if assemblerData.compoundAssembler is None:
                if _ENABLE_CACHE_TRACKER:
                    LOG_DEBUG("Appearance cache. Can't find assembler vID = {0}".format(vId))
                return
            if _ENABLE_CACHE_TRACKER:
                LOG_DEBUG('Appearance cache. Constructed vID = {0}'.format(vId))
            assemblerData.info.typeDescr.keepPrereqs(resourceRefs)
            assembler.appearance.start(resourceRefs)
            assembler.constructAppearance(BigWorld.player().playerVehicleID == vId)
            appearance = assembler.appearance
            self.__appearanceCache[vId] = (appearance, assemblerData.info)
            del self.__assemblersCache[vId]
            del assembler
            if _ENABLE_CACHE_TRACKER:
                d_cacheInfo[vId] = BigWorld.time()
            return appearance

    def __cacheApperance(self, vId, info):
        assembler = vehicle_assembler.createAssembler()
        prereqs = info.typeDescr.prerequisites(True)
        for hitTester in info.typeDescr.getHitTesters():
            if hitTester.bspModelName is not None and not hitTester.isBspModelLoaded():
                prereqs.append(hitTester.bspModelName)

        compoundAssembler, assemblerPrereqs = assembler.prerequisites(info.typeDescr, vId, info.health, info.isCrewActive, info.isTurretDetached)
        prereqs += assemblerPrereqs
        self.__assemblersCache[vId] = _AssemblerData(compoundAssembler, assembler, info, prereqs)
        if self.__spaceLoaded:
            BigWorld.loadResourceListBG(prereqs, partial(_resourceLoaded, prereqs, vId))
        return (compoundAssembler, prereqs)

    def __validate(self, cachedInfo, newInfo):
        valid = cachedInfo.typeDescr.type.name == newInfo.typeDescr.type.name
        return valid


def _resourceLoaded(resNames, vId, resourceRefs):
    global _g_cache
    if _g_cache is None:
        return
    else:
        failedRefs = resourceRefs.failedIDs
        for resName in resNames:
            if resName in failedRefs:
                LOG_WARNING('Resource is not found', resName)

        _g_cache.constructAppearance(vId, resourceRefs)
        return


def init(clientArena):
    global _g_cache
    _g_cache = _AppearanceCache(clientArena)


def destroy():
    global _g_cache
    _g_cache.destroy()
    _g_cache = None
    return


def onSpaceLoaded():
    _g_cache.onSpaceLoaded()


def createAppearance(vId, typeDescr, health, isCrewActive, isTurretDetached):
    newInfo = _VehicleInfo(typeDescr, health, isCrewActive, isTurretDetached)
    return _g_cache.createAppearance(vId, newInfo)


def getAppearance(vId, resourceRefs):
    return _g_cache.getAppearance(vId, resourceRefs)


def cacheApperance(vID, info):
    _g_cache.cacheApperance(vID, info)


def dCacheStatus():
    if _ENABLE_CACHE_TRACKER:
        cache = _g_cache.cache
        LOG_DEBUG('VehicleID cachedTime   Activated  VehicleType')
        for vId, appearance in cache.iteritems():
            cachedTime = d_cacheInfo.get(vId, None)
            LOG_DEBUG('{0}     {1}    {2}   {3}'.format(vId, cachedTime, appearance[0].activated, appearance[0].typeDescriptor.type.name))

    return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\vehicle_systems\appearance_cache.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:01 St�edn� Evropa (letn� �as)
