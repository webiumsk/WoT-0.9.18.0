# 2017.05.04 15:33:47 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/plat-irix5/CL.py
from warnings import warnpy3k
warnpy3k('the CL module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
try:
    from cl import *
except ImportError:
    from CL_old import *
else:
    del CompressImage
    del DecompressImage
    del GetAlgorithmName
    del OpenCompressor
    del OpenDecompressor
    del QueryAlgorithms
    del QueryMaxHeaderSize
    del QueryScheme
    del QuerySchemeFromName
    del SetDefault
    del SetMax
    del SetMin
    try:
        del cvt_type
    except NameError:
        pass

    del error
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\plat-irix5\CL.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:33:47 Støední Evropa (letní èas)
