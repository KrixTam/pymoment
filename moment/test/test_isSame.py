import unittest
from moment import moment


class TestIsSame(unittest.TestCase):

    def test_default(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-2-2 13:02:09.957000 +0800')
        self.assertTrue(a.isSame('2021-04-22 04:02:09.957000 +0800'))
        self.assertFalse(a.isSame(b))

    def test_year(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-1-1 0:0:0.0 +0800')
        self.assertFalse(a.isSame(b, 'year'))
        self.assertTrue(a.isSame(b, 'year', True))

    def test_month(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-1 0:0:0.0 +0800')
        self.assertFalse(a.isSame(b, 'month'))
        self.assertTrue(a.isSame(b, 'month', True))

    def test_quarter(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-1 0:0:0.0 +0800')
        self.assertFalse(a.isSame(b, 'quarter'))
        self.assertTrue(a.isSame(b, 'quarter', True))

    def test_week(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-18 0:0:0.0 +0800')
        self.assertFalse(a.isSame(b, 'week'))
        self.assertTrue(a.isSame(b, 'week', True))

    def test_isoWeek(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-19 0:0:0.0 +0800')
        self.assertFalse(a.isSame(b, 'isoWeek'))
        self.assertTrue(a.isSame(b, 'isoWeek', True))

    def test_day(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 0:0:0.0 +0800')
        self.assertFalse(a.isSame(b, 'day'))
        self.assertTrue(a.isSame(b, 'day', True))

    def test_date(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 0:0:0.0 +0800')
        self.assertFalse(a.isSame(b, 'date'))
        self.assertTrue(a.isSame(b, 'date', True))

    def test_hour(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:0:0.0 +0800')
        self.assertFalse(a.isSame(b, 'hour'))
        self.assertTrue(a.isSame(b, 'hour', True))

    def test_minute(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22  4:2:0.0 +0800')
        self.assertFalse(a.isSame(b, 'minute'))
        self.assertTrue(a.isSame(b, 'minute', True))

    def test_second(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22  4:2:9.0 +0800')
        self.assertFalse(a.isSame(b, 'second'))
        self.assertTrue(a.isSame(b, 'second', True))


if __name__ == '__main__':
    unittest.main()
