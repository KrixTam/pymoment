import unittest
from moment import moment
from datetime import timedelta


class TestAddOperator(unittest.TestCase):

    def test_day(self):
        a = moment('20201228').add(3, 'd')
        b = moment('20201228') + timedelta(days=3)
        self.assertEqual(a, b)

    def test_second(self):
        a = moment('20201228').add(80, 's')
        b = moment('20201228') + timedelta(seconds=80)
        self.assertEqual(a, b)

    def test_millisecond(self):
        a = moment('20201228').add(183, 'ms')
        b = moment('20201228') + timedelta(milliseconds=183)
        self.assertEqual(a, b)

    def test_minute(self):
        a = moment('20201228').add(7, 'm')
        b = moment('20201228') + timedelta(minutes=7)
        self.assertEqual(a, b)

    def test_hour(self):
        a = moment('20201228').add(13, 'h')
        b = moment('20201228') + timedelta(hours=13)
        self.assertEqual(a, b)

    def test_hour(self):
        a = moment('20201228').add(5, 'w')
        b = moment('20201228') + timedelta(weeks=5)
        self.assertEqual(a, b)

    def test_not_implement(self):
        with self.assertRaises(TypeError):
            a = moment('2021-4-2 04:02:09.957031 +0800')
            b = a + 2


if __name__ == '__main__':
    unittest.main()
