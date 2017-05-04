# 2017.05.04 15:28:49 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/dossiers2/common/utils.py
import dossiers2
import struct
__DOSSIER_CONSOLE_OUTPUT_FORMAT = '%s\n--------------------\n%s\n===================='

def printAccountDossier(accountDossierDescr):
    printDossierFromDescr(accountDossierDescr, dossiers2.getAccountDossierDescr, __DOSSIER_CONSOLE_OUTPUT_FORMAT)


def printVehicleDossier(vehicleDossierDescr):
    printDossierFromDescr(vehicleDossierDescr, dossiers2.getVehicleDossierDescr, __DOSSIER_CONSOLE_OUTPUT_FORMAT)


def printTankmanDossier(tankmanDossierDescr):
    printDossierFromDescr(tankmanDossierDescr, dossiers2.getTankmanDossierDescr, __DOSSIER_CONSOLE_OUTPUT_FORMAT)


def printFortifiedRegionsDossier(fortifiedRegionsDossierDescr):
    printDossierFromDescr(fortifiedRegionsDossierDescr, dossiers2.getFortifiedRegionsDossierDescr, __DOSSIER_CONSOLE_OUTPUT_FORMAT)


def printRated7x7Dossier(rated7x7DossierDescr):
    printDossierFromDescr(rated7x7DossierDescr, dossiers2.getRated7x7DossierDescr, __DOSSIER_CONSOLE_OUTPUT_FORMAT)


def printClubDossier(clubDossierDescr):
    printDossierFromDescr(clubDossierDescr, dossiers2.getClubDossierDescr, __DOSSIER_CONSOLE_OUTPUT_FORMAT)


def printDossierFromDescr(dossierDescr, dossierGetter, format):
    printDossier(dossierGetter(dossierDescr), format)


def printDossier(dossier, format):
    print '\n'.join(convertDossierToText(format, dossier))


def convertDossierToText(format, dossier):
    return [ format % (block, dossier[block]) for block in dossier._DossierDescr__blocksLayout ]


def getDossierVersion(dossierCompDescr, versionFormat, latestVersion):
    if dossierCompDescr == '':
        return latestVersion
    return struct.unpack_from(versionFormat, dossierCompDescr)[0]
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\dossiers2\common\utils.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:49 St�edn� Evropa (letn� �as)
