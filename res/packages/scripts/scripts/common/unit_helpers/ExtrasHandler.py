# 2017.05.04 15:34:49 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/unit_helpers/ExtrasHandler.py
import cPickle
from debug_utils import LOG_DEBUG_DEV

class EmptyExtrasHandler(object):

    def __init__(self, unit):
        pass

    def new(self, initial = None):
        result = {}
        if initial:
            result.update(initial)
        return result

    def pack(self, extras):
        return ''

    def unpack(self, extrasStr):
        return {}

    def reset(self, extras):
        return self.new()

    def updateUnitExtras(self, extras, updateStr):
        pass


class SimpleExtrasHandler(EmptyExtrasHandler):

    def pack(self, extras):
        return cPickle.dumps(extras, -1)

    def unpack(self, extrasStr):
        return cPickle.loads(extrasStr)

    def reset(self, extras):
        return extras

    def updateUnitExtras(self, extras, updateStr):
        update = cPickle.loads(updateStr)
        extras.update(update)


class ClanBattleExtrasHandler(SimpleExtrasHandler):

    def __init__(self, unit = None):
        self._unit = unit
        from unit_helpers.MsgProcessor import ClanBattleMgrMsgProcessor
        self._processor = ClanBattleMgrMsgProcessor(unit)

    def new(self, initial = None):
        result = {'battleID': 0,
         'scheduleTime': 0,
         'isBattleRound': 0,
         'prevBuildNum': 0,
         'currentBuildNum': 0,
         'roundStart': 0,
         'battleResultList': [],
         'isEnemyReadyForBattle': 0,
         'clanEquipments': None,
         'lastEquipRev': 0,
         'localizedData': None}
        if initial:
            result.update(initial)
        return result

    def updateUnitExtras(self, extras, updateStr):
        self._processor.unpackOps(updateStr)


class ClubExtrasHandler(SimpleExtrasHandler):

    def __init__(self, unit = None):
        self._unit = unit

    def new(self, initial = None):
        result = {'clubDBID': None,
         'divisionID': None,
         'clubName': None,
         'accDBIDtoRole': None,
         'isRatedBattle': True,
         'accDBIDtoClubTimestamp': None,
         'clubEmblemIDs': None,
         'mapID': None,
         'isEnemyReady': False,
         'isBaseDefence': None,
         'startTime': None}
        if initial:
            result.update(initial)
        return result

    def reset(self, extras):
        return {'clubDBID': extras['clubDBID'],
         'divisionID': extras['divisionID'],
         'clubName': extras['clubName'],
         'accDBIDtoRole': extras['accDBIDtoRole'],
         'isRatedBattle': extras['isRatedBattle'],
         'accDBIDtoClubTimestamp': extras['accDBIDtoClubTimestamp'],
         'clubEmblemIDs': extras['clubEmblemIDs'],
         'mapID': None,
         'isEnemyReady': False,
         'isBaseDefence': None,
         'startTime': extras['startTime']}

    def updateUnitExtras(self, extras, updateStr):
        update = cPickle.loads(updateStr)
        if isinstance(update, tuple):
            extras[update[0]] = update[1]
        else:
            extras.update(update)


class SortieExtrasHandler(SimpleExtrasHandler):

    def __init__(self, unit = None):
        self._unit = unit

    def new(self, initial = None):
        result = {'clanEquipments': None,
         'lastEquipRev': 0}
        if initial:
            result.update(initial)
        return result


class SquadExtrasHandler(SimpleExtrasHandler):
    pass


class ExternalExtrasHandler(SimpleExtrasHandler):

    def new(self, initial = None):
        result = {'rev': 1}
        if initial:
            result.update(initial)
        return result
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\unit_helpers\ExtrasHandler.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:34:49 St�edn� Evropa (letn� �as)
