# 2017.05.04 15:24:07 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/trainings/TrainingSettingsWindow.py
import ArenaType
from account_helpers import gameplay_ctx
from debug_utils import LOG_ERROR, LOG_CURRENT_EXCEPTION
from gui.Scaleform.daapi.view.lobby.trainings import formatters
from gui.Scaleform.daapi.view.meta.TrainingWindowMeta import TrainingWindowMeta
from gui.prb_control import prbEntityProperty
from gui.prb_control.entities.training.legacy.ctx import TrainingSettingsCtx
from gui.prb_control.prb_getters import getTrainingBattleRoundLimits
from gui.shared import events, EVENT_BUS_SCOPE
from gui.shared import g_itemsCache
from helpers import i18n

class ArenasCache(object):

    def __init__(self):
        self.__cache = []
        for arenaTypeID, arenaType in ArenaType.g_cache.iteritems():
            if arenaType.explicitRequestOnly or not gameplay_ctx.isCreationEnabled(arenaType.gameplayName):
                continue
            try:
                nameSuffix = '' if arenaType.gameplayName == 'ctf' else i18n.makeString('#arenas:type/%s/name' % arenaType.gameplayName)
                self.__cache.append({'label': '%s - %s' % (arenaType.name, nameSuffix) if len(nameSuffix) else arenaType.name,
                 'name': arenaType.name,
                 'arenaType': nameSuffix,
                 'key': arenaTypeID,
                 'size': arenaType.maxPlayersInTeam,
                 'time': arenaType.roundLength / 60,
                 'description': '',
                 'icon': formatters.getMapIconPath(arenaType)})
            except Exception:
                LOG_ERROR('There is error while reading arenas cache', arenaTypeID, arenaType)
                LOG_CURRENT_EXCEPTION()
                continue

        self.__cache = sorted(self.__cache, key=lambda x: (x['label'].lower(), x['name'].lower()))

    @property
    def cache(self):
        return self.__cache


class TrainingSettingsWindow(TrainingWindowMeta):

    def __init__(self, ctx = None):
        super(TrainingSettingsWindow, self).__init__()
        self.__isCreateRequest = ctx.get('isCreateRequest', False)
        self.__arenasCache = ArenasCache()

    @prbEntityProperty
    def prbEntity(self):
        return None

    def onWindowClose(self):
        self.destroy()

    def _populate(self):
        super(TrainingSettingsWindow, self)._populate()
        self.as_setDataS(self.getInfo(), self.getMapsData())

    def getMapsData(self):
        return self.__arenasCache.cache

    def getInfo(self):
        settings = TrainingSettingsCtx()
        if not self.__isCreateRequest:
            settings = settings.fetch(self.prbEntity.getSettings())
        if g_itemsCache.isSynced():
            accountAttrs = g_itemsCache.items.stats.attributes
        else:
            accountAttrs = 0
        _, maxBound = getTrainingBattleRoundLimits(accountAttrs)
        info = {'description': settings.getComment(),
         'timeout': settings.getRoundLen() / 60,
         'arena': settings.getArenaTypeID(),
         'privacy': not settings.isOpened(),
         'create': self.__isCreateRequest,
         'canMakeOpenedClosed': True,
         'canChangeComment': True,
         'canChangeArena': True,
         'maxBattleTime': maxBound / 60}
        if not self.__isCreateRequest:
            permissions = self.prbEntity.getPermissions()
            info['canMakeOpenedClosed'] = permissions.canMakeOpenedClosed()
            info['canChangeComment'] = permissions.canChangeComment()
            info['canChangeArena'] = permissions.canChangeArena()
        return info

    def updateTrainingRoom(self, arena, roundLength, isPrivate, comment):
        if self.__isCreateRequest:
            settings = TrainingSettingsCtx(isRequestToCreate=True)
        else:
            settings = TrainingSettingsCtx(isRequestToCreate=False)
        settings.setArenaTypeID(arena)
        settings.setRoundLen(roundLength * 60)
        settings.setOpened(not isPrivate)
        settings.setComment(comment)
        self.fireEvent(events.TrainingSettingsEvent(events.TrainingSettingsEvent.UPDATE_TRAINING_SETTINGS, ctx={'settings': settings}), scope=EVENT_BUS_SCOPE.LOBBY)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\trainings\TrainingSettingsWindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:07 St�edn� Evropa (letn� �as)
