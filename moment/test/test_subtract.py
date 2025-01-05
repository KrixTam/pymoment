import unittest
from moment import moment


class TestSubtract(unittest.TestCase):

    def test_year(self):
        self.assertTrue(moment('20201228').subtract(1, 'y') == moment('20201228').add(-1, 'years'))
        self.assertTrue(moment('20201228').subtract(-2.1, 'years') == moment('20201228').add(2.1, 'y'))

    def test_quarter(self):
        self.assertTrue(moment('20201228').subtract(1, 'Q') == moment('20201228').add(-1, 'quarters'))
        self.assertTrue(moment('20201228').subtract(-2.1, 'quarters') == moment('20201228').add(2.1, 'Q'))

    def test_month(self):
        self.assertTrue(moment('20201228').subtract(1, 'M') == moment('20201228').add(-1, 'months'))
        self.assertTrue(moment('20201228').subtract(-2.1, 'months') == moment('20201228').add(2.1, 'M'))

    def test_week(self):
        self.assertTrue(moment('20201228').subtract(1, 'w') == moment('20201228').add(-1, 'weeks'))
        self.assertTrue(moment('20201228').subtract(-2.1, 'weeks') == moment('20201228').add(2.1, 'w'))

    def test_day(self):
        self.assertTrue(moment('20201228').subtract(1, 'd') == moment('20201228').add(-1, 'days'))
        self.assertTrue(moment('20201228').subtract(-2.1, 'days') == moment('20201228').add(2.1, 'd'))

    def test_hour(self):
        self.assertTrue(moment('20201231T12').subtract(7, 'h') == moment('20201231T12').add(-7, 'hours'))
        self.assertTrue(moment('20201231T12').subtract(-3, 'hours') == moment('20201231T12').add(3, 'h'))

    def test_minute(self):
        self.assertTrue(moment('20201231T12').subtract(7, 'm') == moment('20201231T12').add(-7, 'minutes'))
        self.assertTrue(moment('20201231T12').subtract(-3, 'minutes') == moment('20201231T12').add(3, 'm'))

    def test_second(self):
        self.assertTrue(moment('20201231T12').subtract(7, 's') == moment('20201231T12').add(-7, 'seconds'))
        self.assertTrue(moment('20201231T12').subtract(-3, 'seconds') == moment('20201231T12').add(3, 's'))

    def test_millisecond(self):
        self.assertTrue(moment('20201231T12').subtract(7321321, 'ms') == moment('20201231T12').add(-7321321, 'milliseconds'))
        self.assertTrue(moment('20201231T12').subtract(-3123, 'milliseconds') == moment('20201231T12').add(3123, 'ms'))

    def test_inplace(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        b = a.subtract(13, 's', inplace=True)
        self.assertEqual(a, b)
        self.assertEqual(a.format('YYYY-MM-DD HH:mm:ss.SSSSSS'), '2021-04-22 04:01:56.957000')

    def test_error_01(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        with self.assertRaises(ValueError):
            a.subtract('13', 's')

    def test_error_02(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        with self.assertRaises(TypeError):
            a.subtract(13, 's', 1231)

    def test_error_03(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        with self.assertRaises(ValueError):
            a.subtract({'x': 12})

    def test_error_04(self):
        with self.assertRaises(ValueError):
            moment('20201228').subtract({'m': 21, 'x': 12, 'y': 3, 'd': -4})

    def test_error_05(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        with self.assertRaises(ValueError):
            a.subtract({'x': 12})

    def test_error_06(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        with self.assertRaises(TypeError):
            a.subtract([])

    def test_error_07(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        with self.assertRaises(ValueError):
            a.subtract({})

    def test_dict_01(self):
        a = moment('20201228').subtract({'y': 3})
        b = moment('20201228').subtract({'years': -1, 'd': -4})
        self.assertEqual(a.format('YYYY-MM-DD'), '2017-12-28')
        self.assertEqual(b.format('YYYY-MM-DD'), '2022-01-01')


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
