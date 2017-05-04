# 2017.05.04 15:31:50 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/distutils/tests/test_bdist_msi.py
"""Tests for distutils.command.bdist_msi."""
import sys
import unittest
from test.test_support import run_unittest
from distutils.tests import support

@unittest.skipUnless(sys.platform == 'win32', 'these tests require Windows')

class BDistMSITestCase(support.TempdirManager, support.LoggingSilencer, unittest.TestCase):

    def test_minimal(self):
        from distutils.command.bdist_msi import bdist_msi
        project_dir, dist = self.create_dist()
        cmd = bdist_msi(dist)
        cmd.ensure_finalized()


def test_suite():
    return unittest.makeSuite(BDistMSITestCase)


if __name__ == '__main__':
    run_unittest(test_suite())
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\distutils\tests\test_bdist_msi.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:31:50 St�edn� Evropa (letn� �as)
