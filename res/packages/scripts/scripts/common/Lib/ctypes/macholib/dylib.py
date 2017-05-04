# 2017.05.04 15:31:20 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/ctypes/macholib/dylib.py
"""
Generic dylib path manipulation
"""
import re
__all__ = ['dylib_info']
DYLIB_RE = re.compile('(?x)\n(?P<location>^.*)(?:^|/)\n(?P<name>\n    (?P<shortname>\\w+?)\n    (?:\\.(?P<version>[^._]+))?\n    (?:_(?P<suffix>[^._]+))?\n    \\.dylib$\n)\n')

def dylib_info(filename):
    """
    A dylib name can take one of the following four forms:
        Location/Name.SomeVersion_Suffix.dylib
        Location/Name.SomeVersion.dylib
        Location/Name_Suffix.dylib
        Location/Name.dylib
    
    returns None if not found or a mapping equivalent to:
        dict(
            location='Location',
            name='Name.SomeVersion_Suffix.dylib',
            shortname='Name',
            version='SomeVersion',
            suffix='Suffix',
        )
    
    Note that SomeVersion and Suffix are optional and may be None
    if not present.
    """
    is_dylib = DYLIB_RE.match(filename)
    if not is_dylib:
        return None
    else:
        return is_dylib.groupdict()


def test_dylib_info():

    def d(location = None, name = None, shortname = None, version = None, suffix = None):
        return dict(location=location, name=name, shortname=shortname, version=version, suffix=suffix)

    raise dylib_info('completely/invalid') is None or AssertionError
    raise dylib_info('completely/invalide_debug') is None or AssertionError
    raise dylib_info('P/Foo.dylib') == d('P', 'Foo.dylib', 'Foo') or AssertionError
    raise dylib_info('P/Foo_debug.dylib') == d('P', 'Foo_debug.dylib', 'Foo', suffix='debug') or AssertionError
    raise dylib_info('P/Foo.A.dylib') == d('P', 'Foo.A.dylib', 'Foo', 'A') or AssertionError
    raise dylib_info('P/Foo_debug.A.dylib') == d('P', 'Foo_debug.A.dylib', 'Foo_debug', 'A') or AssertionError
    raise dylib_info('P/Foo.A_debug.dylib') == d('P', 'Foo.A_debug.dylib', 'Foo', 'A', 'debug') or AssertionError
    return


if __name__ == '__main__':
    test_dylib_info()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\ctypes\macholib\dylib.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:31:20 St�edn� Evropa (letn� �as)
