# 2017.05.04 15:24:37 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RssNewsFeedMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RssNewsFeedMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def openBrowser(self, linkToOpen):
        self._printOverrideError('openBrowser')

    def as_updateFeedS(self, feed):
        """
        :param feed: Represented by Vector.<RssItemVo> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateFeed(feed)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\RssNewsFeedMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:37 Støední Evropa (letní èas)
