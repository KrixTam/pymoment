import unittest
from moment import moment


class TestIsSameOrBefore(unittest.TestCase):

    def test_default(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-2-2 13:02:09.957000 +0800')
        self.assertTrue(a.isSameOrBefore([2021, 5, 1]))
        self.assertFalse(a.isSameOrBefore(b))
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-2-2 13:02:09.957000 +0800')
        self.assertTrue(a.isSameOrBefore('2021-04-22 04:02:09.957000 +0800'))
        self.assertFalse(a.isSameOrBefore(b))

    def test_year(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-2-2 13:02:09.957000 +0800')
        self.assertFalse(a.isSameOrBefore(b, 'year'))
        self.assertTrue(a.isSameOrBefore(b, 'year', True))
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-1-1 0:0:0.0 +0800')
        self.assertFalse(a.isSameOrBefore(b, 'year'))
        self.assertTrue(a.isSameOrBefore(b, 'year', True))

    def test_month(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-2 13:02:09.957000 +0800')
        self.assertFalse(a.isSameOrBefore(b, 'month'))
        self.assertTrue(a.isSameOrBefore(b, 'month', True))
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-1 0:0:0.0 +0800')
        self.assertFalse(a.isSameOrBefore(b, 'month'))
        self.assertTrue(a.isSameOrBefore(b, 'month', True))

    def test_quarter(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-5-2 13:02:09.957000 +0800')
        self.assertFalse(a.isSameOrBefore(b, 'quarter'))
        self.assertTrue(a.isSameOrBefore(b, 'quarter', True))
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-1 0:0:0.0 +0800')
        self.assertFalse(a.isSameOrBefore(b, 'quarter'))
        self.assertTrue(a.isSameOrBefore(b, 'quarter', True))

    def test_week(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-21 13:02:09.957000 +0800')
        self.assertFalse(a.isSameOrBefore(b, 'week'))
        self.assertTrue(a.isSameOrBefore(b, 'week', True))
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-18 0:0:0.0 +0800')
        self.assertFalse(a.isSameOrBefore(b, 'week'))
        self.assertTrue(a.isSameOrBefore(b, 'week', True))

    def test_isoWeek(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-21 13:02:09.957000 +0800')
        self.assertFalse(a.isSameOrBefore(b, 'isoWeek'))
        self.assertTrue(a.isSameOrBefore(b, 'isoWeek', True))
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-19 0:0:0.0 +0800')
        self.assertFalse(a.isSameOrBefore(b, 'isoWeek'))
        self.assertTrue(a.isSameOrBefore(b, 'isoWeek', True))

    def test_day(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 13:02:09.957000 +0800')
        self.assertFalse(a.isSameOrBefore(b, 'day'))
        self.assertTrue(a.isSameOrBefore(b, 'day', True))
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 0:0:0.0 +0800')
        self.assertFalse(a.isSameOrBefore(b, 'day'))
        self.assertTrue(a.isSameOrBefore(b, 'day', True))

    def test_date(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 13:02:09.957000 +0800')
        self.assertFalse(a.isSameOrBefore(b, 'date'))
        self.assertTrue(a.isSameOrBefore(b, 'date', True))
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 0:0:0.0 +0800')
        self.assertFalse(a.isSameOrBefore(b, 'date'))
        self.assertTrue(a.isSameOrBefore(b, 'date', True))

    def test_hour(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:12:09.957000 +0800')
        self.assertFalse(a.isSameOrBefore(b, 'hour'))
        self.assertTrue(a.isSameOrBefore(b, 'hour', True))
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:0:0.0 +0800')
        self.assertFalse(a.isSameOrBefore(b, 'hour'))
        self.assertTrue(a.isSameOrBefore(b, 'hour', True))

    def test_minute(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:2:39.957000 +0800')
        self.assertFalse(a.isSameOrBefore(b, 'minute'))
        self.assertTrue(a.isSameOrBefore(b, 'minute', True))
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22  4:2:0.0 +0800')
        self.assertFalse(a.isSameOrBefore(b, 'minute'))
        self.assertTrue(a.isSameOrBefore(b, 'minute', True))

    def test_second(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:2:9.957000 +0800')
        self.assertFalse(a.isSameOrBefore(b, 'second'))
        self.assertTrue(a.isSameOrBefore(b, 'second', True))
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22  4:2:9.0 +0800')
        self.assertFalse(a.isSameOrBefore(b, 'second'))
        self.assertTrue(a.isSameOrBefore(b, 'second', True))


if __name__ == '__main__':
    unittest.main()
