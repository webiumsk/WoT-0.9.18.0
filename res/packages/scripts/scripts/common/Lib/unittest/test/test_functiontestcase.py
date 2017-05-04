# 2017.05.04 15:34:37 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/unittest/test/test_functiontestcase.py
import unittest
from .support import LoggingResult

class Test_FunctionTestCase(unittest.TestCase):

    def test_countTestCases(self):
        test = unittest.FunctionTestCase(lambda : None)
        self.assertEqual(test.countTestCases(), 1)

    def test_run_call_order__error_in_setUp(self):
        events = []
        result = LoggingResult(events)

        def setUp():
            events.append('setUp')
            raise RuntimeError('raised by setUp')

        def test():
            events.append('test')

        def tearDown():
            events.append('tearDown')

        expected = ['startTest',
         'setUp',
         'addError',
         'stopTest']
        unittest.FunctionTestCase(test, setUp, tearDown).run(result)
        self.assertEqual(events, expected)

    def test_run_call_order__error_in_test(self):
        events = []
        result = LoggingResult(events)

        def setUp():
            events.append('setUp')

        def test():
            events.append('test')
            raise RuntimeError('raised by test')

        def tearDown():
            events.append('tearDown')

        expected = ['startTest',
         'setUp',
         'test',
         'addError',
         'tearDown',
         'stopTest']
        unittest.FunctionTestCase(test, setUp, tearDown).run(result)
        self.assertEqual(events, expected)

    def test_run_call_order__failure_in_test(self):
        events = []
        result = LoggingResult(events)

        def setUp():
            events.append('setUp')

        def test():
            events.append('test')
            self.fail('raised by test')

        def tearDown():
            events.append('tearDown')

        expected = ['startTest',
         'setUp',
         'test',
         'addFailure',
         'tearDown',
         'stopTest']
        unittest.FunctionTestCase(test, setUp, tearDown).run(result)
        self.assertEqual(events, expected)

    def test_run_call_order__error_in_tearDown(self):
        events = []
        result = LoggingResult(events)

        def setUp():
            events.append('setUp')

        def test():
            events.append('test')

        def tearDown():
            events.append('tearDown')
            raise RuntimeError('raised by tearDown')

        expected = ['startTest',
         'setUp',
         'test',
         'tearDown',
         'addError',
         'stopTest']
        unittest.FunctionTestCase(test, setUp, tearDown).run(result)
        self.assertEqual(events, expected)

    def test_id(self):
        test = unittest.FunctionTestCase(lambda : None)
        self.assertIsInstance(test.id(), basestring)

    def test_shortDescription__no_docstring(self):
        test = unittest.FunctionTestCase(lambda : None)
        self.assertEqual(test.shortDescription(), None)
        return

    def test_shortDescription__singleline_docstring(self):
        desc = 'this tests foo'
        test = unittest.FunctionTestCase(lambda : None, description=desc)
        self.assertEqual(test.shortDescription(), 'this tests foo')


if __name__ == '__main__':
    unittest.main()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\unittest\test\test_functiontestcase.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:34:37 St�edn� Evropa (letn� �as)
