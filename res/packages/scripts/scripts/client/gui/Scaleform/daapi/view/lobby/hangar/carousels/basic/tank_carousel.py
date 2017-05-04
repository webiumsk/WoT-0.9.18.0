# 2017.05.04 15:23:36 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/basic/tank_carousel.py
import constants
from CurrentVehicle import g_currentVehicle
from account_helpers.settings_core import settings_constants
from gui import SystemMessages
from gui.Scaleform import getButtonsAssetPath
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.hangar.carousels.basic.carousel_data_provider import CarouselDataProvider
from gui.Scaleform.daapi.view.lobby.hangar.carousels.basic.carousel_filter import CarouselFilter
from gui.Scaleform.daapi.view.lobby.hangar.filter_contexts import getFilterSetupContexts, FilterSetupContext
from gui.Scaleform.daapi.view.meta.TankCarouselMeta import TankCarouselMeta
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS
from gui.Scaleform.genConsts.STORE_TYPES import STORE_TYPES
from gui.shared import events, EVENT_BUS_SCOPE, g_itemsCache
from gui.shared.formatters import text_styles
from gui.shared.gui_items.processors.vehicle import VehicleSlotBuyer
from gui.shared.utils import decorators
from gui.shared.utils.functions import makeTooltip
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from helpers.i18n import makeString as _ms
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.game_control import IRentalsController, IIGRController, IClanLockController
_CAROUSEL_FILTERS = ('bonus', 'favorite', 'elite', 'premium')
if constants.IS_KOREA:
    _CAROUSEL_FILTERS += ('igr',)

class TankCarousel(TankCarouselMeta):
    rentals = dependency.descriptor(IRentalsController)
    igrCtrl = dependency.descriptor(IIGRController)
    clanLock = dependency.descriptor(IClanLockController)
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self):
        super(TankCarousel, self).__init__()
        self._usedFilters = _CAROUSEL_FILTERS
        self._carouselDPConfig = {'carouselFilter': None,
         'itemsCache': None,
         'currentVehicle': None}
        self._carouselDPCls = CarouselDataProvider
        self._carouselFilterCls = CarouselFilter
        self._carouselDP = None
        self._itemsCache = None
        return

    def selectVehicle(self, idx):
        """ This method is called from flash when user clicks on carousel item.
        """
        self._carouselDP.selectVehicle(idx)

    def buyTank(self):
        """ Open store with the shop tab and 'vehicle' component set
        """
        ctx = {'tabId': STORE_TYPES.SHOP,
         'component': STORE_CONSTANTS.VEHICLE}
        self.fireEvent(events.LoadViewEvent(VIEW_ALIAS.LOBBY_STORE, ctx=ctx), EVENT_BUS_SCOPE.LOBBY)

    def buySlot(self):
        self.__buySlot()

    def updateHotFilters(self):
        """ This method is called from flash on resize in order to get actual state of filters.
        """
        self.__updateHotFilters()

    def updateParams(self):
        """ This method is called from Hangar in order to update
        the stats of last two items (free slots, slot price)
        """
        self._carouselDP.updateSupplies()

    def resetFilters(self):
        self.filter.reset()
        self.updateHotFilters()
        self.applyFilter()

    def setFilter(self, idx):
        self.filter.switch(self._usedFilters[idx])
        self.blinkCounter()
        self.applyFilter()

    def getTotalVehiclesCount(self):
        return self._carouselDP.getTotalVehiclesCount()

    def getCurrentVehiclesCount(self):
        return self._carouselDP.getCurrentVehiclesCount()

    def hasRentedVehicles(self):
        return self._carouselDP.hasRentedVehicles()

    def hasEventVehicles(self):
        return self._carouselDP.hasEventVehicles()

    def blinkCounter(self):
        self.as_blinkCounterS()

    def applyFilter(self):
        self._carouselDP.applyFilter()
        if not self.filter.isDefault():
            drawAttention = self._carouselDP.getCurrentVehiclesCount() == 0
            self.as_showCounterS(self.formatCountVehicles(), drawAttention)
        else:
            self.as_hideCounterS()

    def formatCountVehicles(self):
        currentVehiclesCount = self._carouselDP.getCurrentVehiclesCount()
        totalVehiclesCount = self._carouselDP.getTotalVehiclesCount()
        style = text_styles.error if currentVehiclesCount == 0 else text_styles.stats
        return '{} / {}'.format(style(currentVehiclesCount), text_styles.main(totalVehiclesCount))

    def updateVehicles(self, vehicles = None, filterCriteria = None):
        if vehicles is None and filterCriteria is None:
            self.as_initCarouselFilterS(self.__getInitialFilterVO(getFilterSetupContexts(self._itemsCache.items.shop.dailyXPFactor)))
        self._carouselDP.updateVehicles(vehicles, filterCriteria)
        self.applyFilter()
        return

    @property
    def filter(self):
        if self._carouselDP is not None:
            return self._carouselDP.filter
        else:
            return
            return

    def _populate(self):
        super(TankCarousel, self)._populate()
        self.rentals.onRentChangeNotify += self.__updateRent
        self.igrCtrl.onIgrTypeChanged += self.__updateIgrType
        self.clanLock.onClanLockUpdate += self.__updateClanLocks
        self.settingsCore.onSettingsChanged += self.__onCarouselSettingsChange
        self.app.loaderManager.onViewLoaded += self.__onViewLoaded
        setting = self.settingsCore.options.getSetting(settings_constants.GAME.CAROUSEL_TYPE)
        self.as_rowCountS(setting.getRowCount())
        self._itemsCache = g_itemsCache
        self._carouselDPConfig.update({'carouselFilter': self._carouselFilterCls(),
         'itemsCache': self._itemsCache,
         'currentVehicle': g_currentVehicle})
        self._carouselDP = self._carouselDPCls(**self._carouselDPConfig)
        setting = self.settingsCore.options.getSetting(settings_constants.GAME.VEHICLE_CAROUSEL_STATS)
        self._carouselDP.setShowStats(setting.get())
        self._carouselDP.setEnvironment(self.app)
        self._carouselDP.setFlashObject(self.as_getDataProviderS())
        self._carouselDP.buildList()
        setting = self.settingsCore.options.getSetting(settings_constants.GAME.DOUBLE_CAROUSEL_TYPE)
        self.as_setSmallDoubleCarouselS(setting.enableSmallCarousel())
        self.as_initCarouselFilterS(self.__getInitialFilterVO(getFilterSetupContexts(self._itemsCache.items.shop.dailyXPFactor)))
        self.applyFilter()

    def _dispose(self):
        self.rentals.onRentChangeNotify -= self.__updateRent
        self.igrCtrl.onIgrTypeChanged -= self.__updateIgrType
        self.clanLock.onClanLockUpdate -= self.__updateClanLocks
        self.settingsCore.onSettingsChanged -= self.__onCarouselSettingsChange
        self.app.loaderManager.onViewLoaded -= self.__onViewLoaded
        self._itemsCache = None
        self._carouselDP.fini()
        self._carouselDP = None
        self._carouselDPConfig.clear()
        super(TankCarousel, self)._dispose()
        return

    def __getInitialFilterVO(self, contexts):
        filters = self.filter.getFilters(self._usedFilters)
        filtersVO = {'counterCloseTooltip': makeTooltip('#tooltips:tanksFilter/counter/close/header', '#tooltips:tanksFilter/counter/close/body'),
         'mainBtn': {'value': getButtonsAssetPath('params'),
                     'tooltip': makeTooltip('#tank_carousel_filter:tooltip/params/header', '#tank_carousel_filter:tooltip/params/body')},
         'hotFilters': []}
        for entry in self._usedFilters:
            filterCtx = contexts.get(entry, FilterSetupContext())
            filtersVO['hotFilters'].append({'value': getButtonsAssetPath(filterCtx.asset or entry),
             'selected': filters[entry],
             'tooltip': makeTooltip('#tank_carousel_filter:tooltip/{}/header'.format(entry), _ms('#tank_carousel_filter:tooltip/{}/body'.format(entry), **filterCtx.ctx))})

        return filtersVO

    def __updateHotFilters(self):
        self.as_setCarouselFilterS({'hotFilters': [ self.filter.get(key) for key in self._usedFilters ]})

    @decorators.process('buySlot')
    def __buySlot(self):
        result = yield VehicleSlotBuyer().request()
        if result.userMsg:
            SystemMessages.pushI18nMessage(result.userMsg, type=result.sysMsgType)

    def __updateRent(self, vehicles):
        self.updateVehicles(vehicles)

    def __updateIgrType(self, roomType, xpFactor):
        self.updateVehicles(filterCriteria=REQ_CRITERIA.VEHICLE.IS_PREMIUM_IGR)

    def __updateClanLocks(self, vehicles, isFull):
        if isFull:
            self.updateVehicles()
        else:
            self.updateVehicles(vehicles)

    def __onCarouselSettingsChange(self, diff):
        if settings_constants.GAME.CAROUSEL_TYPE in diff:
            setting = self.settingsCore.options.getSetting(settings_constants.GAME.CAROUSEL_TYPE)
            self.as_rowCountS(setting.getRowCount())
        if settings_constants.GAME.DOUBLE_CAROUSEL_TYPE in diff:
            setting = self.settingsCore.options.getSetting(settings_constants.GAME.DOUBLE_CAROUSEL_TYPE)
            self.as_setSmallDoubleCarouselS(setting.enableSmallCarousel())
        if settings_constants.GAME.VEHICLE_CAROUSEL_STATS in diff:
            setting = self.settingsCore.options.getSetting(settings_constants.GAME.VEHICLE_CAROUSEL_STATS)
            self._carouselDP.setShowStats(setting.get())
            self._carouselDP.updateVehicles()

    def __onViewLoaded(self, view):
        if view is not None and view.settings is not None:
            if view.settings.alias == VIEW_ALIAS.TANK_CAROUSEL_FILTER_POPOVER:
                view.setTankCarousel(self)
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\hangar\carousels\basic\tank_carousel.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:36 St�edn� Evropa (letn� �as)
