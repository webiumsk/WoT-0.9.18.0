# 2017.05.04 15:28:48 Støední Evropa (letní èas)
# Embedded file name: scripts/common/dossiers2/common/DossierBuilder.py
import struct
from DossierDescr import DossierDescr

class DossierBuilder(object):

    def __init__(self, blockBuilders, versionFormat, blockSizeFormat, version, updater, initializer):
        self.__blockBuilders = blockBuilders
        self.__versionFormat = versionFormat
        self.__headerFormat = '<' + versionFormat + blockSizeFormat * len(blockBuilders)
        self.__latestVersion = version
        self.__updater = updater
        self.__initializer = initializer
        self.__emptyCompDescr = struct.pack(self.__headerFormat, version, *([0] * len(blockBuilders)))

    def build(self, compDescr = ''):
        if compDescr == '':
            dossier = DossierDescr(self.__emptyCompDescr, self.__blockBuilders, self.__headerFormat)
            self.__initializer(dossier)
        else:
            version = struct.unpack_from(self.__versionFormat, compDescr)[0]
            compDescr = self.__updater.updateVersion(version, compDescr)
            dossier = DossierDescr(compDescr, self.__blockBuilders, self.__headerFormat)
        return dossier
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\dossiers2\common\DossierBuilder.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:48 Støední Evropa (letní èas)
