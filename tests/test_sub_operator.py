# coding: utf-8

import unittest
from moment import moment
from datetime import timedelta
from dateutil.parser import parse


class TestSubOperator(unittest.TestCase):

    def test_day(self):
        a = moment('20201228').subtract(3, 'd')
        b = moment('20201228')
        c = timedelta(days=3)
        d = parse('2020-12-25T00:00:00+08:00')
        self.assertEqual(b - a, c)
        self.assertEqual(b - d, c)

    def test_second(self):
        a = moment('20201228').subtract(80, 's')
        b = moment('20201228')
        c = timedelta(seconds=80)
        d = parse('2020-12-27T23:58:40+08:00')
        self.assertEqual(b - a, c)
        self.assertEqual(b - d, c)

    def test_millisecond(self):
        a = moment('20201228').subtract(183, 'ms')
        b = moment('20201228')
        c = timedelta(milliseconds=183)
        d = parse('2020-12-27 23:59:59.817000+08:00')
        self.assertEqual(b - a, c)
        self.assertEqual(b - d, c)

    def test_minute(self):
        a = moment('20201228').subtract(7, 'm')
        b = moment('20201228')
        c = timedelta(minutes=7)
        d = parse('2020-12-27T23:53:00+08:00')
        self.assertEqual(b - a, c)
        self.assertEqual(b - d, c)

    def test_hour(self):
        a = moment('20201228').subtract(13, 'h')
        b = moment('20201228')
        c = timedelta(hours=13)
        d = parse('2020-12-27T11:00:00+08:00')
        self.assertEqual(b - a, c)
        self.assertEqual(b - d, c)

    def test_hour(self):
        a = moment('20201228').subtract(5, 'w')
        b = moment('20201228')
        c = timedelta(weeks=5)
        d = parse('2020-11-23T00:00:00+08:00')
        self.assertEqual(b - a, c)
        self.assertEqual(b - d, c)


if __name__ == '__main__':
    unittest.main()
