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
        a = moment('20191031')
        b = moment('20201128')
        c = moment('20210429')
        self.assertFalse(a.isBetween(b, c, 'year'))
        self.assertTrue(b.isBetween(a, c, 'year'))

    def test_month(self):
        a = moment('20201015')
        b = moment('20201128')
        c = moment('20210429')
        self.assertFalse(a.isBetween(b, c, 'month'))
        self.assertTrue(b.isBetween(a, c, 'month'))

    def test_quarter(self):
        a = moment('20200915')
        b = moment('20201128')
        c = moment('20210429')
        self.assertFalse(a.isBetween(b, c, 'quarter'))
        self.assertTrue(b.isBetween(a, c, 'quarter'))

    def test_week(self):
        a = moment('20210422')
        b = moment('20210429')
        c = moment('20210502')
        self.assertFalse(a.isBetween(b, c, 'week'))
        self.assertTrue(b.isBetween(a, c, 'week'))

    def test_isoWeek(self):
        a = moment('20210423')
        b = moment('20210430')
        c = moment('20210503')
        self.assertFalse(a.isBetween(b, c, 'isoWeek'))
        self.assertTrue(b.isBetween(a, c, 'isoWeek'))

    def test_day(self):
        a = moment('2021-04-21 04:02:09.957000 +0800')
        b = moment('2021-4-22 13:02:09.957000 +0800')
        c = moment('2021-4-23 13:02:09.957000 +0800')
        self.assertFalse(a.isBetween(b, c, 'day'))
        self.assertTrue(b.isBetween(a, c, 'day'))

    def test_date(self):
        a = moment('2021-04-21 04:02:09.957000 +0800')
        b = moment('2021-4-22 13:02:09.957000 +0800')
        c = moment('2021-4-23 13:02:09.957000 +0800')
        self.assertFalse(a.isBetween(b, c, 'date'))
        self.assertTrue(b.isBetween(a, c, 'date'))

    def test_hour(self):
        a = moment('2021-04-22 03:02:09.957000 +0800')
        b = moment('2021-4-22 4:22:09.957000 +0800')
        c = moment('2021-4-23 13:02:09.957000 +0800')
        self.assertFalse(a.isBetween(b, c, 'hour'))
        self.assertTrue(b.isBetween(a, c, 'hour'))

    def test_minute(self):
        a = moment('2021-04-22 04:01:09.957000 +0800')
        b = moment('2021-4-22 4:2:39.957000 +0800')
        c = moment('2021-4-22 4:3:09.957000 +0800')
        self.assertFalse(a.isBetween(b, c, 'minute'))
        self.assertTrue(b.isBetween(a, c, 'minute'))

    def test_second(self):
        a = moment('2021-04-22 04:02:08.957000 +0800')
        b = moment('2021-4-22 4:2:9.957000 +0800')
        c = moment('2021-4-22 4:3:00.957000 +0800')
        self.assertFalse(a.isBetween(b, c, 'second'))
        self.assertTrue(b.isBetween(a, c, 'second'))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
