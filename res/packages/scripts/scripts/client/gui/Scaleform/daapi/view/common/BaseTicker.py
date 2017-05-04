# 2017.05.04 15:22:46 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/common/BaseTicker.py
import BigWorld
import time
import constants
from debug_utils import LOG_DEBUG
from gui.Scaleform.daapi.view.meta.TickerMeta import TickerMeta
from gui import GUI_SETTINGS

class BaseTicker(TickerMeta):
    UPDATE_INTERVAL = 600
    RSS_URL = 'http://wot.kongzhong.com/erji/ticker.xml'

    def __init__(self):
        super(BaseTicker, self).__init__()
        self.__lastUpdateTime = -1
        self.__lastRSS = {}

    def showBrowser(self, entryID):
        """
        Showing browser with given @entryID.
        @param entryID: <str> rss entry id
        """
        entry = self.__findEntry(entryID)
        if entry is not None:
            link = entry.get('link', '')
            if link:
                LOG_DEBUG('Open browser at page: ', link)
                self._handleBrowserLink(link)
            else:
                LOG_DEBUG('Link is empty, nothing to show.')
        return

    def _handleBrowserLink(self, link):
        raise NotImplementedError

    def _populate(self):
        super(BaseTicker, self)._populate()
        self.__updateCbID = None
        self.__updateCallback()
        return

    def _dispose(self):
        super(BaseTicker, self)._dispose()
        self.__clearCallback()
        self.__lastRSS = None
        return

    def __clearCallback(self):
        """ Clear news updating callback """
        if self.__updateCbID is not None:
            BigWorld.cancelCallback(self.__updateCbID)
            self.__updateCbID = None
        return

    def __updateCallback(self):
        """ New updating interval handler """
        self.__update()
        self.__clearCallback()
        self.__updateCbID = BigWorld.callback(self.UPDATE_INTERVAL, self.__updateCallback)

    def __update(self):
        if not GUI_SETTINGS.movingText.show:
            return
        else:
            self.__lastUpdateTime = time.time()
            downloadUrl = None
            if constants.IS_CHINA:
                downloadUrl = BaseTicker.RSS_URL
            from helpers.RSSDownloader import g_downloader
            if g_downloader is not None:
                g_downloader.download(self.__rssDownloadReceived, url=downloadUrl)
            return

    def __rssDownloadReceived(self, rssFeed):
        """ Rss data received handler """
        self.__lastRSS = rssFeed
        self.as_setItemsS(self.__getEntries(rssFeed))

    @classmethod
    def __getEntries(cls, rssFeed):
        """
        @return: <list of dict< 'id':<str>, 'title':<str>, 'summary':<str> >
                list of rss entries data
        """
        result = []
        for entry in rssFeed.get('entries', []):
            result.append({'id': entry.get('id'),
             'title': entry.get('title'),
             'summary': entry.get('summary')})

        return result

    def __findEntry(self, entryID):
        """
        Returns rss entry.
        
        @param entryID: <str> rss id to find
        @return: <dict> entry data
        """
        for entry in self.__lastRSS.get('entries', []):
            if entry.get('id') == entryID:
                return entry

        return None
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\common\BaseTicker.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:46 St�edn� Evropa (letn� �as)
