# 2017.05.04 15:23:53 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/rally/__init__.py
__author__ = 'd_dichkovsky'

class NavigationStack(object):
    __stacks = {}

    @classmethod
    def clear(cls, key):
        if key in cls.__stacks:
            cls.__stacks[key] = []

    @classmethod
    def exclude(cls, key, flashAlias):
        items = cls.__stacks.get(key, [])[:]
        for item in items:
            if item[0] == flashAlias:
                cls.__stacks[key].remove(item)

    @classmethod
    def hasHistory(cls, key):
        if key in cls.__stacks:
            return len(cls.__stacks[key])
        return 0

    @classmethod
    def current(cls, key):
        if key in cls.__stacks and len(cls.__stacks[key]):
            return cls.__stacks[key][-1]
        else:
            return None

    @classmethod
    def prev(cls, key):
        if key in cls.__stacks and len(cls.__stacks[key]) > 1:
            return cls.__stacks[key][-2]
        else:
            return None

    @classmethod
    def nav2Next(cls, key, flashAlias, pyAlias, itemID):
        item = (flashAlias, pyAlias, itemID)
        if key in cls.__stacks:
            if item not in cls.__stacks[key]:
                cls.__stacks[key].append(item)
        else:
            cls.__stacks[key] = [item]

    @classmethod
    def nav2Prev(cls, key):
        if key in cls.__stacks and len(cls.__stacks[key]):
            return cls.__stacks[key].pop()
        else:
            return None
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\rally\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:53 St�edn� Evropa (letn� �as)
