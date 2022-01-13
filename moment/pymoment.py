from datetime import datetime, timedelta
import calendar
from time import gmtime, strftime
import re
from dateutil.parser import parse
import math
import time

EPOCH_DATETIME = datetime(1970, 1, 1)


def generateOrdinal(num):
    ordinal = []
    for n in range(1, num + 1):
        ordinal.append("%d%s" % (n, "tsnrhtdd"[(n // 10 % 10 != 1) * (n % 10 < 4) * n % 10::4]))
    ordinal.insert(0, '0th')
    return ordinal


def get_local_tz():
    tz = strftime("%z", gmtime())
    tz = tz[:3] + ':' + tz[3:]
    return tz


def zeroFill(num, target_length=2):
    abs_num = abs(num)
    t = '%0' + str(target_length) + 'd'
    num_str = t % (abs_num,)
    return num_str


ORDINAL = generateOrdinal(366)

WEEKDAY_S = 'Su Mo Tu We Th Fr Sa'.split(' ')
WEEKDAY = 'Sun Mon Tue Wed Thu Fri Sat'.split(' ')
WEEKDAY_L = 'Sunday Monday Tuesday Wednesday Thursday Friday Saturday'.split(' ')
METRIC = ['days', 'd', 'hours', 'h', 'minutes', 'm', 'seconds', 's', 'milliseconds', 'ms', 'years', 'y', 'quarters', 'Q', 'months', 'M', 'weeks', 'w']


class moment(object):
    format_regex = r'(\[[^\[]*\])|(\\)?([Hh]mm(ss)?|Mo|MM?M?M?|Do|DDDo|DD?D?D?|ddd?d?|do?|w[o|w]?|W[o|W]?|Qo?|N{1,5}|YYYYYY|YYYYY|YYYY|YY|y{2,4}|yo?|gg(ggg?)?|GG(GGG?)?|e|E|a|A|hh?|HH?|kk?|mm?|ss?|S{1,6}|x|X|zz?|ZZ?|LTS|LT|LL?L?L?|l{1,4}.)'

    def __init__(self, m=None):
        super().__init__()
        self.unix = self._instance_unix
        self._d = None
        self._s = {}
        self._week = {
            'dow': 0,  # Sunday is the first day of the week.
            'doy': 6  # The week that contains Jan 6th is the first week of the year.
        }
        tz = get_local_tz()
        if m is None:
            self._parseDatetime(datetime.now(), tz)
        else:
            if isinstance(m, datetime):
                d = datetime(m.year, m.month, m.day, m.hour, m.minute, m.second, m.microsecond, m.tzinfo)
                self._parseDatetime(d, tz)
            else:
                if isinstance(m, str):
                    d = parse(m)
                    self._parseDatetime(d, tz)
                else:
                    if isinstance(m, moment):
                        d = m.toDatetime()
                        self._parseDatetime(d, tz)
                    else:
                        if isinstance(m, list):
                            dt_args = m.copy()
                            length = len(dt_args)
                            if (length > 0) and (length < 9):
                                if 1 == length:
                                    dt_args.append(1)
                                    dt_args.append(1)
                                else:
                                    if 2 == length:
                                        dt_args.append(1)
                                d = datetime(*dt_args)
                                self._parseDatetime(d, tz)
                            else:
                                if 0 == length:
                                    d = datetime.now()
                                    self._parseDatetime(d, tz)
                                else:
                                    raise ValueError('When the parameter of the construction function is a list, the number of parameters in the list is out of range(1, 8).')
                        else:
                            raise TypeError('Unknown type of object for generate the moment object.')
        self._generateDict()

    def __eq__(self, other):
        if isinstance(other, moment):
            return self._d == other._d
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, moment):
            return self._d < other._d
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, moment):
            return self._d > other._d
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, moment):
            return self._d <= other._d
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, moment):
            return self._d >= other._d
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, moment):
            return not (self.__eq__(other))
        else:
            return NotImplemented

    def __add__(self, other):
        if not isinstance(other, timedelta):
            return NotImplemented
        d = self._d + other
        return moment(d)

    def __sub__(self, other):
        if isinstance(other, moment):
            return self.unix_timestamp() * 1000 - other.unix_timestamp() * 1000
        else:
            if isinstance(other, datetime):
                return self.unix_timestamp() * 1000 - other.timestamp() * 1000
            else:
                return NotImplemented

    def __repr__(self):
        return self.format('[moment]("YYYY-MM-DD HH:mm:ss.SSSSSS Z")')

    def _parseDatetime(self, d, tz_info: str = None):
        tz = tz_info
        if tz is None:
            tz = get_local_tz()
        if 0 == len(d.strftime('%z')):
            self._d = parse(d.strftime('%Y-%m-%d %H:%M:%S.%f ') + tz)
        else:
            self._d = d

    def toDatetime(self):
        return datetime(self._d.year, self._d.month, self._d.day, self._d.hour, self._d.minute, self._d.second,
                        self._d.microsecond, self._d.tzinfo)

    def setDatetime(self, d):
        self._parseDatetime(d)
        self._generateDict()

    def add(self, *args, inplace=False):
        tmp = len(args)
        if 1 == tmp:
            settings = args[0]
            if isinstance(settings, dict):
                if len(settings) == 0:
                    raise ValueError('dictionary object should contain at least one item.')
                else:
                    metric, num = settings.popitem()
                    if len(settings) == 0:
                        if metric in METRIC:
                            return self.add(num, metric, inplace=inplace)
                        else:
                            raise ValueError('metric "' + metric + '" is not supported.')
                    else:
                        if metric in METRIC:
                            return self.add(num, metric, inplace=inplace).add(settings, inplace=inplace)
                        else:
                            raise ValueError('metric "' + metric + '" is not supported.')
            else:
                raise TypeError('object should be dictionary.')
        else:
            if 2 == tmp:
                num = args[0]
                metric = args[1]
                if ('days' == metric) or ('d' == metric):
                    days_num = num
                    if isinstance(days_num, float):
                        days_num = round(days_num)
                    if isinstance(days_num, int):
                        new_d = self._d + timedelta(days=days_num)
                        if inplace:
                            self.setDatetime(new_d)
                        return moment(new_d)
                    else:
                        raise ValueError('number should be integer or float.')
                else:
                    if ('hours' == metric) or ('h' == metric):
                        if isinstance(num, int):
                            new_d = self._d + timedelta(hours=num)
                            if inplace:
                                self.setDatetime(new_d)
                            return moment(new_d)
                        else:
                            raise ValueError('number should be integer.')
                    else:
                        if ('minutes' == metric) or ('m' == metric):
                            if isinstance(num, int):
                                new_d = self._d + timedelta(minutes=num)
                                if inplace:
                                    self.setDatetime(new_d)
                                return moment(new_d)
                            else:
                                raise ValueError('number should be integer.')
                        else:
                            if ('seconds' == metric) or ('s' == metric):
                                if isinstance(num, int):
                                    new_d = self._d + timedelta(seconds=num)
                                    if inplace:
                                        self.setDatetime(new_d)
                                    return moment(new_d)
                                else:
                                    raise ValueError('number should be integer.')
                            else:
                                if ('milliseconds' == metric) or ('ms' == metric):
                                    if isinstance(num, int):
                                        new_d = self._d + timedelta(milliseconds=num)
                                        if inplace:
                                            self.setDatetime(new_d)
                                        return moment(new_d)
                                    else:
                                        raise ValueError('number should be integer.')
                                else:
                                    if ('years' == metric) or ('y' == metric):
                                        months = num * 12
                                        if isinstance(months, float):
                                            months = round(months)
                                        if isinstance(months, int):
                                            new_args = [months, 'M']
                                            return self.add(*new_args, inplace=inplace)
                                        else:
                                            raise ValueError('number should be integer or float.')
                                    else:
                                        if ('quarters' == metric) or ('Q' == metric):
                                            months = num * 3
                                            if isinstance(months, float):
                                                months = round(months)
                                            if isinstance(months, int):
                                                new_args = [months, 'M']
                                                return self.add(*new_args, inplace=inplace)
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
                                                    new_d = datetime(year, month, day, self._d.hour, self._d.minute, self._d.second, self._d.microsecond, self._d.tzinfo)
                                                    if inplace:
                                                        self.setDatetime(new_d)
                                                    return moment(new_d)
                                                else:
                                                    raise ValueError('number should be integer or float.')
                                            else:
                                                if ('weeks' == metric) or ('w' == metric):
                                                    days_num = num * 7
                                                    if isinstance(days_num, float):
                                                        days_num = round(days_num)
                                                    if isinstance(days_num, int):
                                                        new_args = [days_num, 'd']
                                                        return self.add(*new_args, inplace=inplace)
                                                    else:
                                                        raise ValueError('number should be integer or float.')
                                                else:
                                                    raise ValueError('metric "' + metric + '" is not supported.')
            else:
                raise TypeError('too many arguments')

    def subtract(self, *args, inplace=False):
        tmp = len(args)
        if 1 == tmp:
            settings = args[0]
            if isinstance(settings, dict):
                if len(settings) == 0:
                    raise ValueError('dictionary object should contain at least one item.')
                else:
                    metric, num = settings.popitem()
                    if len(settings) == 0:
                        if metric in METRIC:
                            return self.subtract(num, metric, inplace=inplace)
                        else:
                            raise ValueError('metric "' + metric + '" is not supported.')
                    else:
                        if metric in METRIC:
                            return self.subtract(num, metric, inplace=inplace).subtract(settings, inplace=inplace)
                        else:
                            raise ValueError('metric "' + metric + '" is not supported.')
            else:
                raise TypeError('object should be dictionary.')
        else:
            if 2 == tmp:
                num = args[0]
                metric = args[1]
                if isinstance(num, float) or isinstance(num, int):
                    new_num = num * (-1)
                    new_args = [new_num, metric]
                    return self.add(*new_args, inplace=inplace)
                else:
                    raise ValueError('number should be integer or float.')
            else:
                raise TypeError('too many arguments')

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
        # first-week day -- which january is always in the first week (4 for iso, 1 for other)
        fwd = 7 + dow - doy
        # first-week day local weekday -- which local weekday is fwd
        fwdlw = (7 + datetime(year, 1, fwd).isoweekday() - dow) % 7
        week_offset = fwd - fwdlw - 1
        return week_offset

    @staticmethod
    def getWeeksInYear(year, dow, doy):
        week_offset = moment.getFirstWeekOffset(year, dow, doy)
        week_offset_next = moment.getFirstWeekOffset(year + 1, dow, doy)
        return (moment.getDaysInYear(year) - week_offset + week_offset_next) // 7

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
        tzz = self._d.strftime('%z')
        tz = tzz[:3] + ':' + tzz[3:]
        unix_timestamp = self.unix_timestamp()
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
            'ww': zeroFill(week_number),
            # Week of Year(ISO)
            'W': str(iso_week_number),
            'Wo': ORDINAL[iso_week_number],
            'WW': zeroFill(iso_week_number),
            # Year
            'YY': zeroFill(int(zeroFill(self._d.year, 4)[-2:])),
            'YYYY': zeroFill(self._d.year, 4),
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
            'HH': zeroFill(self._d.hour),
            'h': str(hour),
            'hh': zeroFill(hour),
            'k': str(hour_k),
            'kk': zeroFill(hour_k),
            # Minute
            'm': str(self._d.minute),
            'mm': zeroFill(self._d.minute),
            # Second
            's': str(self._d.second),
            'ss': zeroFill(self._d.second),
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
            'LT': str(hour) + ':' + zeroFill(self._d.minute) + ' ' + self._d.strftime("%p").upper(),
            # Time with seconds
            'LTS': str(hour) + ':' + zeroFill(self._d.minute) + ':' + zeroFill(
                self._d.second) + ' ' + self._d.strftime("%p").upper(),
            # Month numeral, day of month, year
            'L': zeroFill(self._d.month) + '/' + zeroFill(self._d.day) + '/' + str(self._d.year),
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

    @staticmethod
    def unix(unix_timestamp: int):
        return EPOCH_MOMENT.add(unix_timestamp - EPOCH_DEFAULT, 'ms')

    def _instance_unix(self):
        try:
            unix_timestamp = int(time.mktime(self._d.timetuple()))
        except OverflowError:
            diff = self._d.replace(tzinfo=None) - EPOCH_DATETIME
            unix_timestamp = diff.days * 24 * 3600 + diff.seconds
        return unix_timestamp

    def unix_timestamp(self):
        unix_timestamp = self._instance_unix() + self._d.microsecond / 1000000
        return unix_timestamp

    def daysInMonth(self):
        return calendar.monthrange(self._d.year, self._d.month)[1]

    def daysInYear(self):
        return moment.getDaysInYear(self._d.year)

    def format(self, input_string: str = None) -> str:
        if input_string is None:
            return self.format('YYYY-MM-DDTHH:mm:ssZ')
        else:
            matches = re.split(moment.format_regex, input_string)
            items = [y for y in [x for x in matches if x != ''] if y is not None]
            results = []
            # self._generateDict()
            for item in items:
                if item in self._s:
                    results.append(self._s[item])
                else:
                    if ('[' == item[0]) and (']' == item[-1]):
                        results.append(item[1:-1])
                    else:
                        results.append(item)
            return ''.join(results)

    def millisecond(self, num: int = None):
        if num is None:
            return int(self._s['SSS'])
        else:
            new_d = self._d.replace(microsecond=0) + timedelta(milliseconds=num)
            self.setDatetime(new_d)

    def milliseconds(self, num: int = None):
        return self.millisecond(num)

    def second(self, num: int = None):
        if num is None:
            return self._d.second
        else:
            new_d = self._d.replace(second=0) + timedelta(seconds=num)
            self.setDatetime(new_d)

    def seconds(self, num: int = None):
        return self.second(num)

    def minute(self, num: int = None):
        if num is None:
            return self._d.minute
        else:
            new_d = self._d.replace(minute=0) + timedelta(minutes=num)
            self.setDatetime(new_d)

    def minutes(self, num: int = None):
        return self.minute(num)

    def hour(self, num: int = None):
        if num is None:
            return self._d.hour
        else:
            new_d = self._d.replace(hour=0) + timedelta(hours=num)
            self.setDatetime(new_d)

    def hours(self, num: int = None):
        return self.hour(num)

    def date(self, num: int = None):
        if num is None:
            return self._d.day
        else:
            new_d = self._d.replace(day=1) + timedelta(days=num-1)
            self.setDatetime(new_d)

    def dates(self, num: int = None):
        return self.date(num)

    def day(self, num: int = None):
        weekday = self._d.isoweekday() % 7
        if num is None:
            return weekday
        else:
            day_num = num - weekday
            self.add(day_num, 'd', inplace=True)

    def days(self, num: int = None):
        return self.day(num)

    def weekday(self, num: int = None):
        weekday = (7 + self._d.isoweekday() - self._week['dow']) % 7
        if num is None:
            return weekday
        else:
            day_num = num - weekday
            self.add(day_num, 'd', inplace=True)

    def isoWeekday(self, num: int = None):
        weekday = self._d.isoweekday()
        if num is None:
            return weekday
        else:
            day_num = num - weekday
            self.add(day_num, 'd', inplace=True)

    def dayOfYear(self, num: int = None):
        if num is None:
            return int(self._s['DDD'])
        else:
            new_d = self._d.replace(month=1, day=1) + timedelta(days=num - 1)
            self.setDatetime(new_d)

    def week(self, num: int = None):
        week = int(self._s['w'])
        if num is None:
            return week
        else:
            day_num = (num - week) * 7
            self.add(day_num, 'd', inplace=True)

    def weeks(self, num: int = None):
        return self.week(num)

    def isoWeek(self, num: int = None):
        week = int(self._s['W'])
        if num is None:
            return week
        else:
            day_num = (num - week) * 7
            self.add(day_num, 'd', inplace=True)

    def isoWeeks(self, num: int = None):
        return self.isoWeek(num)

    def month(self, num: int = None):
        month = self._d.month - 1
        if num is None:
            return month
        else:
            month_num = num - month
            self.add(month_num, 'M', inplace=True)

    def months(self, num: int = None):
        return self.month(num)

    def quarter(self, num: int = None):
        quarter = int(self._s['Q'])
        if num is None:
            return quarter
        else:
            quarter_num = num - quarter
            self.add(quarter_num, 'Q', inplace=True)

    def quarters(self, num: int = None):
        return self.quarter(num)

    def year(self, num: int = None):
        if num is None:
            return self._d.year
        else:
            if num > 0:
                new_d = self._d.replace(year=num)
                self.setDatetime(new_d)
            else:
                raise ValueError('The smallest year number is 1')

    def years(self, num: int = None):
        return self.year(num)

    def weeksInYear(self):
        result = int(moment([self._d.year, 12, 31]).format('w'))
        if 1 == result:
            result = int(moment([self._d.year, 12, 31]).add(-7, 'd').format('w'))
        return result

    def isoWeeksInYear(self):
        result = int(moment([self._d.year, 12, 31]).format('W'))
        if 1 == result:
            result = int(moment([self._d.year, 12, 31]).add(-7, 'd').format('W'))
        return result

    def startOf(self, metric: str, inplace=False):
        if 'year' == metric:
            new_d = datetime(self._d.year, 1, 1)
            if inplace:
                self.setDatetime(new_d)
            return moment(new_d)
        else:
            if 'month' == metric:
                new_d = datetime(self._d.year, self._d.month, 1)
                if inplace:
                    self.setDatetime(new_d)
                return moment(new_d)
            else:
                if 'quarter' == metric:
                    month = (int(self._s['Q']) - 1) * 3 + 1
                    new_d = datetime(self._d.year, month, 1)
                    if inplace:
                        self.setDatetime(new_d)
                    return moment(new_d)
                else:
                    if 'week' == metric:
                        dow = self.getLocaleFirstDayOfWeek()
                        if 0 == dow:
                            dow = 7
                        weekday = self._d.isoweekday()
                        days_num = dow - weekday - 7
                        if weekday >= dow:
                            days_num = dow - weekday
                        new_d = self._d + timedelta(days=days_num)
                        new_d = datetime(new_d.year, new_d.month, new_d.day)
                        if inplace:
                            self.setDatetime(new_d)
                        return moment(new_d)
                    else:
                        if 'isoWeek' == metric:
                            if 1 == self._d.isoweekday():
                                new_d = datetime(self._d.year, self._d.month, self._d.day)
                                if inplace:
                                    self.setDatetime(new_d)
                                return moment(new_d)
                            else:
                                days_num = 1 - self._d.isoweekday()
                                new_d = self._d + timedelta(days=days_num)
                                new_d = datetime(new_d.year, new_d.month, new_d.day)
                                if inplace:
                                    self.setDatetime(new_d)
                                return moment(new_d)
                        else:
                            if 'day' == metric:
                                new_d = datetime(self._d.year, self._d.month, self._d.day)
                                if inplace:
                                    self.setDatetime(new_d)
                                return moment(new_d)
                            else:
                                if 'date' == metric:
                                    new_d = datetime(self._d.year, self._d.month, self._d.day)
                                    if inplace:
                                        self.setDatetime(new_d)
                                    return moment(new_d)
                                else:
                                    if 'hour' == metric:
                                        new_d = datetime(self._d.year, self._d.month, self._d.day, self._d.hour)
                                        if inplace:
                                            self.setDatetime(new_d)
                                        return moment(new_d)
                                    else:
                                        if 'minute' == metric:
                                            new_d = datetime(self._d.year, self._d.month, self._d.day, self._d.hour,
                                                             self._d.minute)
                                            if inplace:
                                                self.setDatetime(new_d)
                                            return moment(new_d)
                                        else:
                                            if 'second' == metric:
                                                new_d = datetime(self._d.year, self._d.month, self._d.day, self._d.hour,
                                                                 self._d.minute, self._d.second)
                                                if inplace:
                                                    self.setDatetime(new_d)
                                                return moment(new_d)
                                            else:
                                                raise ValueError('Unknown metric for getting the star unit of the moment object')

    def endOf(self, metric: str, inplace=False):
        if 'year' == metric:
            new_d = datetime(self._d.year, 12, 31, 23, 59, 59, 999999)
            if inplace:
                self.setDatetime(new_d)
            return moment(new_d)
        else:
            if 'month' == metric:
                day = calendar.monthrange(self._d.year, self._d.month)[1]
                new_d = datetime(self._d.year, self._d.month, day, 23, 59, 59, 999999)
                if inplace:
                    self.setDatetime(new_d)
                return moment(new_d)
            else:
                if 'quarter' == metric:
                    month = int(self._s['Q']) * 3
                    day = calendar.monthrange(self._d.year, month)[1]
                    new_d = datetime(self._d.year, month, day, 23, 59, 59, 999999)
                    if inplace:
                        self.setDatetime(new_d)
                    return moment(new_d)
                else:
                    if 'week' == metric:
                        dow = self.getLocaleFirstDayOfWeek()
                        if 0 == dow:
                            dow = 7
                        weekday = self._d.isoweekday()
                        days_num = dow - weekday - 7
                        if weekday >= dow:
                            days_num = dow - weekday
                        days_num = days_num + 6
                        new_d = self._d + timedelta(days=days_num)
                        new_d = datetime(new_d.year, new_d.month, new_d.day, 23, 59, 59, 999999)
                        if inplace:
                            self.setDatetime(new_d)
                        return moment(new_d)
                    else:
                        if 'isoWeek' == metric:
                            if 1 == self._d.isoweekday():
                                new_d = datetime(self._d.year, self._d.month, self._d.day, 23, 59, 59, 999999)\
                                        + timedelta(days=6)
                                if inplace:
                                    self.setDatetime(new_d)
                                return moment(new_d)
                            else:
                                days_num = 1 - self._d.isoweekday() + 6
                                new_d = self._d + timedelta(days=days_num)
                                new_d = datetime(new_d.year, new_d.month, new_d.day, 23, 59, 59, 999999)
                                if inplace:
                                    self.setDatetime(new_d)
                                return moment(new_d)
                        else:
                            if 'day' == metric:
                                new_d = datetime(self._d.year, self._d.month, self._d.day, 23, 59, 59, 999999)
                                if inplace:
                                    self.setDatetime(new_d)
                                return moment(new_d)
                            else:
                                if 'date' == metric:
                                    new_d = datetime(self._d.year, self._d.month, self._d.day, 23, 59, 59, 999999)
                                    if inplace:
                                        self.setDatetime(new_d)
                                    return moment(new_d)
                                else:
                                    if 'hour' == metric:
                                        new_d = datetime(self._d.year, self._d.month, self._d.day, self._d.hour,
                                                         59, 59, 999999)
                                        if inplace:
                                            self.setDatetime(new_d)
                                        return moment(new_d)
                                    else:
                                        if 'minute' == metric:
                                            new_d = datetime(self._d.year, self._d.month, self._d.day, self._d.hour,
                                                             self._d.minute, 59, 999999)
                                            if inplace:
                                                self.setDatetime(new_d)
                                            return moment(new_d)
                                        else:
                                            if 'second' == metric:
                                                new_d = datetime(self._d.year, self._d.month, self._d.day, self._d.hour,
                                                                 self._d.minute, self._d.second, 999999)
                                                if inplace:
                                                    self.setDatetime(new_d)
                                                return moment(new_d)
                                            else:
                                                raise ValueError('Unknown metric for getting the star unit of the moment object')

    def locale(self, week: dict):
        if 'dow' in week:
            self._week['dow'] = week['dow']
        if 'doy' in week:
            self._week['doy'] = week['doy']
        self._generateDict()

    def isBefore(self, m, metric: str = None, start_flag=False):
        m_object = moment(m)
        if metric is None:
            return self.__lt__(m_object)
        else:
            if start_flag:
                this_object = self.startOf(metric)
                return this_object < m_object
            else:
                this_object = self.endOf(metric)
                return this_object < m_object

    def isSame(self, m, metric: str = None, start_flag=False):
        m_object = moment(m)
        if metric is None:
            return self.__eq__(m_object)
        else:
            if start_flag:
                this_object = self.startOf(metric)
                return this_object == m_object
            else:
                this_object = self.endOf(metric)
                return this_object == m_object

    def isAfter(self, m, metric: str = None, start_flag=False):
        m_object = moment(m)
        if metric is None:
            return self.__gt__(m_object)
        else:
            if start_flag:
                this_object = self.startOf(metric)
                return this_object > m_object
            else:
                this_object = self.endOf(metric)
                return this_object > m_object

    def isSameOrBefore(self, m, metric: str = None, start_flag=False):
        m_object = moment(m)
        if metric is None:
            return self.__le__(m_object)
        else:
            if start_flag:
                this_object = self.startOf(metric)
                return this_object <= m_object
            else:
                this_object = self.endOf(metric)
                return this_object <= m_object

    def isSameOrAfter(self, m, metric: str = None, start_flag=False):
        m_object = moment(m)
        if metric is None:
            return self.__ge__(m_object)
        else:
            if start_flag:
                this_object = self.startOf(metric)
                return this_object >= m_object
            else:
                this_object = self.endOf(metric)
                return this_object >= m_object

    def isBetween(self, m_from, m_to, metric: str = None, start_flag=False):
        m_from_object = moment(m_from)
        m_to_object = moment(m_to)
        if m_from_object > m_to_object:
            m_tmp_object = m_from_object
            m_from_object = m_to_object
            m_to_object = m_tmp_object
        if metric is None:
            return self.__gt__(m_from_object) and self.__lt__(m_to_object)
        else:
            if start_flag:
                this_object = self.startOf(metric)
                return (this_object > m_from_object) and (this_object < m_to_object)
            else:
                this_object = self.endOf(metric)
                return (this_object > m_from_object) and (this_object < m_to_object)

    def isLeapYear(self):
        return calendar.isleap(self._d.year)

    def isLeap(self):
        return self.isLeapYear()


EPOCH_DEFAULT = 1608480000
EPOCH_MOMENT = moment('2020-12-21')
