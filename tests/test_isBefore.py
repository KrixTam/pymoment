# coding: utf-8

import unittest
from moment import moment


class TestIsBefore(unittest.TestCase):

    def test_default(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-2-2 13:02:09.957000 +0800')
        self.assertTrue(a.isBefore([2021, 5, 1]))
        self.assertFalse(a.isBefore(b))

    def test_year(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-2-2 13:02:09.957000 +0800')
        self.assertFalse(a.isBefore(b, 'year'))
        self.assertTrue(a.isBefore(b, 'year', True))

    def test_month(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-2 13:02:09.957000 +0800')
        self.assertFalse(a.isBefore(b, 'month'))
        self.assertTrue(a.isBefore(b, 'month', True))

    def test_quarter(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-5-2 13:02:09.957000 +0800')
        self.assertFalse(a.isBefore(b, 'quarter'))
        self.assertTrue(a.isBefore(b, 'quarter', True))

    def test_week(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-21 13:02:09.957000 +0800')
        self.assertFalse(a.isBefore(b, 'week'))
        self.assertTrue(a.isBefore(b, 'week', True))

    def test_isoWeek(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-21 13:02:09.957000 +0800')
        self.assertFalse(a.isBefore(b, 'isoWeek'))
        self.assertTrue(a.isBefore(b, 'isoWeek', True))

    def test_day(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 13:02:09.957000 +0800')
        self.assertFalse(a.isBefore(b, 'day'))
        self.assertTrue(a.isBefore(b, 'day', True))

    def test_date(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 13:02:09.957000 +0800')
        self.assertFalse(a.isBefore(b, 'date'))
        self.assertTrue(a.isBefore(b, 'date', True))

    def test_hour(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:12:09.957000 +0800')
        self.assertFalse(a.isBefore(b, 'hour'))
        self.assertTrue(a.isBefore(b, 'hour', True))

    def test_minute(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:2:39.957000 +0800')
        self.assertFalse(a.isBefore(b, 'minute'))
        self.assertTrue(a.isBefore(b, 'minute', True))

    def test_second(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:2:9.957000 +0800')
        self.assertFalse(a.isBefore(b, 'second'))
        self.assertTrue(a.isBefore(b, 'second', True))


if __name__ == '__main__':
    unittest.main()
