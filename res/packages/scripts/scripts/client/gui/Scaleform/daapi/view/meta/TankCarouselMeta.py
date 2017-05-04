# 2017.05.04 15:24:39 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TankCarouselMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class TankCarouselMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def selectVehicle(self, id):
        self._printOverrideError('selectVehicle')

    def buyTank(self):
        self._printOverrideError('buyTank')

    def buySlot(self):
        self._printOverrideError('buySlot')

    def setFilter(self, id):
        self._printOverrideError('setFilter')

    def resetFilters(self):
        self._printOverrideError('resetFilters')

    def updateHotFilters(self):
        self._printOverrideError('updateHotFilters')

    def as_getDataProviderS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDataProvider()

    def as_setCarouselFilterS(self, data):
        """
        :param data: Represented by TankCarouselFilterSelectedVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCarouselFilter(data)

    def as_initCarouselFilterS(self, data):
        """
        :param data: Represented by TankCarouselFilterInitVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_initCarouselFilter(data)

    def as_showCounterS(self, countText, isAttention):
        if self._isDAAPIInited():
            return self.flashObject.as_showCounter(countText, isAttention)

    def as_rowCountS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_rowCount(value)

    def as_hideCounterS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideCounter()

    def as_blinkCounterS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_blinkCounter()

    def as_setSmallDoubleCarouselS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSmallDoubleCarousel(value)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\TankCarouselMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:39 St�edn� Evropa (letn� �as)
