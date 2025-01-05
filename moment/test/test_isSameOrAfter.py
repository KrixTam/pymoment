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
        self.assertFalse(a.isSameOrAfter())

    def test_year(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-2-2 13:02:09.957000 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'year'))
        self.assertTrue(a.isSameOrAfter('2020-2-2 13:02:09', 'year'))
        self.assertFalse(a.isSameOrAfter('2022-2-2 13:02:09', 'year'))

    def test_month(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-2 13:02:09.957000 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'month'))
        self.assertTrue(a.isSameOrAfter('2021-2-2 13:02:09', 'month'))
        self.assertFalse(a.isSameOrAfter('2022-2-2 13:02:09', 'month'))

    def test_quarter(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-5-2 13:02:09.957000 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'quarter'))
        self.assertTrue(a.isSameOrAfter('2021-2-2 13:02:09', 'quarter'))
        self.assertFalse(a.isSameOrAfter('2022-2-2 13:02:09', 'quarter'))

    def test_week(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-21 13:02:09.957000 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'week'))
        self.assertTrue(a.isSameOrAfter('2021-4-2 13:02:09', 'week'))
        self.assertFalse(a.isSameOrAfter('2022-2-2 13:02:09', 'week'))

    def test_isoWeek(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-21 13:02:09.957000 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'isoWeek'))
        self.assertTrue(a.isSameOrAfter('2021-4-2 13:02:09', 'isoWeek'))
        self.assertFalse(a.isSameOrAfter('2022-2-2 13:02:09', 'isoWeek'))

    def test_day(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 13:02:09.957000 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'day'))
        self.assertTrue(a.isSameOrAfter('2021-4-21 13:02:09', 'day'))
        self.assertFalse(a.isSameOrAfter('2022-2-2 13:02:09', 'day'))

    def test_date(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 13:02:09.957000 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'date'))
        self.assertTrue(a.isSameOrAfter('2021-4-21 13:02:09', 'date'))
        self.assertFalse(a.isSameOrAfter('2022-2-2 13:02:09', 'date'))

    def test_hour(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:12:09.957000 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'hour'))
        self.assertTrue(a.isSameOrAfter('2021-4-21 13:02:09', 'hour'))
        self.assertFalse(a.isSameOrAfter('2021-4-22 13:02:09', 'hour'))

    def test_minute(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:2:39.957000 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'minute'))
        self.assertTrue(a.isSameOrAfter('2021-4-21 04:02', 'minute'))
        self.assertFalse(a.isSameOrAfter('2021-4-22 13:02:09', 'minute'))

    def test_second(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:2:9.957000 +0800')
        self.assertTrue(a.isSameOrAfter(b, 'second'))
        self.assertTrue(a.isSameOrAfter('2021-4-22 04:02', 'second'))
        self.assertFalse(a.isSameOrAfter('2021-4-22 13:02:09', 'second'))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
