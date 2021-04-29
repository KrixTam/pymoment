# coding: utf-8

import unittest
from moment import moment


class TestIsSameOrAfter(unittest.TestCase):

    def test_default(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-2-2 13:02:09.957000 +0800')
        self.assertFalse(a.isSameOrAfter([2021, 5, 1]))
        self.assertTrue(a.isSameOrAfter(b))
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-2-2 13:02:09.957000 +0800')
        self.assertTrue(a.isSameOrAfter('2021-04-22 04:02:09.957000 +0800'))
        self.assertTrue(a.isSameOrAfter(b))

    def test_year(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-2-2 13:02:09.957000 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'year'))
        self.assertFalse(a.isSameOrAfter(b, 'year', True))
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-1-1 0:0:0.0 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'year'))
        self.assertTrue(a.isSameOrAfter(b, 'year', True))

    def test_month(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-2 13:02:09.957000 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'month'))
        self.assertFalse(a.isSameOrAfter(b, 'month', True))
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-1 0:0:0.0 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'month'))
        self.assertTrue(a.isSameOrAfter(b, 'month', True))

    def test_quarter(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-5-2 13:02:09.957000 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'quarter'))
        self.assertFalse(a.isSameOrAfter(b, 'quarter', True))
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-1 0:0:0.0 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'quarter'))
        self.assertTrue(a.isSameOrAfter(b, 'quarter', True))

    def test_week(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-21 13:02:09.957000 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'week'))
        self.assertFalse(a.isSameOrAfter(b, 'week', True))
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-18 0:0:0.0 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'week'))
        self.assertTrue(a.isSameOrAfter(b, 'week', True))

    def test_isoWeek(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-21 13:02:09.957000 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'isoWeek'))
        self.assertFalse(a.isSameOrAfter(b, 'isoWeek', True))
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-19 0:0:0.0 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'isoWeek'))
        self.assertTrue(a.isSameOrAfter(b, 'isoWeek', True))

    def test_day(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 13:02:09.957000 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'day'))
        self.assertFalse(a.isSameOrAfter(b, 'day', True))
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 0:0:0.0 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'day'))
        self.assertTrue(a.isSameOrAfter(b, 'day', True))

    def test_date(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 13:02:09.957000 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'date'))
        self.assertFalse(a.isSameOrAfter(b, 'date', True))
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 0:0:0.0 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'date'))
        self.assertTrue(a.isSameOrAfter(b, 'date', True))

    def test_hour(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:12:09.957000 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'hour'))
        self.assertFalse(a.isSameOrAfter(b, 'hour', True))
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:0:0.0 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'hour'))
        self.assertTrue(a.isSameOrAfter(b, 'hour', True))

    def test_minute(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:2:39.957000 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'minute'))
        self.assertFalse(a.isSameOrAfter(b, 'minute', True))
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22  4:2:0.0 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'minute'))
        self.assertTrue(a.isSameOrAfter(b, 'minute', True))

    def test_second(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:2:9.957000 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'second'))
        self.assertFalse(a.isSameOrAfter(b, 'second', True))
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22  4:2:9.0 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'second'))
        self.assertTrue(a.isSameOrAfter(b, 'second', True))


if __name__ == '__main__':
    unittest.main()
