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
        self.assertTrue(a.isSame(b, 'year'))
        self.assertFalse(a.isSame('2022-1-1', 'year'))

    def test_month(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-1 0:0:0.0 +0800')
        self.assertTrue(a.isSame(b, 'month'))
        self.assertFalse(a.isSame('2021-1-1', 'month'))

    def test_quarter(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-1 0:0:0.0 +0800')
        self.assertTrue(a.isSame(b, 'quarter'))
        self.assertFalse(a.isSame('2021-01-22 04:02:09', 'quarter'))

    def test_week(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-18 0:0:0.0 +0800')
        self.assertTrue(a.isSame(b, 'week'))
        self.assertFalse(a.isSame('2021-04-28 04:02:09', 'week'))

    def test_isoWeek(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-19 0:0:0.0 +0800')
        self.assertTrue(a.isSame(b, 'isoWeek'))
        self.assertFalse(a.isSame('2021-04-28 04:02:09', 'isoWeek'))

    def test_day(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 0:0:0.0 +0800')
        self.assertTrue(a.isSame(b, 'day'))
        self.assertFalse(a.isSame('2021-04-21 04:02:09', 'day'))

    def test_date(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 0:0:0.0 +0800')
        self.assertTrue(a.isSame(b, 'date'))
        self.assertFalse(a.isSame('2021-04-21 04:02:09', 'date'))

    def test_hour(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:0:0.0 +0800')
        self.assertTrue(a.isSame(b, 'hour'))
        self.assertFalse(a.isSame('2021-04-22 05:02:09', 'hour'))

    def test_minute(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22  4:2:0.0 +0800')
        self.assertTrue(a.isSame(b, 'minute'))
        self.assertFalse(a.isSame('2021-04-22 04:12:09', 'minute'))

    def test_second(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22  4:2:9.0 +0800')
        self.assertTrue(a.isSame(b, 'second'))
        self.assertFalse(a.isSame('2021-04-22 04:2:19', 'second'))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
