# coding: utf-8

import unittest
from moment import moment


class TestIsAfter(unittest.TestCase):

    def test_default(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-2-2 13:02:09.957000 +0800')
        self.assertFalse(a.isAfter([2021, 5, 1]))
        self.assertTrue(a.isAfter(b))

    def test_year(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-2-2 13:02:09.957000 +0800')
        self.assertTrue(a.isAfter(b, 'year'))
        self.assertFalse(a.isAfter(b, 'year', True))

    def test_month(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-2 13:02:09.957000 +0800')
        self.assertTrue(a.isAfter(b, 'month'))
        self.assertFalse(a.isAfter(b, 'month', True))

    def test_quarter(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-5-2 13:02:09.957000 +0800')
        self.assertTrue(a.isAfter(b, 'quarter'))
        self.assertFalse(a.isAfter(b, 'quarter', True))

    def test_week(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-21 13:02:09.957000 +0800')
        self.assertTrue(a.isAfter(b, 'week'))
        self.assertFalse(a.isAfter(b, 'week', True))

    def test_isoWeek(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-21 13:02:09.957000 +0800')
        self.assertTrue(a.isAfter(b, 'isoWeek'))
        self.assertFalse(a.isAfter(b, 'isoWeek', True))

    def test_day(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 13:02:09.957000 +0800')
        self.assertTrue(a.isAfter(b, 'day'))
        self.assertFalse(a.isAfter(b, 'day', True))

    def test_date(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 13:02:09.957000 +0800')
        self.assertTrue(a.isAfter(b, 'date'))
        self.assertFalse(a.isAfter(b, 'date', True))

    def test_hour(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:12:09.957000 +0800')
        self.assertTrue(a.isAfter(b, 'hour'))
        self.assertFalse(a.isAfter(b, 'hour', True))

    def test_minute(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:2:39.957000 +0800')
        self.assertTrue(a.isAfter(b, 'minute'))
        self.assertFalse(a.isAfter(b, 'minute', True))

    def test_second(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:2:9.957000 +0800')
        self.assertTrue(a.isAfter(b, 'second'))
        self.assertFalse(a.isAfter(b, 'second', True))


if __name__ == '__main__':
    unittest.main()
