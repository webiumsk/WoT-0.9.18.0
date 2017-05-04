# 2017.05.04 15:24:47 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/ImageManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class ImageManagerMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    """

    def as_setImageCacheSettingsS(self, maxSize, minSize):
        if self._isDAAPIInited():
            return self.flashObject.as_setImageCacheSettings(maxSize, minSize)

    def as_loadImagesS(self, sourceData):
        if self._isDAAPIInited():
            return self.flashObject.as_loadImages(sourceData)

    def as_unloadImagesS(self, sourceData):
        if self._isDAAPIInited():
            return self.flashObject.as_unloadImages(sourceData)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\entities\abstract\ImageManagerMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:47 Støední Evropa (letní èas)
