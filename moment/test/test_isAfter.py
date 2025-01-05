import unittest
from moment import moment


class TestIsAfter(unittest.TestCase):

    def test_default(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-2-2 13:02:09.957000 +0800')
        self.assertFalse(a.isAfter([2021, 5, 1]))
        self.assertTrue(a.isAfter(b))
        self.assertFalse(a.isAfter())

    def test_year(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-2-2 13:02:09.957000 +0800')
        self.assertFalse(a.isAfter(b, 'year'))
        self.assertTrue(a.isAfter([2020, 3, 8], 'year'))

    def test_month(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-2 13:02:09.957000 +0800')
        self.assertFalse(a.isAfter(b, 'month'))
        self.assertTrue(a.isAfter([2021, 3, 8], 'month'))

    def test_quarter(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-5-2 13:02:09.957000 +0800')
        self.assertFalse(a.isAfter(b, 'quarter'))
        self.assertTrue(a.isAfter([2021, 1, 8], 'month'))

    def test_week(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-21 13:02:09.957000 +0800')
        self.assertFalse(a.isAfter(b, 'week'))
        self.assertTrue(a.isAfter([2021, 3, 28], 'month'))

    def test_isoWeek(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-21 13:02:09.957000 +0800')
        self.assertFalse(a.isAfter(b, 'isoWeek'))
        self.assertTrue(a.isAfter([2021, 3, 28], 'isoWeek'))

    def test_day(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 13:02:09.957000 +0800')
        self.assertFalse(a.isAfter(b, 'day'))
        self.assertTrue(a.isAfter([2021, 4, 21], 'day'))

    def test_date(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 13:02:09.957000 +0800')
        self.assertFalse(a.isAfter(b, 'date'))
        self.assertTrue(a.isAfter('2021-04-21 23:58:09', 'date'))

    def test_hour(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:12:09.957000 +0800')
        self.assertFalse(a.isAfter(b, 'hour'))
        self.assertTrue(a.isAfter('2021-04-22 03:58:09', 'hour'))

    def test_minute(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:2:39.957000 +0800')
        self.assertFalse(a.isAfter(b, 'minute'))
        self.assertTrue(a.isAfter('2021-04-22 04:01:09', 'minute'))

    def test_second(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:2:9.957000 +0800')
        self.assertFalse(a.isAfter(b, 'second'))
        self.assertTrue(a.isAfter('2021-04-22 04:02:08', 'second'))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
