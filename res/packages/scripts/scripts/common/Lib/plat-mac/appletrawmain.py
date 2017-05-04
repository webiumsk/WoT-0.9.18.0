# 2017.05.04 15:33:57 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/plat-mac/appletrawmain.py
from warnings import warnpy3k
warnpy3k('In 3.x, the appletrawmain module is removed.', stacklevel=2)
import argvemulator
import os
import sys
import marshal
if not sys.argv or sys.argv[0][:1] == '-':
    _dir = os.path.split(sys.executable)[0]
    _dir = os.path.split(_dir)[0]
    _dir = os.path.join(_dir, 'Resources')
    sys.argv.insert(0, '__rawmain__')
else:
    _dir = os.path.split(sys.argv[0])[0]
sys.path.insert(0, _dir)
argvemulator.ArgvCollector().mainloop()
__file__ = os.path.join(_dir, '__main__.py')
if os.path.exists(__file__):
    sys.argv[0] = __file__
    del argvemulator
    del os
    del sys
    del _dir
    execfile(__file__)
else:
    __file__ = os.path.join(_dir, '__main__.pyc')
    if os.path.exists(__file__):
        sys.argv[0] = __file__
        _fp = open(__file__, 'rb')
        _fp.read(8)
        __code__ = marshal.load(_fp)
        del argvemulator
        del os
        del sys
        del marshal
        del _dir
        del _fp
        exec __code__
    else:
        sys.stderr.write('%s: neither __main__.py nor __main__.pyc found\n' % sys.argv[0])
        sys.exit(1)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\plat-mac\appletrawmain.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:33:57 Støední Evropa (letní èas)
