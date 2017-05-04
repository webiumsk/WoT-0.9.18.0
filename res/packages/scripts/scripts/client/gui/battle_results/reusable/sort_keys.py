# 2017.05.04 15:21:25 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/battle_results/reusable/sort_keys.py
from gui.shared.gui_items import Vehicle
from gui.shared.sort_key import SortKey

class AchievementSortKey(SortKey):
    __slots__ = ('achievement',)

    def __init__(self, achievement):
        super(AchievementSortKey, self).__init__()
        self.achievement = achievement

    def _cmp(self, other):
        x = self.achievement[0]
        y = other.achievement[0]
        result = cmp(y.hasRibbon(), x.hasRibbon())
        if result:
            return result
        result = cmp(y.getUserName(), x.getUserName())
        if result:
            return result


class _VehicleSortKey(SortKey):
    __slots__ = ('info',)

    def __init__(self, vehicleInfo):
        super(_VehicleSortKey, self).__init__()
        self.info = vehicleInfo

    def _cmp(self, other):
        left = self.info.vehicle
        right = other.info.vehicle
        if left is not None:
            level = left.level
            classOrder = self.info.getOrderByClass()
            shortName = left.shortUserName
        else:
            level = -1
            classOrder = Vehicle.UNKNOWN_VEHICLE_CLASS_ORDER
            shortName = ''
        if right is not None:
            otherLevel = right.level
            otherClassOrder = other.info.getOrderByClass()
            otherShortName = right.shortUserName
        else:
            otherLevel = -1
            otherClassOrder = Vehicle.UNKNOWN_VEHICLE_CLASS_ORDER
            otherShortName = ''
        result = cmp(otherLevel, level)
        if result:
            return result
        result = cmp(classOrder, otherClassOrder)
        if result:
            return result
        result = cmp(shortName, otherShortName)
        if result:
            return result
        else:
            return


class VehicleInfoSortKey(_VehicleSortKey):
    __slots__ = ()

    def _cmp(self, other):
        result = super(VehicleInfoSortKey, self)._cmp(other)
        if result:
            return result
        return cmp(self.info.player.name, other.info.player.name)


class TeamItemSortKey(_VehicleSortKey):
    __slots__ = ()

    def _cmp(self, other):
        result = super(TeamItemSortKey, self)._cmp(other)
        if result:
            return -result
        return cmp(self.info.player.name, other.info.player.name)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\battle_results\reusable\sort_keys.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:25 St�edn� Evropa (letn� �as)
