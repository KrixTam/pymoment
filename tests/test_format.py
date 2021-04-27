# coding: utf-8

import unittest
from moment import moment


class TestFormat(unittest.TestCase):

    def test_month(self):
        a = moment('2021-01-12')
        b = moment('2020-12-31')
        self.assertEqual(a.format('M'), '1')
        self.assertEqual(b.format('M'), '12')
        self.assertEqual(a.format('Mo'), '1st')
        self.assertEqual(b.format('Mo'), '12th')
        self.assertEqual(a.format('MM'), '01')
        self.assertEqual(b.format('MM'), '12')
        self.assertEqual(a.format('MMM'), 'Jan')
        self.assertEqual(b.format('MMM'), 'Dec')
        self.assertEqual(a.format('MMMM'), 'January')
        self.assertEqual(b.format('MMMM'), 'December')

    def test_Quarter(self):
        a = moment('2021-01-12')
        b = moment('2020-03-31')
        c = moment('2021-04-12')
        d = moment('2020-12-31')
        self.assertEqual(a.format('Q'), '1')
        self.assertEqual(b.format('Q'), '1')
        self.assertEqual(c.format('Q'), '2')
        self.assertEqual(d.format('Q'), '4')
        self.assertEqual(a.format('Qo'), '1st')
        self.assertEqual(b.format('Qo'), '1st')
        self.assertEqual(c.format('Qo'), '2nd')
        self.assertEqual(d.format('Qo'), '4th')

    def test_day_of_month(self):
        a = moment('2020-02-29')
        b = moment('2020-02-01')
        self.assertEqual(a.format('D'), '29')
        self.assertEqual(b.format('D'), '1')
        self.assertEqual(a.format('Do'), '29th')
        self.assertEqual(b.format('Do'), '1st')
        self.assertEqual(a.format('DD'), '29')
        self.assertEqual(b.format('DD'), '01')

    def test_day_of_year(self):
        a = moment('2021-01-02')
        b = moment('2020-03-31')
        self.assertEqual(a.format('DDD'), '2')
        self.assertEqual(b.format('DDD'), '91')
        self.assertEqual(a.format('DDDo'), '2nd')
        self.assertEqual(b.format('DDDo'), '91st')
        self.assertEqual(a.format('DDDD'), '002')
        self.assertEqual(b.format('DDDD'), '091')

    def test_day_of_week(self):
        a = moment('2021-01-02')
        b = moment('2020-03-31')
        self.assertEqual(a.format('d'), '6')
        self.assertEqual(b.format('d'), '2')
        self.assertEqual(a.format('do'), '6th')
        self.assertEqual(b.format('do'), '2nd')
        self.assertEqual(a.format('dd'), 'Sa')
        self.assertEqual(b.format('dd'), 'Tu')
        self.assertEqual(a.format('ddd'), 'Sat')
        self.assertEqual(b.format('ddd'), 'Tue')
        self.assertEqual(a.format('dddd'), 'Saturday')
        self.assertEqual(b.format('dddd'), 'Tuesday')

    def test_day_of_week_iso(self):
        a = moment('2021-01-02')
        b = moment('2020-03-31')
        self.assertEqual(a.format('E'), '6')
        self.assertEqual(b.format('E'), '2')

    def test_week_of_year(self):
        a = moment('2021-01-02')
        b = moment('2020-03-31')
        c = moment('2020-12-28')
        self.assertEqual(a.format('w'), '1')
        self.assertEqual(b.format('w'), '14')
        self.assertEqual(c.format('w'), '1')
        self.assertEqual(a.format('wo'), '1st')
        self.assertEqual(b.format('wo'), '14th')
        self.assertEqual(c.format('wo'), '1st')
        self.assertEqual(a.format('ww'), '01')
        self.assertEqual(b.format('ww'), '14')
        self.assertEqual(c.format('ww'), '01')

    def test_week_of_year_iso(self):
        a = moment('2021-01-02')
        b = moment('2020-03-31')
        c = moment('2020-12-28')
        d = moment('2021-01-08')
        self.assertEqual(a.format('W'), '53')
        self.assertEqual(b.format('W'), '14')
        self.assertEqual(c.format('W'), '53')
        self.assertEqual(d.format('W'), '1')
        self.assertEqual(a.format('Wo'), '53rd')
        self.assertEqual(b.format('Wo'), '14th')
        self.assertEqual(c.format('Wo'), '53rd')
        self.assertEqual(d.format('Wo'), '1st')
        self.assertEqual(a.format('WW'), '53')
        self.assertEqual(b.format('WW'), '14')
        self.assertEqual(c.format('WW'), '53')
        self.assertEqual(d.format('WW'), '01')

    def test_year(self):
        a = moment('2021-01-02')
        b = moment('2020-03-31')
        self.assertEqual(a.format('YY'), '21')
        self.assertEqual(b.format('YY'), '20')
        self.assertEqual(a.format('YYYY'), '2021')
        self.assertEqual(b.format('YYYY'), '2020')

    def test_am_pm(self):
        a = moment('2021-01-02 02:12:37')
        b = moment('2021-01-01 22:32:37')
        self.assertEqual(a.format('A'), 'AM')
        self.assertEqual(b.format('A'), 'PM')
        self.assertEqual(a.format('a'), 'am')
        self.assertEqual(b.format('a'), 'pm')

    def test_hour(self):
        a = moment('2021-01-02 02:12:37')
        b = moment('2021-01-01 22:32:37')
        c = moment('2021-11-21 00:32:37')
        self.assertEqual(a.format('H'), '2')
        self.assertEqual(b.format('H'), '22')
        self.assertEqual(c.format('H'), '0')
        self.assertEqual(a.format('HH'), '02')
        self.assertEqual(b.format('HH'), '22')
        self.assertEqual(c.format('HH'), '00')
        self.assertEqual(a.format('h'), '2')
        self.assertEqual(b.format('h'), '10')
        self.assertEqual(c.format('h'), '12')
        self.assertEqual(a.format('hh'), '02')
        self.assertEqual(b.format('hh'), '10')
        self.assertEqual(c.format('hh'), '12')
        self.assertEqual(a.format('k'), '2')
        self.assertEqual(b.format('k'), '22')
        self.assertEqual(c.format('k'), '24')
        self.assertEqual(a.format('kk'), '02')
        self.assertEqual(b.format('kk'), '22')
        self.assertEqual(c.format('kk'), '24')

    def test_minute(self):
        a = moment('2021-01-02 02:00:37')
        b = moment('2021-01-01 22:03:37')
        c = moment('2021-11-21 00:59:37')
        self.assertEqual(a.format('m'), '0')
        self.assertEqual(b.format('m'), '3')
        self.assertEqual(c.format('m'), '59')
        self.assertEqual(a.format('mm'), '00')
        self.assertEqual(b.format('mm'), '03')
        self.assertEqual(c.format('mm'), '59')

    def test_second(self):
        a = moment('2021-01-02 02:00:07')
        b = moment('2021-01-01 22:03:00')
        c = moment('2021-11-21 00:59:33')
        self.assertEqual(a.format('s'), '7')
        self.assertEqual(b.format('s'), '0')
        self.assertEqual(c.format('s'), '33')
        self.assertEqual(a.format('ss'), '07')
        self.assertEqual(b.format('ss'), '00')
        self.assertEqual(c.format('ss'), '33')

    def test_fractional_second(self):
        a = moment('2021-01-02 02:00:07.123786')
        self.assertEqual(a.format('S'), '1')
        self.assertEqual(a.format('SS'), '12')
        self.assertEqual(a.format('SSS'), '123')
        self.assertEqual(a.format('SSSS'), '1237')
        self.assertEqual(a.format('SSSSS'), '12378')
        self.assertEqual(a.format('SSSSSS'), '123786')

    def test_timezone(self):
        a = moment('2021-01-02 02:00:07.123786+03:00')
        self.assertEqual(a.format('Z'), '+03:00')
        self.assertEqual(a.format('ZZ'), '+0300')
        b = moment('2020-03-31')
        self.assertEqual(b.format('Z'), '+08:00')
        self.assertEqual(b.format('ZZ'), '+0800')

    def test_unix_timestamp(self):
        a = moment('2021-04-22 03:19:07.433000 +0800')
        b = moment('2021-04-22 04:22:09.957000 +0800')
        self.assertEqual(a.format('X'), '1619032747')
        self.assertEqual(a.format('x'), '1619032747433')
        self.assertEqual(b.format('X'), '1619036529')
        self.assertEqual(b.format('x'), '1619036529957')

    def test_localized_format(self):
        a = moment('2021-04-22 03:19:07.433000 +0800')
        b = moment('2021-10-02 14:22:09.957000 +0800')
        self.assertEqual(a.format('LT'), '3:19 AM')
        self.assertEqual(b.format('LT'), '2:22 PM')
        self.assertEqual(a.format('LTS'), '3:19:07 AM')
        self.assertEqual(b.format('LTS'), '2:22:09 PM')
        # print(a.format('L LTS'))
        self.assertEqual(a.format('L'), '04/22/2021')
        self.assertEqual(b.format('L'), '10/02/2021')
        self.assertEqual(a.format('l'), '4/22/2021')
        self.assertEqual(b.format('l'), '10/2/2021')
        self.assertEqual(a.format('LL'), 'April 22, 2021')
        self.assertEqual(b.format('LL'), 'October 2, 2021')
        self.assertEqual(a.format('ll'), 'Apr 22, 2021')
        self.assertEqual(b.format('ll'), 'Oct 2, 2021')
        self.assertEqual(a.format('LLL'), 'April 22, 2021 3:19 AM')
        self.assertEqual(b.format('LLL'), 'October 2, 2021 2:22 PM')
        self.assertEqual(a.format('lll'), 'Apr 22, 2021 3:19 AM')
        self.assertEqual(b.format('lll'), 'Oct 2, 2021 2:22 PM')
        self.assertEqual(a.format('LLLL'), 'Thursday, April 22, 2021 3:19 AM')
        self.assertEqual(b.format('LLLL'), 'Saturday, October 2, 2021 2:22 PM')
        self.assertEqual(a.format('llll'), 'Thu, Apr 22, 2021 3:19 AM')
        self.assertEqual(b.format('llll'), 'Sat, Oct 2, 2021 2:22 PM')

    def test_escape(self):
        a = moment('2021-04-22 04:02:09.957000 +0800')
        self.assertEqual(a.format('[Today is] dddd.'), 'Today is Thursday.')


if __name__ == '__main__':
    unittest.main()
