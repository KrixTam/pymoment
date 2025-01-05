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
        self.assertTrue(a.isSameOrBefore())

    def test_year(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-2-2 13:02:09.957000 +0800')
        self.assertTrue(a.isSameOrBefore(b, 'year'))
        self.assertTrue(a.isSameOrBefore('2022-2-2 13:02:09', 'year'))
        self.assertFalse(a.isSameOrBefore('2020-2-2 13:02:09', 'year'))

    def test_month(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-2 13:02:09.957000 +0800')
        self.assertTrue(a.isSameOrBefore(b, 'month'))
        self.assertTrue(a.isSameOrBefore('2022-2-2 13:02:09', 'month'))
        self.assertFalse(a.isSameOrBefore('2020-2-2 13:02:09', 'month'))

    def test_quarter(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-5-2 13:02:09.957000 +0800')
        self.assertTrue(a.isSameOrBefore(b, 'quarter'))
        self.assertTrue(a.isSameOrBefore('2022-2-2 13:02:09', 'quarter'))
        self.assertFalse(a.isSameOrBefore('2020-2-2 13:02:09', 'quarter'))

    def test_week(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-21 13:02:09.957000 +0800')
        self.assertTrue(a.isSameOrBefore(b, 'week'))
        self.assertTrue(a.isSameOrBefore('2022-2-2 13:02:09', 'week'))
        self.assertFalse(a.isSameOrBefore('2020-2-2 13:02:09', 'week'))

    def test_isoWeek(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-21 13:02:09.957000 +0800')
        self.assertTrue(a.isSameOrBefore(b, 'isoWeek'))
        self.assertTrue(a.isSameOrBefore('2022-2-2 13:02:09', 'isoWeek'))
        self.assertFalse(a.isSameOrBefore('2020-2-2 13:02:09', 'isoWeek'))

    def test_day(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 13:02:09.957000 +0800')
        self.assertTrue(a.isSameOrBefore(b, 'day'))
        self.assertTrue(a.isSameOrBefore('2022-2-2 13:02:09', 'day'))
        self.assertFalse(a.isSameOrBefore('2020-2-2 13:02:09', 'day'))

    def test_date(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 13:02:09.957000 +0800')
        self.assertTrue(a.isSameOrBefore(b, 'date'))
        self.assertTrue(a.isSameOrBefore('2022-2-2 13:02:09', 'date'))
        self.assertFalse(a.isSameOrBefore('2020-2-2 13:02:09', 'date'))

    def test_hour(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:12:09.957000 +0800')
        self.assertTrue(a.isSameOrBefore(b, 'hour'))
        self.assertTrue(a.isSameOrBefore('2022-2-2 13:02:09', 'hour'))
        self.assertFalse(a.isSameOrBefore('2020-2-2 13:02:09', 'hour'))

    def test_minute(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:2:39.957000 +0800')
        self.assertTrue(a.isSameOrBefore(b, 'minute'))
        self.assertTrue(a.isSameOrBefore('2022-2-2 13:02:09', 'minute'))
        self.assertFalse(a.isSameOrBefore('2020-2-2 13:02:09', 'minute'))

    def test_second(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = moment('2021-4-22 4:2:9.957000 +0800')
        self.assertTrue(a.isSameOrBefore(b, 'second'))
        self.assertTrue(a.isSameOrBefore('2022-2-2 13:02:09', 'minute'))
        self.assertFalse(a.isSameOrBefore('2020-2-2 13:02:09', 'minute'))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
