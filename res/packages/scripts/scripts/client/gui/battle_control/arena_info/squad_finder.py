# 2017.05.04 15:21:08 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/battle_control/arena_info/squad_finder.py
from collections import defaultdict
from gui.battle_control.arena_info import settings

class ISquadFinder(object):
    __slots__ = ()

    def clear(self):
        raise NotImplementedError

    def addVehicleInfo(self, team, prebattleID, vehicleID):
        raise NotImplementedError

    def getNumberOfSquadmen(self, team, prebattleID):
        raise NotImplementedError

    def getNumberOfSquads(self):
        raise NotImplementedError

    def findSquads(self):
        raise NotImplementedError


class EmptySquadFinder(ISquadFinder):
    __slots__ = ()

    def clear(self):
        pass

    def addVehicleInfo(self, team, prebattleID, vehicleID):
        pass

    def getNumberOfSquadmen(self, team, prebattleID):
        return 0

    def getNumberOfSquads(self):
        return 0

    def findSquads(self):
        return []


class _SquadFinder(ISquadFinder):
    __slots__ = ('_prbStats',)

    def __init__(self, teams):
        super(_SquadFinder, self).__init__()
        self._prbStats = {team:defaultdict(set) for team in teams}

    def clear(self):
        for stats in self._prbStats.itervalues():
            stats.clear()

    def addVehicleInfo(self, team, prebattleID, vehicleID):
        if not prebattleID:
            return
        self._prbStats[team][prebattleID].add(vehicleID)

    def getNumberOfSquadmen(self, team, prebattleID):
        return len(self._prbStats[team][prebattleID])

    def getNumberOfSquads(self):
        raise NotImplementedError

    def findSquads(self):
        raise NotImplementedError


class TeamScopeNumberingFinder(_SquadFinder):
    __slots__ = ('_teamsSquadIndices',)

    def __init__(self, teams):
        super(TeamScopeNumberingFinder, self).__init__(teams)
        self._teamsSquadIndices = {team:{} for team in teams}

    def clear(self):
        for indices in self._teamsSquadIndices.itervalues():
            indices.clear()

        super(TeamScopeNumberingFinder, self).clear()

    def getNumberOfSquads(self):
        return sum((max(indices.itervalues()) for indices in self._teamsSquadIndices.itervalues() if indices))

    def findSquads(self):
        for teamID, team in self._prbStats.iteritems():
            squadIndices = self._teamsSquadIndices[teamID]
            squads = filter(lambda item: len(item[1]) in settings.SQUAD_RANGE_TO_SHOW, team.iteritems())
            if not squads:
                continue
            squads = sorted(squads, key=lambda item: item[0])
            for prebattleID, vehiclesIDs in squads:
                if prebattleID not in squadIndices:
                    if squadIndices:
                        squadIndices[prebattleID] = max(squadIndices.itervalues()) + 1
                    else:
                        squadIndices[prebattleID] = 1
                for vehicleID in vehiclesIDs:
                    yield (vehicleID, squadIndices[prebattleID])


class ContinuousNumberingFinder(_SquadFinder):
    __slots__ = ('_squadIndices',)

    def __init__(self, teams):
        super(ContinuousNumberingFinder, self).__init__(teams)
        self._squadIndices = {}

    def clear(self):
        self._squadIndices.clear()
        super(ContinuousNumberingFinder, self).clear()

    def getNumberOfSquads(self):
        if self._squadIndices:
            return max(self._squadIndices.itervalues())
        return 0

    def findSquads(self):
        for teamID, team in self._prbStats.iteritems():
            for prebattleID, vehiclesIDs in team.iteritems():
                if not vehiclesIDs or len(vehiclesIDs) not in settings.SQUAD_RANGE_TO_SHOW:
                    continue
                if prebattleID not in self._squadIndices:
                    if self._squadIndices:
                        self._squadIndices[prebattleID] = max(self._squadIndices.itervalues()) + 1
                    else:
                        self._squadIndices[prebattleID] = 1
                for vehicleID in vehiclesIDs:
                    yield (vehicleID, self._squadIndices[prebattleID])


def createSquadFinder(arenaVisitor):
    teams = arenaVisitor.type.getTeamsOnArenaRange()
    guiVisitor = arenaVisitor.gui
    if guiVisitor.isRandomBattle() or guiVisitor.isEventBattle() or guiVisitor.isFalloutClassic():
        finder = TeamScopeNumberingFinder(teams)
    elif guiVisitor.isFalloutMultiTeam():
        finder = ContinuousNumberingFinder(teams)
    else:
        finder = EmptySquadFinder()
    return finder
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\battle_control\arena_info\squad_finder.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:09 St�edn� Evropa (letn� �as)
