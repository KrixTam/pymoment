import unittest
import datetime
from moment import moment
from moment.pymoment import EPOCH_MOMENT, EPOCH_DEFAULT


class TestUnix(unittest.TestCase):
    def test_class_unix(self):
        self.assertEqual(moment.unix(EPOCH_DEFAULT), EPOCH_MOMENT)

    def test_instance_unix_01(self):
        self.assertEqual(EPOCH_MOMENT.unix(), EPOCH_DEFAULT)

    def test_instance_unix_02(self):
        dt = datetime.datetime(1900, 1, 1, 19, 6, 28)
        a = moment(dt)
        self.assertEqual(a.unix(), -2208949155)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
