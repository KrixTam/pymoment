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
        ori = moment('20201228')
        a = ori.add(3, 'd')
        b = ori.add(-1, 'days')
        c = ori.add(4.6, 'days')
        d = ori.add(-5.5, 'd', inplace=True)
        self.assertEqual(a.format('YYYY-MM-DD'), '2020-12-31')
        self.assertEqual(b.format('YYYY-MM-DD'), '2020-12-27')
        self.assertEqual(c.format('YYYY-MM-DD'), '2021-01-02')
        self.assertEqual(d.format('YYYY-MM-DD'), '2020-12-22')
        self.assertEqual(d, ori)

    def test_hour(self):
        ori = moment('20201231T12')
        a = ori.add(3, 'h')
        b = ori.add(-3, 'hours')
        c = ori.add(13, 'h', inplace=True)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss'), '2020-12-31 15:00:00')
        self.assertEqual(b.format('YYYY-MM-DD HH:mm:ss'), '2020-12-31 09:00:00')
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss'), '2021-01-01 01:00:00')
        self.assertEqual(c, ori)

    def test_minute(self):
        ori = moment('20201231T12')
        a = ori.add(3, 'm')
        b = ori.add(-9, 'minutes')
        c = ori.add(62, 'minutes', inplace=True)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss'), '2020-12-31 12:03:00')
        self.assertEqual(b.format('YYYY-MM-DD HH:mm:ss'), '2020-12-31 11:51:00')
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss'), '2020-12-31 13:02:00')
        self.assertEqual(c, ori)

    def test_second(self):
        a = moment('20201231T12').add(7, 's')
        b = moment('20201231T12').add(-91, 'seconds')
        c = moment('20201231T12').add(62, 's')
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss'), '2020-12-31 12:00:07')
        self.assertEqual(b.format('YYYY-MM-DD HH:mm:ss'), '2020-12-31 11:58:29')
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss'), '2020-12-31 12:01:02')

    def test_millisecond(self):
        ori = moment('20201231T12')
        a = ori.add(7, 'ms')
        b = ori.add(-912319, 'milliseconds')
        c = ori.add(62321321, 'ms', inplace=True)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2020-12-31 12:00:00.007000')
        self.assertEqual(b.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2020-12-31 11:44:47.681000')
        self.assertEqual(c.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-01-01 05:18:41.321000')
        self.assertEqual(c, ori)

    def test_inplace(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = a.add(53, 's', inplace=True)
        self.assertEqual(a, b)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-22 04:03:02.957000')

    def test_error_01(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        with self.assertRaises(ValueError):
            a.add('123', 'days')

    def test_error_02(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        with self.assertRaises(ValueError):
            a.add(12.3, 'h')

    def test_error_03(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        with self.assertRaises(ValueError):
            a.add(12.3, 'm')

    def test_error_04(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        with self.assertRaises(ValueError):
            a.add(12.3, 's')

    def test_error_05(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        with self.assertRaises(ValueError):
            a.add(12.3, 'ms')

    def test_error_06(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        with self.assertRaises(ValueError):
            a.add('123', 'y')

    def test_error_07(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        with self.assertRaises(ValueError):
            a.add('123', 'Q')

    def test_error_08(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        with self.assertRaises(ValueError):
            a.add('123', 'M')

    def test_error_09(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        with self.assertRaises(ValueError):
            a.add('123', 'w')

    def test_error_10(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        with self.assertRaises(ValueError):
            a.add(123, 'x')

    def test_error_11(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        with self.assertRaises(TypeError):
            a.add(13, 's', 1231)

    def test_error_12(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        with self.assertRaises(ValueError):
            a.add({})

    def test_error_13(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        with self.assertRaises(ValueError):
            a.add({'x': 12})

    def test_error_14(self):
        with self.assertRaises(ValueError):
            moment('20201228').add({'m': 21, 'x': 12, 'y': 3, 'd': -4})

    def test_error_15(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        with self.assertRaises(ValueError):
            a.add({'x': 12})

    def test_error_16(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        with self.assertRaises(TypeError):
            a.add([])

    def test_dict_01(self):
        a = moment('20201228').add({'y': 3})
        b = moment('20201228').add({'years': -1, 'd': -4})
        self.assertEqual(a.format('YYYY-MM-DD'), '2023-12-28')
        self.assertEqual(b.format('YYYY-MM-DD'), '2019-12-24')


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
