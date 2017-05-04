# 2017.05.04 15:33:12 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_getcwdu.py
"""
Fixer that changes os.getcwdu() to os.getcwd().
"""
from .. import fixer_base
from ..fixer_util import Name

class FixGetcwdu(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n              power< 'os' trailer< dot='.' name='getcwdu' > any* >\n              "

    def transform(self, node, results):
        name = results['name']
        name.replace(Name(u'getcwd', prefix=name.prefix))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\lib2to3\fixes\fix_getcwdu.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:33:12 Støední Evropa (letní èas)
