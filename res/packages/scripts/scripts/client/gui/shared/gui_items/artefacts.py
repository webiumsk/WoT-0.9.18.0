# 2017.05.04 15:25:50 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/artefacts.py
from debug_utils import LOG_CURRENT_EXCEPTION
from gui.shared.gui_items import FittingItem
from gui.shared.money import Currency
from items import artefacts

class VehicleArtefact(FittingItem):

    @property
    def icon(self):
        return self.descriptor.icon[0]

    def _getShortInfo(self, vehicle = None, expanded = False):
        return self.shortDescription

    @property
    def isStimulator(self):
        """ Is item stimulator which can increase crew role levels. """
        return isinstance(self.descriptor, artefacts.Stimulator)

    @property
    def crewLevelIncrease(self):
        """ Value of crew role levels increasing. """
        if not self.isStimulator:
            return 0
        return self.descriptor['crewLevelIncrease']

    @property
    def isRemovingStun(self):
        return False


class Equipment(VehicleArtefact):

    def _getAltPrice(self, buyPrice, proxy):
        """ Overridden method for receiving special action price value for shells
        @param buyPrice:
        @param proxy:
        @return: an instance of Money class
        """
        creditsPrice = buyPrice.exchange(Currency.GOLD, Currency.CREDITS, proxy.exchangeRateForShellsAndEqs)
        return buyPrice.replace(Currency.CREDITS, creditsPrice.credits)

    @property
    def icon(self):
        return '../maps/icons/artefact/%s.png' % super(Equipment, self).icon

    @property
    def tags(self):
        return self.descriptor.tags

    @property
    def defaultLayoutValue(self):
        return (self.intCD if not self.isBoughtForCredits else -self.intCD, 1)

    @property
    def isRemovingStun(self):
        descr = self.descriptor
        return bool(descr.stunResistanceEffect or descr.stunResistanceDuration)

    def isInstalled(self, vehicle, slotIdx = None):
        for idx, eq in enumerate(vehicle.eqs):
            if eq is not None and self.intCD == eq.intCD:
                if slotIdx is None:
                    return True
                return idx == slotIdx

        return super(Equipment, self).isInstalled(vehicle, slotIdx)

    def mayInstall(self, vehicle, slotIdx = None):
        for idx, eq in enumerate(vehicle.eqs):
            if slotIdx is not None and idx == slotIdx or eq is None:
                continue
            if eq.intCD != self.intCD:
                installPossible = eq.descriptor.checkCompatibilityWithActiveEquipment(self.descriptor)
                if installPossible:
                    installPossible = self.descriptor.checkCompatibilityWithEquipment(eq.descriptor)
                if not installPossible:
                    return (False, 'not with installed equipment')

        return self.descriptor.checkCompatibilityWithVehicle(vehicle.descriptor)

    def getInstalledVehicles(self, vehicles):
        result = set()
        for vehicle in vehicles:
            installed = map(lambda x: (x.intCD if x is not None else None), vehicle.eqs)
            if self.intCD in installed:
                result.add(vehicle)

        return result

    def getConflictedEquipments(self, vehicle):
        conflictEqs = list()
        if self in vehicle.eqs:
            return conflictEqs
        else:
            for e in vehicle.eqs:
                if e is not None:
                    compatibility = e.descriptor.checkCompatibilityWithActiveEquipment(self.descriptor)
                    if compatibility:
                        compatibility = self.descriptor.checkCompatibilityWithEquipment(e.descriptor)
                    if not compatibility:
                        conflictEqs.append(e)

            return conflictEqs

    def getGUIEmblemID(self):
        return super(Equipment, self).icon


class OptionalDevice(VehicleArtefact):

    def __init__(self, intCompactDescr, proxy = None, isBoughtForCredits = False):
        super(OptionalDevice, self).__init__(intCompactDescr, proxy, isBoughtForCredits)
        splitIcon = self.icon.split('/')
        labelWithExtension = splitIcon[len(splitIcon) - 1]
        label = labelWithExtension.split('.')[0]
        self.GUIEmblemID = label

    @property
    def isRemovable(self):
        return self.descriptor['removable']

    def isInstalled(self, vehicle, slotIdx = None):
        for idx, op in enumerate(vehicle.optDevices):
            if op is not None and self.intCD == op.intCD:
                if slotIdx is None:
                    return True
                return idx == slotIdx

        return super(OptionalDevice, self).isInstalled(vehicle, slotIdx)

    def mayInstall(self, vehicle, slotIdx):
        return vehicle.descriptor.mayInstallOptionalDevice(self.intCD, slotIdx)

    def mayRemove(self, vehicle):
        try:
            slotIdx = vehicle.optDevices.index(self)
            return vehicle.descriptor.mayRemoveOptionalDevice(slotIdx)
        except Exception:
            LOG_CURRENT_EXCEPTION()
            return (False, 'not installed on vehicle')

    def getInstalledVehicles(self, vehicles):
        result = set()
        for vehicle in vehicles:
            installed = map(lambda x: (x.intCD if x is not None else None), vehicle.optDevices)
            if self.intCD in installed:
                result.add(vehicle)

        return result

    def getGUIEmblemID(self):
        return self.GUIEmblemID
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\artefacts.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:25:50 St�edn� Evropa (letn� �as)
