# 2017.05.04 15:28:36 Støední Evropa (letní èas)
# Embedded file name: scripts/common/LRUCache.py
import collections

class LRUCache(object):

    def __init__(self, limit):
        self.__cache = collections.OrderedDict()
        self.__limit = limit

    def get(self, key):
        try:
            value = self.__cache.pop(key)
            self.__cache[key] = value
            return value
        except KeyError:
            return None

        return None

    def peek(self, key):
        return self.__cache.get(key, None)

    def set(self, key, value):
        try:
            self.__cache.pop(key)
        except KeyError:
            if len(self.__cache) >= self.__limit:
                self.__cache.popitem(last=False)

        self.__cache[key] = value

    def pop(self, key):
        return self.__cache.pop(key, None)

    def clear(self):
        self.__cache.clear()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\LRUCache.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:36 Støední Evropa (letní èas)
