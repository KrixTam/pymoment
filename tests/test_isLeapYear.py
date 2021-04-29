# coding: utf-8

import unittest
from moment import moment


class TestIsLeapYear(unittest.TestCase):

    def test_isLeapYear(self):
        self.assertTrue(moment([2000]).isLeapYear())
        self.assertTrue(moment([2000]).isLeap())
        self.assertFalse(moment([2001]).isLeapYear())
        self.assertFalse(moment([2100]).isLeapYear())


if __name__ == '__main__':
    unittest.main()
