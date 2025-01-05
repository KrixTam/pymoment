import unittest
from moment import moment


class TestDaysInMonth(unittest.TestCase):

    def test_default(self):
        self.assertEqual(moment('20200213').daysInMonth(), 29)
        self.assertEqual(moment('20210413').daysInMonth(), 30)
        self.assertEqual(moment('20210813').daysInMonth(), 31)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
