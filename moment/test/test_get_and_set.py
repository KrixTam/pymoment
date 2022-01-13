import math
import unittest
from moment import moment
from moment.pymoment import EPOCH_MOMENT


class TestGetAndSet(unittest.TestCase):

    def test_millisecond(self):
        a = moment('2021-4-2 04:02:09.957031 +0800')
        self.assertEqual(a.millisecond(), a.milliseconds())
        self.assertEqual(a.millisecond(), 957)
        a.millisecond(204)
        self.assertEqual(a.millisecond(), 204)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-02 04:02:09.204000')
        a.millisecond(22304)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-02 04:02:31.304000')

    def test_second(self):
        a = moment('2021-4-2 04:02:09.957031 +0800')
        self.assertEqual(a.second(), a.seconds())
        self.assertEqual(a.second(), 9)
        a.second(43)
        self.assertEqual(a.second(), 43)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-02 04:02:43.957031')
        a.second(4567)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-02 05:18:07.957031')

    def test_minute(self):
        a = moment('2021-4-2 04:02:09.957031 +0800')
        self.assertEqual(a.minute(), a.minutes())
        self.assertEqual(a.minute(), 2)
        a.minute(43)
        self.assertEqual(a.minute(), 43)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-02 04:43:09.957031')
        a.minute(123)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-02 06:03:09.957031')

    def test_hour(self):
        a = moment('2021-4-2 04:02:09.957031 +0800')
        self.assertEqual(a.hour(), a.hours())
        self.assertEqual(a.hour(), 4)
        a.hour(13)
        self.assertEqual(a.hour(), 13)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-02 13:02:09.957031')
        a.hour(458)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-21 02:02:09.957031')

    def test_date(self):
        a = moment('2021-4-7 04:02:09.957031 +0800')
        self.assertEqual(a.date(), a.dates())
        self.assertEqual(a.date(), 7)
        a.date(13)
        self.assertEqual(a.date(), 13)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-13 04:02:09.957031')
        a.date(-58)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-02-01 04:02:09.957031')

    def test_day(self):
        a = moment('2021-04-27T12:42:14+08:00')
        self.assertEqual(a.day(), a.days())
        self.assertEqual(a.day(), 2)
        a.day(7)
        self.assertEqual(a.day(), 0)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-05-02 12:42:14.000000')
        a.day(-4)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-28 12:42:14.000000')

    def test_weekday(self):
        a = moment('2021-04-27T12:42:14+08:00')
        self.assertEqual(a.weekday(), 2)
        a.weekday(7)
        self.assertEqual(a.weekday(), 0)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-05-02 12:42:14.000000')
        a.weekday(-4)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-28 12:42:14.000000')
        # change the first day of the week to Monday
        a = moment('2021-04-27T12:42:14+08:00')
        a.locale({'dow': 1})
        self.assertEqual(a.weekday(), 1)
        a.weekday(7)
        self.assertEqual(a.weekday(), 0)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-05-03 12:42:14.000000')
        a.weekday(-4)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-29 12:42:14.000000')
        self.assertEqual(a.format('w'), '18')
        self.assertEqual(a.format('W'), '17')
        a.locale({'doy': 2})
        a.format('W')
        self.assertEqual(a.format('w'), '17')
        self.assertEqual(a.format('W'), '17')

    def test_isoWeekday(self):
        a = moment('2021-04-27T12:42:14+08:00')
        self.assertEqual(a.isoWeekday(), 2)
        a.isoWeekday(7)
        self.assertEqual(a.isoWeekday(), 7)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-05-02 12:42:14.000000')
        a.isoWeekday(-4)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-21 12:42:14.000000')
        a.isoWeekday(0)
        self.assertEqual(a.isoWeekday(), 7)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-18 12:42:14.000000')

    def test_dayOfYear(self):
        a = moment('2021-4-2 04:02:09.957031 +0800')
        self.assertEqual(a.dayOfYear(), 92)
        a.dayOfYear(67)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-03-08 04:02:09.957031')
        a.dayOfYear(-267)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2020-04-08 04:02:09.957031')

    def test_week(self):
        a = moment('2021-4-2 04:02:09.957031 +0800')
        self.assertEqual(a.week(), a.weeks())
        self.assertEqual(a.week(), 14)
        a.week(2)
        self.assertEqual(a.week(), 2)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-01-08 04:02:09.957031')
        a.week(0)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2020-12-25 04:02:09.957031')
        a.week(-9)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2019-10-25 04:02:09.957031')

    def test_isoWeek(self):
        a = moment('2021-4-2 04:02:09.957031 +0800')
        self.assertEqual(a.isoWeek(), a.isoWeeks())
        self.assertEqual(a.isoWeek(), 13)
        a.isoWeek(2)
        self.assertEqual(a.isoWeek(), 2)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-01-15 04:02:09.957031')
        a.isoWeek(0)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-01-01 04:02:09.957031')
        a.isoWeek(-9)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2019-10-25 04:02:09.957031')

    def test_month(self):
        a = moment('2021-4-2 04:02:09.957031 +0800')
        self.assertEqual(a.month(), a.months())
        self.assertEqual(a.month(), 3)
        a.month(2)
        self.assertEqual(a.month(), 2)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-03-02 04:02:09.957031')
        a.month(0)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-01-02 04:02:09.957031')
        a.month(-9)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2020-04-02 04:02:09.957031')

    def test_quarter(self):
        a = moment('2021-4-2 04:02:09.957031 +0800')
        self.assertEqual(a.quarter(), a.quarters())
        self.assertEqual(a.quarter(), 2)
        a.quarter(1)
        self.assertEqual(a.quarter(), 1)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-01-02 04:02:09.957031')
        a.quarter(0)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2020-10-02 04:02:09.957031')
        a.quarter(-9)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2017-07-02 04:02:09.957031')

    def test_year(self):
        a = moment('2021-4-2 04:02:09.957031 +0800')
        self.assertEqual(a.year(), a.years())
        self.assertEqual(a.year(), 2021)
        a.year(1)
        self.assertEqual(a.year(), 1)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '0001-04-02 04:02:09.957031')

    def test_error_year(self):
        with self.assertRaises(ValueError):
            a = moment()
            a.year(0)

    def test_weeksInYear(self):
        a = moment('2021-4-2 04:02:09.957031 +0800')
        self.assertEqual(a.weeksInYear(), 52)
        b = moment([2020, 2, 11])
        self.assertEqual(b.weeksInYear(), 52)

    def test_isoWeeksInYear(self):
        a = moment('2021-4-2 04:02:09.957031 +0800')
        self.assertEqual(a.isoWeeksInYear(), 52)
        b = moment([2020, 2, 11])
        self.assertEqual(b.isoWeeksInYear(), 53)
        c = moment([2019, 1, 2])
        self.assertEqual(c.isoWeeksInYear(), 52)

    def test_not_implement_01(self):
        with self.assertRaises(TypeError):
            a = moment('2021-4-2 04:02:09.957031 +0800')
            if a > 1:
                pass

    def test_not_implement_02(self):
        with self.assertRaises(TypeError):
            a = moment('2021-4-2 04:02:09.957031 +0800')
            if a >= 1:
                pass

    def test_not_implement_03(self):
        with self.assertRaises(TypeError):
            a = moment('2021-4-2 04:02:09.957031 +0800')
            if a < 1:
                pass

    def test_not_implement_04(self):
        with self.assertRaises(TypeError):
            a = moment('2021-4-2 04:02:09.957031 +0800')
            if a <= 1:
                pass

    def test_not_implement_05(self):
        a = moment('2021-4-2 04:02:09.957031 +0800')
        self.assertEqual(a.__eq__(1), NotImplemented)

    def test_not_implement_06(self):
        a = moment('2021-4-2 04:02:09.957031 +0800')
        self.assertEqual(a.__ne__(1), NotImplemented)

    def test_repr(self):
        self.assertEqual(EPOCH_MOMENT.__repr__(), 'moment("2020-12-21 00:00:00.000000 +08:00")')

    def test_constructor_01(self):
        a = moment([2021, 12])
        b = moment([2021, 12, 1])
        self.assertEqual(a, b)

    def test_constructor_02(self):
        a = moment()
        b = moment([])
        self.assertEqual(math.floor(b - a), 0)

    def test_error_constructor_01(self):
        with self.assertRaises(ValueError):
            a = moment([2011, 11, 11, 1, 1, 1, 1, 0, 0, 0])

    def test_error_constructor_02(self):
        with self.assertRaises(TypeError):
            a = moment(2021)

    def test_tz(self):
        a = moment('2021-4-2 04:02:09.957031 +0000')
        # for moment.js "a.format()" should return '2021-04-02T12:02:09+08:00'
        # self.assertEqual(a.format(), '2021-04-02T12:02:09+08:00')
        # but for this python version, it would return '2021-04-02T04:02:09+00:00'
        self.assertEqual(a.format(), '2021-04-02T04:02:09+00:00')

    def test_getLocaleFirstDayOfYear(self):
        a = moment('2021-4-2 04:02:09.957031 +0800')
        self.assertEqual(a.getLocaleFirstDayOfYear(), 6)

    def test_zerofill(self):
        a = moment('2021-4-2 04:02:09.95 -2:00')


if __name__ == '__main__':
    unittest.main()
