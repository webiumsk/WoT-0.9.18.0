# 2017.05.04 15:26:31 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/view_helpers/emblems.py
import BigWorld
import ResMgr
from functools import partial
from debug_utils import LOG_WARNING
from gui.LobbyContext import g_lobbyContext
from gui.shared.utils import mapTextureToTheMemory, getImageSize
from gui.clans import settings as clan_settings

def _readEmblem(filePath):
    data = ResMgr.openSection(filePath)
    if data is not None:
        return data.asBinary
    else:
        return


class _EmblemsHelper(object):

    @property
    def remoteCache(self):
        from gui.shared.RemoteDataDownloader import g_remoteCache
        return g_remoteCache

    @classmethod
    def getMemoryTexturePath(cls, emblem):
        return mapTextureToTheMemory(emblem)

    @classmethod
    def requestEmblemByUrl(cls, url, size, callback, defaultEmblemGetter = None):
        defaultEmblemGetter = defaultEmblemGetter or (lambda v: None)

        def _onEmblemReceived(_, emblem):
            imgSize = getImageSize(emblem)
            if imgSize != size:
                LOG_WARNING('Received emblem has invalid size, use default instead', imgSize, size, url, type(emblem))
                emblem = defaultEmblemGetter(size)
            callback(emblem)

        if hasattr(BigWorld.player(), 'customFilesCache'):
            if url is not None:
                BigWorld.player().customFilesCache.get(url, _onEmblemReceived)
            else:
                BigWorld.callback(0.0, lambda : callback(defaultEmblemGetter(size)))
        else:
            LOG_WARNING('Trying to get emblem by url from non-account', url)
        return


class ClanEmblemsHelper(_EmblemsHelper):
    __default = {16: _readEmblem(clan_settings.getDefaultEmblem16x16()),
     32: _readEmblem(clan_settings.getDefaultEmblem32x32()),
     64: None,
     128: _readEmblem(clan_settings.getDefaultEmblem128x128()),
     256: _readEmblem(clan_settings.getDefaultEmblem256x256())}

    def requestClanEmblem16x16(self, clanDbID):
        self.__makeRequest(clanDbID, 16, self.onClanEmblem16x16Received)

    def requestClanEmblem32x32(self, clanDbID):
        self.__makeRequest(clanDbID, 32, self.onClanEmblem32x32Received)

    def requestClanEmblem64x64(self, clanDbID):
        self.__makeRequest(clanDbID, 64, self.onClanEmblem64x64Received)

    def requestClanEmblem128x128(self, clanDbID):
        self.__makeRequest(clanDbID, 128, self.onClanEmblem128x128Received)

    def requestClanEmblem256x256(self, clanDbID):
        self.__makeRequest(clanDbID, 256, self.onClanEmblem256x256Received)

    def onClanEmblem16x16Received(self, clanDbID, emblem):
        pass

    def onClanEmblem32x32Received(self, clanDbID, emblem):
        pass

    def onClanEmblem64x64Received(self, clanDbID, emblem):
        pass

    def onClanEmblem128x128Received(self, clanDbID, emblem):
        pass

    def onClanEmblem256x256Received(self, clanDbID, emblem):
        pass

    def getDefaultClanEmblem(self, size):
        width, _ = size
        return self.__default.get(width, None)

    def _requestClanEmblem(self, clanDbID, url, size, handler):
        cb = partial(handler, clanDbID)
        self.requestEmblemByUrl(url, (size, size), cb, self.getDefaultClanEmblem)

    def __makeRequest(self, clanDbID, size, requestHandler):
        svrSettings = g_lobbyContext.getServerSettings()
        url = svrSettings.fileServer.getClanEmblemBySize(clanDbID, size) if svrSettings is not None else None
        self._requestClanEmblem(clanDbID, url, size, requestHandler)
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\view_helpers\emblems.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:31 St�edn� Evropa (letn� �as)
