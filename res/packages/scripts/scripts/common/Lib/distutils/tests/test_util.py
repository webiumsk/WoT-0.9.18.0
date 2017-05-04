# 2017.05.04 15:31:56 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/distutils/tests/test_util.py
"""Tests for distutils.util."""
import sys
import unittest
from test.test_support import run_unittest
from distutils.errors import DistutilsByteCompileError
from distutils.util import byte_compile, grok_environment_error

class UtilTestCase(unittest.TestCase):

    def test_dont_write_bytecode(self):
        old_dont_write_bytecode = sys.dont_write_bytecode
        sys.dont_write_bytecode = True
        try:
            self.assertRaises(DistutilsByteCompileError, byte_compile, [])
        finally:
            sys.dont_write_bytecode = old_dont_write_bytecode

    def test_grok_environment_error(self):
        exc = IOError('Unable to find batch file')
        msg = grok_environment_error(exc)
        self.assertEqual(msg, 'error: Unable to find batch file')


def test_suite():
    return unittest.makeSuite(UtilTestCase)


if __name__ == '__main__':
    run_unittest(test_suite())
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\distutils\tests\test_util.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:31:56 Støední Evropa (letní èas)
