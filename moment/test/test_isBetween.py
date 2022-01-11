import unittest
from moment import moment


class TestIsBetween(unittest.TestCase):

    def test_default(self):
        a = moment('20201231')
        b = moment('20201128')
        c = moment('20210429')
        self.assertTrue(a.isBetween(b, c))
        self.assertTrue(a.isBetween(c, b))
        self.assertFalse(b.isBetween(a, c))

    def test_year(self):
        a = moment('20201031')
        b = moment('20201128')
        c = moment('20210429')
        self.assertTrue(a.isBetween(b, c, 'year'))
        self.assertFalse(b.isBetween(a, c, 'year', True))

    def test_month(self):
        a = moment('20201115')
        b = moment('20201128')
        c = moment('20210429')
        self.assertTrue(a.isBetween(b, c, 'month'))
        self.assertFalse(b.isBetween(a, c, 'month', True))

    def test_quarter(self):
        a = moment('20201115')
        b = moment('20201128')
        c = moment('20210429')
        self.assertTrue(a.isBetween(b, c, 'quarter'))
        self.assertFalse(b.isBetween(a, c, 'quarter', True))

    def test_week(self):
        a = moment('20210426')
        b = moment('20210429')
        c = moment('20210502')
        self.assertTrue(a.isBetween(b, c, 'week'))
        self.assertFalse(b.isBetween(a, c, 'week', True))

    def test_isoWeek(self):
        a = moment('20210426')
        b = moment('20210430')
        c = moment('20210503')
        self.assertTrue(a.isBetween(b, c, 'isoWeek'))
        self.assertFalse(b.isBetween(a, c, 'isoWeek', True))

    def test_day(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 13:02:09.957000 +0800')
        c = moment('2021-4-23 13:02:09.957000 +0800')
        self.assertTrue(a.isBetween(b, c, 'day'))
        self.assertFalse(b.isBetween(a, c, 'day', True))

    def test_day(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 13:02:09.957000 +0800')
        c = moment('2021-4-23 13:02:09.957000 +0800')
        self.assertTrue(a.isBetween(b, c, 'date'))
        self.assertFalse(b.isBetween(a, c, 'date', True))

    def test_hour(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:22:09.957000 +0800')
        c = moment('2021-4-23 13:02:09.957000 +0800')
        self.assertTrue(a.isBetween(b, c, 'hour'))
        self.assertFalse(b.isBetween(a, c, 'hour', True))

    def test_minute(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:2:39.957000 +0800')
        c = moment('2021-4-22 4:3:09.957000 +0800')
        self.assertTrue(a.isBetween(b, c, 'minute'))
        self.assertFalse(b.isBetween(a, c, 'minute', True))

    def test_second(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:2:9.957000 +0800')
        c = moment('2021-4-22 4:3:00.957000 +0800')
        self.assertTrue(a.isBetween(b, c, 'second'))
        self.assertFalse(b.isBetween(a, c, 'second', True))


if __name__ == '__main__':
    unittest.main()
