# 2017.05.04 15:31:49 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/distutils/tests/test_bdist.py
"""Tests for distutils.command.bdist."""
import os
import unittest
from test.test_support import run_unittest
from distutils.command.bdist import bdist
from distutils.tests import support

class BuildTestCase(support.TempdirManager, unittest.TestCase):

    def test_formats(self):
        dist = self.create_dist()[1]
        cmd = bdist(dist)
        cmd.formats = ['msi']
        cmd.ensure_finalized()
        self.assertEqual(cmd.formats, ['msi'])
        formats = ['bztar',
         'gztar',
         'msi',
         'rpm',
         'tar',
         'wininst',
         'zip',
         'ztar']
        found = sorted(cmd.format_command)
        self.assertEqual(found, formats)

    def test_skip_build(self):
        dist = self.create_dist()[1]
        cmd = bdist(dist)
        cmd.skip_build = 1
        cmd.ensure_finalized()
        dist.command_obj['bdist'] = cmd
        names = ['bdist_dumb', 'bdist_wininst']
        if os.name == 'nt':
            names.append('bdist_msi')
        for name in names:
            subcmd = cmd.get_finalized_command(name)
            self.assertTrue(subcmd.skip_build, '%s should take --skip-build from bdist' % name)


def test_suite():
    return unittest.makeSuite(BuildTestCase)


if __name__ == '__main__':
    run_unittest(test_suite())
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\distutils\tests\test_bdist.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:31:49 St�edn� Evropa (letn� �as)
