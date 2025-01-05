import unittest
from moment import moment


class TestStartOf(unittest.TestCase):

    def test_year(self):
        a = moment('2021-04-22 04:02:09.957000 +0800').startOf('year')
        b = moment('2021-2-2 13:02:09.957000 +0800').startOf('year')
        c = moment('2021-3-31 20:52:29.957000 +0800')
        c.startOf('year', inplace=True)
        self.assertEqual(a, b)
        self.assertEqual(a, c)
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-01-01 00:00:00.000000')

    def test_month(self):
        a = moment('2021-04-22 04:02:09.957000 +0800').startOf('month')
        b = moment('2021-4-2 13:02:09.957000 +0800').startOf('month')
        c = moment('2021-3-31 20:52:29.957000 +0800')
        c.startOf('month', inplace=True)
        self.assertEqual(a, b)
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-03-01 00:00:00.000000')

    def test_quarter(self):
        a = moment('2021-04-22 04:02:09.957000 +0800').startOf('quarter')
        b = moment('2021-4-2 13:02:09.957000 +0800').startOf('quarter')
        c = moment('2021-5-31 20:52:29.957000 +0800')
        c.startOf('quarter', inplace=True)
        self.assertEqual(a, b)
        self.assertEqual(a, c)
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-01 00:00:00.000000')

    def test_week(self):
        a = moment('2021-4-2 04:02:09.957000 +0800').startOf('week')
        b = moment('2021-3-29 13:02:09.957000 +0800').startOf('week')
        c = moment('2021-3-28 20:52:29.957000 +0800')
        c.startOf('week', inplace=True)
        self.assertEqual(a, b)
        self.assertEqual(a, c)
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-03-28 00:00:00.000000')

    def test_isoWeek(self):
        a = moment('2021-4-2 04:02:09.957000 +0800').startOf('isoWeek')
        b = moment('2021-3-29 13:02:09.957000 +0800').startOf('isoWeek')
        c = moment('2021-3-28 20:52:29.957000 +0800')
        c.startOf('isoWeek', inplace=True)
        d = moment('2021-4-5 04:02:09.957000 +0800')
        d.startOf('isoWeek', inplace=True)
        e = a.add(7, 'd')
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-03-22 00:00:00.000000')
        self.assertEqual(d, e)

    def test_day(self):
        a = moment('2021-4-2 04:02:09.957000 +0800').startOf('day')
        b = moment('2021-4-02 13:02:09.957000 +0800').startOf('day')
        c = moment('2021-3-28 20:52:29.957000 +0800')
        c.startOf('day', inplace=True)
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-03-28 00:00:00.000000')

    def test_date(self):
        a = moment('2021-4-2 04:02:09.957000 +0800').startOf('date')
        b = moment('2021-4-02 13:02:09.957000 +0800').startOf('date')
        c = moment('2021-3-28 20:52:29.957000 +0800')
        c.startOf('date', inplace=True)
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-03-28 00:00:00.000000')

    def test_hour(self):
        a = moment('2021-4-2 04:02:09.957000 +0800').startOf('hour')
        b = moment('2021-4-02 13:02:09.957000 +0800').startOf('hour')
        c = moment('2021-3-28 20:52:29.957000 +0800')
        c.startOf('hour', inplace=True)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-02 04:00:00.000000')
        self.assertEqual(b.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-02 13:00:00.000000')
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-03-28 20:00:00.000000')

    def test_minute(self):
        a = moment('2021-4-2 04:02:09.957000 +0800').startOf('minute')
        b = moment('2021-4-02 13:02:09.957000 +0800').startOf('minute')
        c = moment('2021-3-28 20:52:29.957000 +0800')
        c.startOf('minute', inplace=True)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-02 04:02:00.000000')
        self.assertEqual(b.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-02 13:02:00.000000')
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-03-28 20:52:00.000000')

    def test_second(self):
        a = moment('2021-4-2 04:02:09.957000 +0800').startOf('second')
        b = moment('2021-4-02 13:02:09.957000 +0800').startOf('second')
        c = moment('2021-3-28 20:52:29.957000 +0800')
        c.startOf('second', inplace=True)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-02 04:02:09.000000')
        self.assertEqual(b.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-02 13:02:09.000000')
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-03-28 20:52:29.000000')

    def test_error(self):
        with self.assertRaises(ValueError):
            moment('2021-4-2 04:02:09.957000 +0800').startOf('ms')


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
