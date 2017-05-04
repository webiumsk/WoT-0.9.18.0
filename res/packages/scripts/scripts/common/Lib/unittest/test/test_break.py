# 2017.05.04 15:34:37 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/unittest/test/test_break.py
import gc
import os
import sys
import signal
import weakref
from cStringIO import StringIO
import unittest

@unittest.skipUnless(hasattr(os, 'kill'), 'Test requires os.kill')

@unittest.skipIf(sys.platform == 'win32', 'Test cannot run on Windows')

@unittest.skipIf(sys.platform == 'freebsd6', 'Test kills regrtest on freebsd6 if threads have been used')

class TestBreak(unittest.TestCase):
    int_handler = None

    def setUp(self):
        self._default_handler = signal.getsignal(signal.SIGINT)
        if self.int_handler is not None:
            signal.signal(signal.SIGINT, self.int_handler)
        return

    def tearDown(self):
        signal.signal(signal.SIGINT, self._default_handler)
        unittest.signals._results = weakref.WeakKeyDictionary()
        unittest.signals._interrupt_handler = None
        return

    def testInstallHandler(self):
        default_handler = signal.getsignal(signal.SIGINT)
        unittest.installHandler()
        self.assertNotEqual(signal.getsignal(signal.SIGINT), default_handler)
        try:
            pid = os.getpid()
            os.kill(pid, signal.SIGINT)
        except KeyboardInterrupt:
            self.fail('KeyboardInterrupt not handled')

        self.assertTrue(unittest.signals._interrupt_handler.called)

    def testRegisterResult(self):
        result = unittest.TestResult()
        unittest.registerResult(result)
        for ref in unittest.signals._results:
            if ref is result:
                break
            elif ref is not result:
                self.fail('odd object in result set')
        else:
            self.fail('result not found')

    def testInterruptCaught(self):
        default_handler = signal.getsignal(signal.SIGINT)
        result = unittest.TestResult()
        unittest.installHandler()
        unittest.registerResult(result)
        self.assertNotEqual(signal.getsignal(signal.SIGINT), default_handler)

        def test(result):
            pid = os.getpid()
            os.kill(pid, signal.SIGINT)
            result.breakCaught = True
            self.assertTrue(result.shouldStop)

        try:
            test(result)
        except KeyboardInterrupt:
            self.fail('KeyboardInterrupt not handled')

        self.assertTrue(result.breakCaught)

    def testSecondInterrupt(self):
        if signal.getsignal(signal.SIGINT) == signal.SIG_IGN:
            self.skipTest('test requires SIGINT to not be ignored')
        result = unittest.TestResult()
        unittest.installHandler()
        unittest.registerResult(result)

        def test(result):
            pid = os.getpid()
            os.kill(pid, signal.SIGINT)
            result.breakCaught = True
            self.assertTrue(result.shouldStop)
            os.kill(pid, signal.SIGINT)
            self.fail('Second KeyboardInterrupt not raised')

        try:
            test(result)
        except KeyboardInterrupt:
            pass
        else:
            self.fail('Second KeyboardInterrupt not raised')

        self.assertTrue(result.breakCaught)

    def testTwoResults(self):
        unittest.installHandler()
        result = unittest.TestResult()
        unittest.registerResult(result)
        new_handler = signal.getsignal(signal.SIGINT)
        result2 = unittest.TestResult()
        unittest.registerResult(result2)
        self.assertEqual(signal.getsignal(signal.SIGINT), new_handler)
        result3 = unittest.TestResult()

        def test(result):
            pid = os.getpid()
            os.kill(pid, signal.SIGINT)

        try:
            test(result)
        except KeyboardInterrupt:
            self.fail('KeyboardInterrupt not handled')

        self.assertTrue(result.shouldStop)
        self.assertTrue(result2.shouldStop)
        self.assertFalse(result3.shouldStop)

    def testHandlerReplacedButCalled(self):
        if signal.getsignal(signal.SIGINT) == signal.SIG_IGN:
            self.skipTest('test requires SIGINT to not be ignored')
        unittest.installHandler()
        handler = signal.getsignal(signal.SIGINT)

        def new_handler(frame, signum):
            handler(frame, signum)

        signal.signal(signal.SIGINT, new_handler)
        try:
            pid = os.getpid()
            os.kill(pid, signal.SIGINT)
        except KeyboardInterrupt:
            pass
        else:
            self.fail("replaced but delegated handler doesn't raise interrupt")

    def testRunner(self):
        runner = unittest.TextTestRunner(stream=StringIO())
        result = runner.run(unittest.TestSuite())
        self.assertIn(result, unittest.signals._results)

    def testWeakReferences(self):
        result = unittest.TestResult()
        unittest.registerResult(result)
        ref = weakref.ref(result)
        del result
        gc.collect()
        gc.collect()
        self.assertIsNone(ref())

    def testRemoveResult(self):
        result = unittest.TestResult()
        unittest.registerResult(result)
        unittest.installHandler()
        self.assertTrue(unittest.removeResult(result))
        self.assertFalse(unittest.removeResult(unittest.TestResult()))
        try:
            pid = os.getpid()
            os.kill(pid, signal.SIGINT)
        except KeyboardInterrupt:
            pass

        self.assertFalse(result.shouldStop)

    def testMainInstallsHandler(self):
        failfast = object()
        test = object()
        verbosity = object()
        result = object()
        default_handler = signal.getsignal(signal.SIGINT)

        class FakeRunner(object):
            initArgs = []
            runArgs = []

            def __init__(self, *args, **kwargs):
                self.initArgs.append((args, kwargs))

            def run(self, test):
                self.runArgs.append(test)
                return result

        class Program(unittest.TestProgram):

            def __init__(self, catchbreak):
                self.exit = False
                self.verbosity = verbosity
                self.failfast = failfast
                self.catchbreak = catchbreak
                self.testRunner = FakeRunner
                self.test = test
                self.result = None
                return

        p = Program(False)
        p.runTests()
        self.assertEqual(FakeRunner.initArgs, [((), {'buffer': None,
           'verbosity': verbosity,
           'failfast': failfast})])
        self.assertEqual(FakeRunner.runArgs, [test])
        self.assertEqual(p.result, result)
        self.assertEqual(signal.getsignal(signal.SIGINT), default_handler)
        FakeRunner.initArgs = []
        FakeRunner.runArgs = []
        p = Program(True)
        p.runTests()
        self.assertEqual(FakeRunner.initArgs, [((), {'buffer': None,
           'verbosity': verbosity,
           'failfast': failfast})])
        self.assertEqual(FakeRunner.runArgs, [test])
        self.assertEqual(p.result, result)
        self.assertNotEqual(signal.getsignal(signal.SIGINT), default_handler)
        return

    def testRemoveHandler(self):
        default_handler = signal.getsignal(signal.SIGINT)
        unittest.installHandler()
        unittest.removeHandler()
        self.assertEqual(signal.getsignal(signal.SIGINT), default_handler)
        unittest.removeHandler()
        self.assertEqual(signal.getsignal(signal.SIGINT), default_handler)

    def testRemoveHandlerAsDecorator(self):
        default_handler = signal.getsignal(signal.SIGINT)
        unittest.installHandler()

        @unittest.removeHandler
        def test():
            self.assertEqual(signal.getsignal(signal.SIGINT), default_handler)

        test()
        self.assertNotEqual(signal.getsignal(signal.SIGINT), default_handler)


@unittest.skipUnless(hasattr(os, 'kill'), 'Test requires os.kill')

@unittest.skipIf(sys.platform == 'win32', 'Test cannot run on Windows')

@unittest.skipIf(sys.platform == 'freebsd6', 'Test kills regrtest on freebsd6 if threads have been used')

class TestBreakDefaultIntHandler(TestBreak):
    int_handler = signal.default_int_handler


@unittest.skipUnless(hasattr(os, 'kill'), 'Test requires os.kill')

@unittest.skipIf(sys.platform == 'win32', 'Test cannot run on Windows')

@unittest.skipIf(sys.platform == 'freebsd6', 'Test kills regrtest on freebsd6 if threads have been used')

class TestBreakSignalIgnored(TestBreak):
    int_handler = signal.SIG_IGN


@unittest.skipUnless(hasattr(os, 'kill'), 'Test requires os.kill')

@unittest.skipIf(sys.platform == 'win32', 'Test cannot run on Windows')

@unittest.skipIf(sys.platform == 'freebsd6', 'Test kills regrtest on freebsd6 if threads have been used')

class TestBreakSignalDefault(TestBreak):
    int_handler = signal.SIG_DFL
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\unittest\test\test_break.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:34:37 St�edn� Evropa (letn� �as)
