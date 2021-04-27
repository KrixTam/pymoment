# coding: utf-8

import unittest
from moment import moment


class TestAdd(unittest.TestCase):

    def test_year(self):
        a = moment('20201228').add(3, 'y')
        b = moment('20201228').add(-1, 'years')
        c = moment('20201228').add(-1.5, 'y')
        d = moment('20201231').add(3.2, 'years')
        self.assertEqual(a.format('YYYY-MM-DD'), '2023-12-28')
        self.assertEqual(b.format('YYYY-MM-DD'), '2019-12-28')
        self.assertEqual(c.format('YYYY-MM-DD'), '2019-06-28')
        self.assertEqual(d.format('YYYY-MM-DD'), '2024-02-29')

    def test_quarter(self):
        a = moment('20201228').add(3, 'quarters')
        b = moment('20201228').add(-1, 'Q')
        c = moment('20201228').add(-1.2, 'Q')
        d = moment('20201231').add(3.4, 'quarters')
        self.assertEqual(a.format('YYYY-MM-DD'), '2021-09-28')
        self.assertEqual(b.format('YYYY-MM-DD'), '2020-09-28')
        self.assertEqual(c.format('YYYY-MM-DD'), '2020-08-28')
        self.assertEqual(d.format('YYYY-MM-DD'), '2021-10-31')

    def test_month(self):
        a = moment('20201228').add(3, 'M')
        b = moment('20201228').add(-1, 'months')
        c = moment('20201228').add(-1.5, 'M')
        d = moment('20201231').add(2.2, 'months')
        self.assertEqual(a.format('YYYY-MM-DD'), '2021-03-28')
        self.assertEqual(b.format('YYYY-MM-DD'), '2020-11-28')
        self.assertEqual(c.format('YYYY-MM-DD'), '2020-10-28')
        self.assertEqual(d.format('YYYY-MM-DD'), '2021-02-28')

    def test_week(self):
        a = moment('20201228').add(3, 'w')
        b = moment('20201228').add(-1, 'weeks')
        c = moment('20201231').add(-43.7, 'w')
        d = moment('20201231').add(2.2, 'weeks')
        self.assertEqual(a.format('YYYY-MM-DD'), '2021-01-18')
        self.assertEqual(b.format('YYYY-MM-DD'), '2020-12-21')
        self.assertEqual(c.format('YYYY-MM-DD'), '2020-02-29')
        self.assertEqual(d.format('YYYY-MM-DD'), '2021-01-15')

    def test_day(self):
        a = moment('20201228').add(3, 'd')
        b = moment('20201228').add(-1, 'days')
        c = moment('20201228').add(4.6, 'days')
        d = moment('20201228').add(-5.5, 'd')
        self.assertEqual(a.format('YYYY-MM-DD'), '2020-12-31')
        self.assertEqual(b.format('YYYY-MM-DD'), '2020-12-27')
        self.assertEqual(c.format('YYYY-MM-DD'), '2021-01-02')
        self.assertEqual(d.format('YYYY-MM-DD'), '2020-12-22')

    def test_hour(self):
        a = moment('20201231T12').add(3, 'h')
        b = moment('20201231T12').add(-3, 'hours')
        c = moment('20201231T12').add(13, 'h')
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss'), '2020-12-31 15:00:00')
        self.assertEqual(b.format('YYYY-MM-DD HH:mm:ss'), '2020-12-31 09:00:00')
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss'), '2021-01-01 01:00:00')

    def test_minute(self):
        a = moment('20201231T12').add(3, 'm')
        b = moment('20201231T12').add(-9, 'minutes')
        c = moment('20201231T12').add(62, 'minutes')
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss'), '2020-12-31 12:03:00')
        self.assertEqual(b.format('YYYY-MM-DD HH:mm:ss'), '2020-12-31 11:51:00')
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss'), '2020-12-31 13:02:00')

    def test_second(self):
        a = moment('20201231T12').add(7, 's')
        b = moment('20201231T12').add(-91, 'seconds')
        c = moment('20201231T12').add(62, 's')
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss'), '2020-12-31 12:00:07')
        self.assertEqual(b.format('YYYY-MM-DD HH:mm:ss'), '2020-12-31 11:58:29')
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss'), '2020-12-31 12:01:02')

    def test_millisecond(self):
        a = moment('20201231T12').add(7, 'ms')
        b = moment('20201231T12').add(-912319, 'milliseconds')
        c = moment('20201231T12').add(62321321, 'ms')
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2020-12-31 12:00:00.007000')
        self.assertEqual(b.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2020-12-31 11:44:47.681000')
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-01-01 05:18:41.321000')

    def test_inplace(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = a.add(53, 's', inplace=True)
        self.assertEqual(a, b)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-22 04:03:02.957000')


if __name__ == '__main__':
    unittest.main()