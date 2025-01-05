import unittest
from moment import moment


class TestDaysInYear(unittest.TestCase):

    def test_default(self):
        self.assertEqual(moment('20200213').daysInYear(), 366)
        self.assertEqual(moment('20210413').daysInYear(), 365)
        self.assertEqual(moment('20210813').daysInYear(), 365)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
