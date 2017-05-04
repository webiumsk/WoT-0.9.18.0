# 2017.05.04 15:23:40 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/messengerBar/VehicleCompareCartButton.py
from gui.Scaleform.daapi.view.meta.ButtonWithCounterMeta import ButtonWithCounterMeta
from helpers import dependency
from skeletons.gui.game_control import IVehicleComparisonBasket

class VehicleCompareCartButton(ButtonWithCounterMeta):
    comparisonBasket = dependency.descriptor(IVehicleComparisonBasket)

    def __init__(self):
        super(VehicleCompareCartButton, self).__init__()

    def _populate(self):
        super(VehicleCompareCartButton, self)._populate()
        self.comparisonBasket.onChange += self.__onCountChanged
        self.comparisonBasket.onSwitchChange += self.__onVehCmpBasketStateChanged
        self.__changeCount(self.comparisonBasket.getVehiclesCount())

    def _dispose(self):
        self.comparisonBasket.onChange -= self.__onCountChanged
        self.comparisonBasket.onSwitchChange -= self.__onVehCmpBasketStateChanged
        super(VehicleCompareCartButton, self)._dispose()

    def __onVehCmpBasketStateChanged(self):
        if not self.comparisonBasket.isEnabled():
            self.destroy()

    def __onCountChanged(self, _):
        """
        gui.game_control.VehComparisonBasket.onChange event handler
        :param _: instance of gui.game_control.veh_comparison_basket._ChangedData
        """
        self.__changeCount(self.comparisonBasket.getVehiclesCount())

    def __changeCount(self, count):
        self.as_setCountS(count)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\messengerBar\VehicleCompareCartButton.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:40 Støední Evropa (letní èas)
