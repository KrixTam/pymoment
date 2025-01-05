import unittest
from moment import moment
from datetime import timedelta
from dateutil.parser import parse


class TestSubOperator(unittest.TestCase):

    def test_day(self):
        a = moment('20201228').subtract(3, 'd')
        b = moment('20201228')
        c = 3 * 24 * 60 * 60 * 1000
        d = parse('2020-12-25T00:00:00+08:00')
        self.assertEqual(b - a, c)
        self.assertEqual(b - d, c)

    def test_second(self):
        a = moment('20201228').subtract(80, 's')
        b = moment('20201228')
        c = 80 * 1000
        d = parse('2020-12-27T23:58:40+08:00')
        self.assertEqual(b - a, c)
        self.assertEqual(b - d, c)

    def test_millisecond(self):
        a = moment('20201228').subtract(183, 'ms')
        b = moment('20201228')
        c = 183
        d = parse('2020-12-27 23:59:59.817000+08:00')
        self.assertEqual(b - a, c)
        self.assertEqual(b - d, c)

    def test_minute(self):
        a = moment('20201228').subtract(7, 'm')
        b = moment('20201228')
        c = 7 * 60 * 1000
        d = parse('2020-12-27T23:53:00+08:00')
        self.assertEqual(b - a, c)
        self.assertEqual(b - d, c)

    def test_hour(self):
        a = moment('20201228').subtract(13, 'h')
        b = moment('20201228')
        c = 13 * 60 * 60 * 1000
        d = parse('2020-12-27T11:00:00+08:00')
        self.assertEqual(b - a, c)
        self.assertEqual(b - d, c)

    def test_week(self):
        a = moment('20201228').subtract(5, 'w')
        b = moment('20201228')
        c = 5 * 7 * 24 * 60 * 60 * 1000
        d = parse('2020-11-23T00:00:00+08:00')
        self.assertEqual(b - a, c)
        self.assertEqual(b - d, c)

    def test_not_implement(self):
        with self.assertRaises(TypeError):
            a = moment('2021-4-2 04:02:09.957031 +0800')
            b = a - 2


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
