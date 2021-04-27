# coding: utf-8

import unittest
from moment import moment


class TestEndOf(unittest.TestCase):

    def test_year(self):
        a = moment('2021-04-22 04:02:09.957000 +0800').endOf('year')
        b = moment('2021-2-2 13:02:09.957000 +0800').endOf('year')
        c = moment('2021-3-31 20:52:29.957000 +0800')
        c.endOf('year', inplace=True)
        self.assertEqual(a, b)
        self.assertEqual(a, c)
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-12-31 23:59:59.999999')

    def test_month(self):
        a = moment('2021-04-22 04:02:09.957000 +0800').endOf('month')
        b = moment('2021-4-2 13:02:09.957000 +0800').endOf('month')
        c = moment('2021-3-31 20:52:29.957000 +0800')
        c.endOf('month', inplace=True)
        self.assertEqual(a, b)
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-03-31 23:59:59.999999')

    def test_quarter(self):
        a = moment('2021-04-22 04:02:09.957000 +0800').endOf('quarter')
        b = moment('2021-4-2 13:02:09.957000 +0800').endOf('quarter')
        c = moment('2021-5-31 20:52:29.957000 +0800')
        c.endOf('quarter', inplace=True)
        self.assertEqual(a, b)
        self.assertEqual(a, c)
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-06-30 23:59:59.999999')

    def test_week(self):
        a = moment('2021-4-2 04:02:09.957000 +0800').endOf('week')
        b = moment('2021-3-29 13:02:09.957000 +0800').endOf('week')
        c = moment('2021-3-28 20:52:29.957000 +0800')
        c.endOf('week', inplace=True)
        self.assertEqual(a, b)
        self.assertEqual(a, c)
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-03 23:59:59.999999')

    def test_isoWeek(self):
        a = moment('2021-4-2 04:02:09.957000 +0800').endOf('isoWeek')
        b = moment('2021-3-29 13:02:09.957000 +0800').endOf('isoWeek')
        c = moment('2021-3-28 20:52:29.957000 +0800')
        c.endOf('isoWeek', inplace=True)
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-03-28 23:59:59.999999')

    def test_day(self):
        a = moment('2021-4-2 04:02:09.957000 +0800').endOf('day')
        b = moment('2021-4-02 13:02:09.957000 +0800').endOf('day')
        c = moment('2021-3-28 20:52:29.957000 +0800')
        c.endOf('day', inplace=True)
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-03-28 23:59:59.999999')

    def test_date(self):
        a = moment('2021-4-2 04:02:09.957000 +0800').endOf('date')
        b = moment('2021-4-02 13:02:09.957000 +0800').endOf('date')
        c = moment('2021-3-28 20:52:29.957000 +0800')
        c.endOf('date', inplace=True)
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-03-28 23:59:59.999999')

    def test_hour(self):
        a = moment('2021-4-2 04:02:09.957000 +0800').endOf('hour')
        b = moment('2021-4-02 13:02:09.957000 +0800').endOf('hour')
        c = moment('2021-3-28 20:52:29.957000 +0800')
        c.endOf('hour', inplace=True)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-02 04:59:59.999999')
        self.assertEqual(b.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-02 13:59:59.999999')
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-03-28 20:59:59.999999')

    def test_minute(self):
        a = moment('2021-4-2 04:02:09.957000 +0800').endOf('minute')
        b = moment('2021-4-02 13:02:09.957000 +0800').endOf('minute')
        c = moment('2021-3-28 20:52:29.957000 +0800')
        c.endOf('minute', inplace=True)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-02 04:02:59.999999')
        self.assertEqual(b.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-02 13:02:59.999999')
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-03-28 20:52:59.999999')

    def test_second(self):
        a = moment('2021-4-2 04:02:09.957000 +0800').endOf('second')
        b = moment('2021-4-02 13:02:09.957000 +0800').endOf('second')
        c = moment('2021-3-28 20:52:29.957000 +0800')
        c.endOf('second', inplace=True)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-02 04:02:09.999999')
        self.assertEqual(b.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-02 13:02:09.999999')
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-03-28 20:52:29.999999')


if __name__ == '__main__':
    unittest.main()
