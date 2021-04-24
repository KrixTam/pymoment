# coding: utf-8

from datetime import datetime, timedelta
import calendar
from time import gmtime, strftime
import re
from dateutil.parser import parse
import math


def generateOrdinal(num):
    ordinal = []
    for n in range(1, num + 1):
        ordinal.append("%d%s" % (n, "tsnrhtdd"[(n // 10 % 10 != 1) * (n % 10 < 4) * n % 10::4]))
    ordinal.insert(0, '0th')
    return ordinal


ORDINAL = generateOrdinal(366)

WEEKDAY_S = 'Su Mo Tu We Th Fr Sa'.split(' ')
WEEKDAY = 'Sun Mon Tue Wed Thu Fri Sat'.split(' ')
WEEKDAY_L = 'Sunday Monday Tuesday Wednesday Thursday Friday Saturday'.split(' ')


class moment(object):
    format_regex = r'(\[[^\[]*\])|(\\)?([Hh]mm(ss)?|Mo|MM?M?M?|Do|DDDo|DD?D?D?|ddd?d?|do?|w[o|w]?|W[o|W]?|Qo?|N{1,5}|YYYYYY|YYYYY|YYYY|YY|y{2,4}|yo?|gg(ggg?)?|GG(GGG?)?|e|E|a|A|hh?|HH?|kk?|mm?|ss?|S{1,6}|x|X|zz?|ZZ?|LTS|LT|LL?L?L?|l{1,4}.)'

    def __init__(self, m=None):
        super().__init__()
        self._d = None
        self._s = {}
        self._week = {
            'dow': 0,  # Sunday is the first day of the week.
            'doy': 6  # The week that contains Jan 6th is the first week of the year.
        }
        if m is None:
            self._d = datetime.now()
        else:
            if isinstance(m, datetime):
                self._d = datetime(m.year, m.month, m.day, m.hour, m.minute, m.second, m.microsecond, m.tzinfo)
            else:
                if isinstance(m, str):
                    self._d = parse(m)
                else:
                    if isinstance(m, moment):
                        self._d = m.toDatetime()
                    else:
                        raise TypeError('Unknown type of object for generate the moment object.')
        self._generateDict()

    def toDatetime(self):
        return datetime(self._d.year, self._d.month, self._d.day, self._d.hour, self._d.minute, self._d.second,
                        self._d.microsecond, self._d.tzinfo)

    def add(self, *args):
        tmp = len(args)
        if 1 == tmp:
            #
            raise TypeError('function missing required arguments')
        else:
            if 2 == tmp:
                num = args[0]
                metric = args[1]
                if ('days' == metric) or ('d' == metric):
                    days_num = num
                    if isinstance(days_num, float):
                        days_num = round(days_num)
                    if isinstance(days_num, int):
                        return moment(self._d + timedelta(days=days_num))
                    else:
                        raise ValueError('number should be integer or float.')
                else:
                    if ('hours' == metric) or ('h' == metric):
                        if isinstance(num, int):
                            return moment(self._d + timedelta(hours=num))
                        else:
                            raise ValueError('number should be integer.')
                    else:
                        if ('minutes' == metric) or ('m' == metric):
                            if isinstance(num, int):
                                return moment(self._d + timedelta(minutes=num))
                            else:
                                raise ValueError('number should be integer.')
                        else:
                            if ('seconds' == metric) or ('s' == metric):
                                if isinstance(num, int):
                                    return moment(self._d + timedelta(seconds=num))
                                else:
                                    raise ValueError('number should be integer.')
                            else:
                                if ('milliseconds' == metric) or ('ms' == metric):
                                    if isinstance(num, int):
                                        return moment(self._d + timedelta(milliseconds=num))
                                    else:
                                        raise ValueError('number should be integer.')
                                else:
                                    if ('years' == metric) or ('y' == metric):
                                        # d = self._d.date()
                                        # new_d = None
                                        # try:
                                        #     new_d = d.replace(year=d.year + num)
                                        # except ValueError:
                                        #     new_d = d + (date(d.year + num, 3, 1) - date(d.year, 3, 1))
                                        # new_dt = datetime(new_d.year, new_d.month, new_d.day, self._d.hour,
                                        #                   self._d.minute, self._d.second, self._d.microsecond,
                                        #                   self._d.tzinfo)
                                        # return moment(new_dt)
                                        months = num * 12
                                        if isinstance(months, float):
                                            months = round(months)
                                        if isinstance(months, int):
                                            return self.add(months, 'M')
                                        else:
                                            raise ValueError('number should be integer or float.')
                                    else:
                                        if ('quarters' == metric) or ('Q' == metric):
                                            months = num * 3
                                            if isinstance(months, float):
                                                months = round(months)
                                            if isinstance(months, int):
                                                return self.add(months, 'M')
                                            else:
                                                raise ValueError('number should be integer or float.')
                                        else:
                                            if ('months' == metric) or ('M' == metric):
                                                months_num = num
                                                if isinstance(months_num, float):
                                                    months_num = round(months_num)
                                                if isinstance(months_num, int):
                                                    month = self._d.month - 1 + months_num
                                                    year = self._d.year + month // 12
                                                    month = month % 12 + 1
                                                    day = min(self._d.day, calendar.monthrange(year, month)[1])
                                                    return moment(datetime(year, month, day, self._d.hour,
                                                                           self._d.minute, self._d.second,
                                                                           self._d.microsecond,
                                                                           self._d.tzinfo))
                                                else:
                                                    raise ValueError('number should be integer or float.')
                                            else:
                                                if ('weeks' == metric) or ('w' == metric):
                                                    days_num = num * 7
                                                    if isinstance(days_num, float):
                                                        days_num = round(days_num)
                                                    if isinstance(days_num, int):
                                                        return self.add(days_num, 'd')
                                                    else:
                                                        raise ValueError('number should be integer or float.')
                                                else:
                                                    raise ValueError('metric "' + metric + '" is not supported.')
            else:
                raise TypeError('function missing required arguments')

    def getLocaleFirstDayOfWeek(self):
        return self._week['dow']

    def getLocaleFirstDayOfYear(self):
        return self._week['doy']

    @staticmethod
    def getDaysInYear(year):
        return (datetime(year, 12, 31) - datetime(year, 1, 1)).days + 1

    def getWeekOfYear(self, dow, doy):
        result = {
            'week': -1,
            'year': -1
        }
        week_offset = moment.getFirstWeekOffset(self._d.year, dow, doy)
        day_of_year = int(self._d.strftime("%j"))
        week = math.floor((day_of_year - week_offset - 1) / 7) + 1
        if week < 1:
            result['year'] = self._d.year - 1
            result['week'] = week + moment.getWeeksInYear(result['year'], dow, doy)
        else:
            tmp_week = moment.getWeeksInYear(self._d.year, dow, doy)
            if week > tmp_week:
                result['year'] = self._d.year + 1
                result['week'] = week - tmp_week
            else:
                result['year'] = self._d.year
                result['week'] = week
        return result

    @staticmethod
    def getFirstWeekOffset(year, dow, doy):
        # fwd = 7 + self._week['dow'] - self._week['doy']
        # fwdlw = (7 + datetime(self._d.year, 1, 1).isoweekday() - self._week['dow']) % 7
        # week_offset = fwd - fwdlw - 1
        fwd = 7 + dow - doy
        fwdlw = (7 + datetime(year, 1, fwd).isoweekday() - dow) % 7
        week_offset = fwd - fwdlw - 1
        return week_offset

    @staticmethod
    def getWeeksInYear(year, dow, doy):
        week_offset = moment.getFirstWeekOffset(year, dow, doy)
        week_offset_next = moment.getFirstWeekOffset(year + 1, dow, doy)
        return (moment.getDaysInYear(year) - week_offset + week_offset_next) // 7

    @staticmethod
    def zeroFill(num, target_length=2, force_sign=False):
        abs_num = abs(num)
        sign_str = ''
        if num >= 0:
            if force_sign:
                sign_str = '+'
        else:
            sign_str = '-'
        t = '%0' + str(target_length) + 'd'
        # return "%02d" % (num,)
        num_str = t % (abs_num,)
        return sign_str + num_str

    def _generateDict(self):
        quarter = (self._d.month - 1) // 3 + 1
        day_of_year = int(self._d.strftime("%j"))
        weekday = int(self._d.strftime("%w"))
        week_number = self.getWeekOfYear(self._week['dow'], self._week['doy'])['week']
        iso_week_number = self.getWeekOfYear(1, 4)['week']
        hour = self._d.hour % 12
        if 0 == hour:
            hour = 12
        hour_k = self._d.hour
        if 0 == hour_k:
            hour_k = 24
        microsecond = self._d.strftime('%f')
        tz = self._d.strftime('%z')
        if 0 == len(tz):
            tz = strftime("%z", gmtime())
        tzz = tz
        tz = tz[:3] + ':' + tz[3:]
        unix_timestamp = self._d.timestamp()
        d = {
            # Month
            'M': str(self._d.month),
            'Mo': ORDINAL[self._d.month],
            'MM': self._d.strftime("%m"),
            'MMM': self._d.strftime("%b"),
            'MMMM': self._d.strftime("%B"),
            # Quarter
            'Q': str(quarter),
            'Qo': ORDINAL[quarter],
            # Day of Month
            'D': str(self._d.day),
            'Do': ORDINAL[self._d.day],
            'DD': self._d.strftime("%d"),
            # Day of Year
            'DDD': str(day_of_year),
            'DDDo': ORDINAL[day_of_year],
            'DDDD': self._d.strftime("%j"),
            # Day of Week
            'd': str(weekday),
            'do': ORDINAL[weekday],
            'dd': WEEKDAY_S[weekday],
            'ddd': WEEKDAY[weekday],
            'dddd': WEEKDAY_L[weekday],
            # Day of Week (Locale) is not supported
            # Day of Week(ISO)
            'E': str(self._d.isoweekday()),
            # Week of Year
            'w': str(week_number),
            'wo': ORDINAL[week_number],
            'ww': moment.zeroFill(week_number),
            # Week of Year(ISO)
            'W': str(iso_week_number),
            'Wo': ORDINAL[iso_week_number],
            'WW': moment.zeroFill(iso_week_number),
            # Year
            'YY': str(self._d.year)[2:],
            'YYYY': str(self._d.year),
            # YYYYYY Expanded Years is not supported
            # Y is not supported
            # Era Year is not supported
            # Era is not supported
            # Week Year is not supported
            # Week Year(ISO) is not supported
            # AM / PM
            'A': self._d.strftime("%p").upper(),
            'a': self._d.strftime("%p").lower(),
            # Hour
            'H': str(self._d.hour),
            'HH': moment.zeroFill(self._d.hour),
            'h': str(hour),
            'hh': moment.zeroFill(hour),
            'k': str(hour_k),
            'kk': moment.zeroFill(hour_k),
            # Minute
            'm': str(self._d.minute),
            'mm': moment.zeroFill(self._d.minute),
            # Second
            's': str(self._d.second),
            'ss': moment.zeroFill(self._d.second),
            # Fractional Second
            'S': microsecond[0],
            'SS': microsecond[:2],
            'SSS': microsecond[:3],
            'SSSS': microsecond[:4],
            'SSSSS': microsecond[:5],
            'SSSSSS': microsecond,
            # Time Zone
            # 'z' and 'zz' are not supported.
            'Z': tz,
            'ZZ': tzz,
            # Unix Timestamp
            'X': str(unix_timestamp).split('.')[0],
            # Unix Millisecond Timestamp
            'x': str(unix_timestamp * 1000).split('.')[0],
            # Localized formats
            # Time
            'LT': str(hour) + ':' + moment.zeroFill(self._d.minute) + ' ' + self._d.strftime("%p").upper(),
            # Time with seconds
            'LTS': str(hour) + ':' + moment.zeroFill(self._d.minute) + ':' + moment.zeroFill(
                self._d.second) + ' ' + self._d.strftime("%p").upper(),
            # Month numeral, day of month, year
            'L': moment.zeroFill(self._d.month) + '/' + moment.zeroFill(self._d.day) + '/' + str(self._d.year),
            'l': str(self._d.month) + '/' + str(self._d.day) + '/' + str(self._d.year)
        }
        # Month name, day of month, year
        d['LL'] = d['MMMM'] + ' ' + str(self._d.day) + ', ' + str(self._d.year)
        d['ll'] = d['MMM'] + ' ' + str(self._d.day) + ', ' + str(self._d.year)
        # Month name, day of month, year, time
        d['LLL'] = d['LL'] + ' ' + d['LT']
        d['lll'] = d['ll'] + ' ' + d['LT']
        # Month name, day of month, day of week, year, time
        d['LLLL'] = d['dddd'] + ', ' + d['LLL']
        d['llll'] = d['ddd'] + ', ' + d['lll']
        self._s = d

    def format(self, input_string: str = None) -> str:
        if input_string is None:
            return self._d.isoformat().split('.')[0]
        else:
            matches = re.split(moment.format_regex, input_string)
            items = [y for y in [x for x in matches if x is not ''] if y is not None]
            results = []
            self._generateDict()
            for item in items:
                if item in self._s:
                    results.append(self._s[item])
                else:
                    if ('[' == item[0]) and (']' == item[-1]):
                        results.append(item[1:-1])
                    else:
                        results.append(item)
            return ''.join(results)
