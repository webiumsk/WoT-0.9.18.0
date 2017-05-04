# 2017.05.04 15:26:47 Støední Evropa (letní èas)
# Embedded file name: scripts/client/helpers/ro_property.py


def getMethod(name):

    def _getMethod(self):
        return self.__readonly__[name]

    return _getMethod


class ROPropertyMeta(type):

    def __new__(cls, className, bases, classDict):
        readonly = classDict.get('__readonly__', {})
        for name, default in readonly.items():
            classDict[name] = property(getMethod(name))

        return type.__new__(cls, className, bases, classDict)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\helpers\ro_property.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:47 Støední Evropa (letní èas)
