# 2017.05.04 15:21:37 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/doc_loaders/__init__.py
from items import _xml

def readDict(xmlCtx, section, subsectionName, converter = lambda value: value.asString):
    result = {}
    for name, value in _xml.getChildren(xmlCtx, section, subsectionName):
        result[name] = converter(value)

    return result
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\doc_loaders\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:37 Støední Evropa (letní èas)
