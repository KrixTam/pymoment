import coverage
import unittest


def run_all_tests(test_modules):
    suite = unittest.TestSuite()
    for t in test_modules:
        try:
            # If the module defines a suite() function, call it to get the suite.
            mod = __import__(t, globals(), locals(), ['suite'])
            suite_fn = getattr(mod, 'suite')
            suite.addTest(suite_fn())
        except (ImportError, AttributeError):
            # else, just load all the test cases from the module.
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))
    unittest.TextTestRunner().run(suite)


test_modules = [
    'moment.test.test_add',
    'moment.test.test_add_operator',
    'moment.test.test_daysInMonth',
    'moment.test.test_daysInYear',
    'moment.test.test_endOf',
    'moment.test.test_format',
    'moment.test.test_get_and_set',
    'moment.test.test_isAfter',
    'moment.test.test_isBefore',
    'moment.test.test_isBetween',
    'moment.test.test_isLeapYear',
    'moment.test.test_isSame',
    'moment.test.test_isSameOrAfter',
    'moment.test.test_isSameOrBefore',
    'moment.test.test_startOf',
    'moment.test.test_sub_operator',
    'moment.test.test_subtract',
    'moment.test.test_unix',
]

# 执行测试用例
cov = coverage.Coverage()
cov.start()

run_all_tests(test_modules)

cov.stop()
cov.save()

cov.html_report(directory='htmlcov')