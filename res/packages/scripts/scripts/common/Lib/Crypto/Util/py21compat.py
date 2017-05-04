# 2017.05.04 15:31:18 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/Crypto/Util/py21compat.py
"""Compatibility code for Python 2.1

Currently, this just defines:
    - True and False
    - object
    - isinstance
"""
__revision__ = '$Id$'
__all__ = []
import sys
import __builtin__
try:
    (True, False)
except NameError:
    True, False = (1, 0)
    __all__ += ['True', 'False']

try:
    object
except NameError:

    class object:
        pass


    __all__ += ['object']

try:
    isinstance(5, (int, long))
except TypeError:
    __all__ += ['isinstance']
    _builtin_type_map = {tuple: type(()),
     list: type([]),
     str: type(''),
     unicode: type(u''),
     int: type(0),
     long: type(0L)}

    def isinstance(obj, t):
        if not __builtin__.isinstance(t, type(())):
            return __builtin__.isinstance(obj, _builtin_type_map.get(t, t))
        else:
            for typ in t:
                if __builtin__.isinstance(obj, _builtin_type_map.get(typ, typ)):
                    return True

            return False


try:

    class A:

        def a():
            pass

        a = staticmethod(a)


except NameError:

    class staticmethod:

        def __init__(self, anycallable):
            self.__call__ = anycallable


    __all__ += ['staticmethod']
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\Crypto\Util\py21compat.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:31:19 St�edn� Evropa (letn� �as)
