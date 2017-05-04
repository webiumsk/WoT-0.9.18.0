# 2017.05.04 15:29:17 Støední Evropa (letní èas)
# Embedded file name: scripts/common/items/qualifiers/_xml.py
import expressions

def parseCondition(section):
    if not section.has_key('condition'):
        return (None, None)
    else:
        return expressions.parseExpression(section['condition'].asString)


def parseValue(section):
    if not section.has_key('value'):
        return (None, None)
    else:
        x = section['value'].asString.strip(' ')
        if x.endswith('%'):
            res = (True, int(x[:-1]))
        else:
            res = (False, int(x))
        return res
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\items\qualifiers\_xml.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:29:17 Støední Evropa (letní èas)
