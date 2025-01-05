# pymoment

The python version of "moment" which is made with reference to "moment.js"

To install pymoment, please download the whl file, then install with the *pip* command:

> pip install pymoment-*.whl

or just install:

> pip install pymoment

Then import the package for your code:

> from moment import moment

|Parameter for Constructor|Code|Notes|
|---|---|---|
|None|moment()|Get the current date and time|
|moment|moment(m)|Create a new moment object with the moment object "m"|
|datetime.datetime|moment(d)|Create a moment object with the datetime object "d"|
|str|moment('2021-04-12')|Parsing the string to a moment object|
|list|moment([2021, 4, 12])|Parsing the list to a moment object|


## Parse

### Now

> now = moment()
> 
> now = moment([])
>  
> now = moment(datetime.datetime.now())

### String

> moment(String)

You can create a moment from a string. The following are examples of strings in supported formats.

> 2013-02-08               # Date only
> 
> 2013-02-08T09            # An hour time part separated by a T
> 
> 2013-02-08 09            # An hour time part separated by a space
> 
> 2013-02-08 09:30         # An hour and minute time part
> 
> 2013-02-08 09:30:26      # An hour, minute, and second time part
> 
> 2013-02-08 09:30:26.123  # An hour, minute, second, and millisecond time part
> 
> 20130208T080910,123      # Short date and time up to ms, separated by comma
> 
> 20130208T080910.123      # Short date and time up to ms
> 
> 20130208T080910          # Short date and time up to seconds
> 
> 20130208T0809            # Short date and time up to minutes
> 
> 20130208T08              # Short date and time, hours only
> 
> 20130208                 # Short date only

With time zone:

> 2021-04-22 04:02:09.957000 +0800
> 
> 2021-04-22 04:02:09 +0800
> 
> 2021-04-22 04:02 +0800
> 
> 2021-04-22 04 +0800
> 
> 20210422 04:02:09 +0800

### List

> moment([2021, 4, 12])

You can create a moment with a list of numbers that mirror the parameters passed to datetime.

> [ year, month=1, day=1, hour=0, minute=0, second=0, microsecond=0 ]

Any parameter except "year" will default to the lowest possible number.

> moment([2010])        # January 1st
> 
> moment([2010, 6])     # July 1st
> 
> moment([2010, 6, 10]) # July 10th

If an empty list is passed, you could get the current date time.

> moment([])


## Display

Once parsing and manipulation are done, you need some way to display the moment.

### Format

This is the most robust display option. It takes a string of tokens and replaces them with their corresponding values.

> moment().format()
> 
> moment().format(String)

| |Token|Output|
|---|---|---|
|**Month**|M|1 2 ... 11 12|
| |Mo|1st 2nd ... 11th 12th|
| |MM|01 02 ... 11 12|
| |MMM|Jan Feb ... Nov Dec|
| |MMMM|January February ... November December|
|Quarter|Q|1 2 3 4|
| |Qo|1st 2nd 3rd 4th|
|Day of Month|D|1 2 ... 30 31|
| |Do|1st 2nd ... 30th 31st|
| |DD|01 02 ... 30 31|
|Day of Year|DDD|1 2 ... 364 365|
| |DDDo|1st 2nd ... 364th 365th|
| |DDDD|001 002 ... 364 365|
|Day of Week|d|0 1 ... 5 6|
| |do|0th 1st ... 5th 6th|
| |dd|Su Mo ... Fr Sa|
| |ddd|Sun Mon ... Fri Sat|
| |dddd|Sunday Monday ... Friday Saturday|
|Day of Week (ISO)|E|1 2 ... 6 7|
|Week of Year|w|1 2 ... 52 53|
| |wo|1st 2nd ... 52nd 53rd|
| |ww|01 02 ... 52 53|
|Week of Year (ISO)|W|1 2 ... 52 53|
| |Wo|1st 2nd ... 52nd 53rd|
| |WW|01 02 ... 52 53|
|Year|YY|70 71 ... 29 30|
| |YYYY|1970 1971 ... 2029 2030|
|AM/PM|A|AM PM|
| |a|am pm|
|Hour|H|0 1 ... 22 23|
| |HH|00 01 ... 22 23|
| |h|1 2 ... 11 12|
| |hh|01 02 ... 11 12|
| |k|1 2 ... 23 24|
| |kk|01 02 ... 23 24|
|Minute|m|0 1 ... 58 59|
| |mm|00 01 ... 58 59|
|Second|s|0 1 ... 58 59|
| |ss|00 01 ... 58 59|
|Fractional Second|S|0 1 ... 8 9|
| |SS|00 01 ... 98 99|
| |SSS|000 001 ... 998 999|
| |SSSS|0000 0001 ... 9998 9999|
| |SSSSS|00000 00001 ... 99998 99999|
| |SSSSSS|000000 000001 ... 999998 999999|
|Time Zone|Z|-07:00 -06:00 ... +06:00 +07:00|
| |ZZ|-0700 -0600 ... +0600 +0700|
|Unix Timestamp|X|1360013296|
|Unix Millisecond Timestamp|x|1360013296123|
|Time|LT|8:30 PM|
|Time with seconds|LTS|8:30:25 PM|
|Month numeral, day of month, year|L|09/04/1986|
| |l|9/4/1986|
|Month name, day of month, year|LL|September 4, 1986|
| |ll|Sep 4, 1986|
|Month name, day of month, year, time|LLL|September 4, 1986 8:30 PM|
| |lll|Sep 4, 1986 8:30 PM|
|Month name, day of month, day of week, year, time|LLLL|Thursday, September 4, 1986 8:30 PM|
| |llll|Thu, Sep 4, 1986 8:30 PM|

#### Escaping characters

To escape characters in format strings, you can wrap the characters in square brackets.

> moment('2021-04-22 04:02:09.957000 +0800').format('[Today is] dddd.')
> 
> 'Today is Thursday.'


## Get + Set

Calling all methods without parameters acts as a getter, and calling them with a parameter acts as a setter.

### Millisecond

> moment().millisecond(Number)
> 
> moment().millisecond()  # Number
> 
> moment().milliseconds(Number)
> 
> moment().milliseconds()  # Number

Gets or sets the milliseconds.

Accepts numbers from 0 to 999. If the range is exceeded, it will bubble up to the seconds.

### Second

> moment().second(Number)
> 
> moment().second()  # Number
> 
> moment().seconds(Number)
> 
> moment().seconds()  # Number

Gets or sets the seconds.

Accepts numbers from 0 to 59. If the range is exceeded, it will bubble up to the minutes.

### Minutes

> moment().minute(Number)
> 
> moment().minute()  # Number
> 
> moment().minutes(Number)
> 
> moment().minutes()  # Number

Gets or sets the minutes.

Accepts numbers from 0 to 59. If the range is exceeded, it will bubble up to the hour.

### Hour

> moment().hour(Number)
> 
> moment().hour()  # Number
> 
> moment().hours(Number)
> 
> moment().hours()  # Number

Gets or sets the hour.

Accepts numbers from 0 to 23. If the range is exceeded, it will bubble up to the day.

### Date of Month

> moment().date(Number)
> 
> moment().date()  # Number
> 
> moment().dates(Number)
> 
> moment().dates()  # Number

Gets or sets the day of the month.

Accepts numbers from 1 to 31. If the range is exceeded, it will bubble up to the months.

**Note**: *moment.date* is for the date of the month, and *moment.day* is for the day of the week.

### Day of Week

> moment().day(Number)
> 
> moment().day()  # Number
> 
> moment().days(Number)
> 
> moment().days()  # Number

Gets or sets the day of the week.

This method can be used to set the day of the week, with Sunday as 0 and Saturday as 6.

If the value given is from 0 to 6, the resulting date will be within the current (Sunday-to-Saturday) week.

If the range is exceeded, it will bubble up to other weeks.

**Note**: *moment.date* is for the date of the month, and *moment.day* is for the day of the week.

### Day of Week (Locale Aware)

> moment().weekday(Number)
> 
> moment().weekday()  # Number

> moment().weekday(Number)
> 
> moment().weekday() # Number

Gets or sets the day of the week according to the locale.

If the locale assigns Monday as the first day of the week, moment().weekday(0) will be Monday. If Sunday is the first day of the week, moment().weekday(0) will be Sunday.

### Day of Week (Locale Aware)

> moment().isoWeekday(Number)
> moment().isoWeekday()  # Number

Gets or sets the ISO day of the week with 1 being Monday and 7 being Sunday.

As with moment#day, if the range is exceeded, it will bubble up to other weeks.

### Day of Year

> moment().dayOfYear(Number)
> 
> moment().dayOfYear()  # Number

Gets or sets the day of the year.

Accepts numbers from 1 to 366. If the range is exceeded, it will bubble up to the years.

### Week of Year

> moment().week(Number)
> 
> moment().week()  # Number
> 
> moment().weeks(Number)
> 
> moment().weeks()  # Number

Gets or sets the week of the year.

Because different locales define week of year numbering differently, use *moment.local* to set the localized week of the year.

The week of the year varies depending on which day is the first day of the week (Sunday, Monday, etc), and which week is the first week of the year.

For example, in the United States, Sunday is the first day of the week. The week with January 1st in it is the first week of the year.

In France, Monday is the first day of the week, and the week with January 4th is the first week of the year.

The output of *moment.week* will depend on the locale for that moment.

When setting the week of the year, the day of the week is retained.

### Week of Year (ISO)

> moment().isoWeek(Number)
> 
> moment().isoWeek()  # Number
> 
> moment().isoWeeks(Number)
> 
> moment().isoWeeks()  # Number

Gets or sets the [ISO week of the year](https://en.wikipedia.org/wiki/ISO_week_date).

When setting the week of the year, the day of the week is retained.

### Month

> moment().month(Number)
> 
> moment().month()  # Number
> 
> moment().months(Number)
> 
> moment().months()  # Number

Gets or sets the month.

Accepts numbers from 0 to 11. If the range is exceeded, it will bubble up to the year.

**Note**: Months are zero indexed, so January is month 0.

### Quarter

> moment().quarter()  # Number
> 
> moment().quarter(Number)
> 
> moment().quarters()  # Number
> 
> moment().quarters(Number)

Gets the quarter (1 to 4) and sets the quarter with parameter *Number*.

If the range is exceeded, it will bubble up to other quarters.

### Year

> moment().year(Number)
> 
> moment().year()  # Number
> 
> moment().years(Number)
> 
> moment().years()  # Number

Gets or sets the year. According to *datetime.MINYEAR*, parameter *Number* should larger than zero.

### Weeks In Year

> moment().weeksInYear()

Gets the number of weeks according to locale in the current moment's year.

### Weeks In Year (ISO)

> moment().isoWeeksInYear()

Gets the number of weeks in the current moment's year, according to [ISO weeks](https://en.wikipedia.org/wiki/ISO_week_date).

### Unix Timestamp

> moment().unix()

*moment.unix* outputs a Unix timestamp (the number of seconds since the Unix Epoch).

This value is floored to the nearest second, and does not include a milliseconds component.

### Days in Month

> moment().daysInMonth()

Get the number of days in the current month.

> moment('20200213').daysInMonth()  # 29
> 
> moment('20210813').daysInMonth()  # 31

### Days in Year

> moment().daysInYear()

Get the number of days in the current year.

> moment('20200213').daysInYear()  # 366
> 
> moment('20210413').daysInYear()  # 365

## Manipulate

### Add

> moment().add(Number, String, inplace=False)
> 
> moment().add(Dictionary)

Mutates the original moment by adding time and return a new moment instance as a result.

This is a pretty robust function for adding time to an existing moment. To add time, pass the key of what time you want to add, and the amount you want to add.

> moment().add(7, 'days')
> 
> moment().add({'days': 7})

There are some shorthand keys as well if you're into that whole brevity thing.

> moment().add(7, 'd')
> 
> moment().add({'d': 7})

If *inplace* is *True*, the original moment instance should be updated by the adding operation.

|Key|Shorthand|
|---|---|
|years|y|
|quarters|Q|
|months|M|
|weeks|w|
|days|d|
|hours|h|
|minutes|m|
|seconds|s|
|milliseconds|ms|

If the day of the month on the original date is greater than the number of days in the final month, the day of the month will change to the last day in the final month.

> moment('2010-01-31').add(1, 'months') # 2010-02-28

When decimal values are passed for days and months, they are rounded to the nearest integer. Weeks, quarters, and years are converted to days or months, and then rounded to the nearest integer.

> moment('2010-01-31').add(1.5, 'months') == moment('2010-01-31').add(2, 'months')
> 
> moment('2010-01-31').add(.7, 'years') == moment('2010-01-31').add(8, 'months') # .7*12 = 8.4, rounded to 8

### Subtract

> moment().subtract(Number, String, inplace=False)
> 
> moment().subtract(Dictionary)

Mutates the original moment by subtracting time and return a new moment instance as a result.

This is exactly the same as *moment().add*, only instead of adding time, it subtracts time.

> moment().subtract(7, 'days')
> 
> moment().subtract({'days': 7})

If *inplace* is *True*, the original moment instance should be updated by the subtracting operation.

### Start of Time

> moment().startOf(String, inplace=False)

Mutates the original moment by setting it to the start of a unit of time.

If *inplace* is *True*, the original moment instance should be updated to the start of a unit of time.

> moment().startOf('year')     # set to January 1st, 12:00 am this year
> 
> moment().startOf('month')    # set to the first of this month, 12:00 am
> 
> moment().startOf('quarter')  # set to the beginning of the current quarter, 1st day of months, 12:00 am
> 
> moment().startOf('week')     # set to the first day of this week, 12:00 am
> 
> moment().startOf('isoWeek')  # set to the first day of this week according to ISO 8601, 12:00 am
> 
> moment().startOf('day')      # set to 12:00 am today
> 
> moment().startOf('date')     # set to 12:00 am today
> 
> moment().startOf('hour')     # set to now, but with 0 mins, 0 secs, and 0 ms
> 
> moment().startOf('minute')   # set to now, but with 0 seconds and 0 milliseconds
> 
> moment().startOf('second')   # same as moment().milliseconds(0)

### End of Time

> moment().endOf(String, inplace=False)

Mutates the original moment by setting it to the end of a unit of time.

This is the same as *moment.startOf*, only instead of setting to the start of a unit of time, it sets to the end of a unit of time.


### Operator

"+" and "-" are supported.

While doing "-" operation, *timedelta* is the result of the operation.

> (moment('20201228') - moment('20201225')) == timedelta(days=3)

While doing "+" operation, *timedelta* is added to the moment instance and returning a new moment instance.

The followings should get the same result.

> moment('20201228') + timedelta(days=3)
> 
> moment('20201228').add(3, 'd')

## Query

### Is Before

> moment().isBefore(moment|str|datetime|list)
> 
> moment().isBefore(moment|str|datetime|list, str)

Check if a moment is before another moment. The first argument will be parsed as a moment, if not already so.

> moment('2010-10-20').isBefore('2010-10-21')  # True

If you want to limit the granularity to a unit other than milliseconds, pass the units as the second parameter.

As the second parameter determines the precision, and not just a single value to check, using day will check for year, month and day.

> moment('2010-10-20').isBefore('2010-12-31', 'year')  # False
> 
> moment('2010-10-20').isBefore('2011-01-01', 'year')  # True

Like *moment.isAfter* and *moment.isSame*, any of the units of time that are supported for *moment.startOf* are supported for *moment.isBefore*.

> year month week isoWeek day hour minute second

If nothing is passed to moment#isBefore, it will default to the current time.

### Is Same

> moment().isSame(moment|str|datetime|list)
> 
> moment().isSame(moment|str|datetime|list, str)

Check if a moment is the same as another moment. The first argument will be parsed as a moment, if not already so.

> moment('2010-10-20').isSame('2010-10-20')  # True

If you want to limit the granularity to a unit other than milliseconds, pass it as the second parameter.

> moment('2010-10-20').isSame('2009-12-31', 'year')  # False
> 
> moment('2010-10-20').isSame('2010-01-01', 'year')  # True
> 
> moment('2010-10-20').isSame('2010-12-31', 'year')  # True
> 
> moment('2010-10-20').isSame('2011-01-01', 'year')  # False

When including a second parameter, it will match all units equal or larger. Passing in month will check month and year. Passing in day will check day, month, and year.

> moment('2010-01-01').isSame('2011-01-01', 'month')  # False, different year
> 
> moment('2010-01-01').isSame('2010-02-01', 'day')  # False, different month

Like *moment.isAfter* and *moment.isBefore*, any of the units of time that are supported for *moment.startOf* are supported for *moment.isSame*.

> year month week isoWeek day hour minute second

### Is After

> moment().isAfter(moment|str|datetime|list)
> 
> moment().isAfter(moment|str|datetime|list, str)

Check if a moment is after another moment. The first argument will be parsed as a moment, if not already so.

> moment('2010-10-20').isAfter('2010-10-19')  # True

If you want to limit the granularity to a unit other than milliseconds, pass the units as the second parameter.

As the second parameter determines the precision, and not just a single value to check, using day will check for year, month and day.

> moment('2010-10-20').isAfter('2010-01-01', 'year')  # False
> 
> moment('2010-10-20').isAfter('2009-12-31', 'year')  # True

Like *moment.isSame* and *moment.isBefore*, any of the units of time that are supported for *moment.startOf* are supported for *moment.isAfter*.

> year month week isoWeek day hour minute second

If nothing is passed to *moment.isAfter*, it will default to the current time.

> moment().isAfter()  # False

### Is Same or Before

> moment().isSameOrBefore(moment|str|datetime|list)
> 
> moment().isSameOrBefore(moment|str|datetime|list, str)

Check if a moment is before or the same as another moment. The first argument will be parsed as a moment, if not already so.

> moment('2010-10-20').isSameOrBefore('2010-10-21')  # True
> 
> moment('2010-10-20').isSameOrBefore('2010-10-20')  # True
> 
> moment('2010-10-20').isSameOrBefore('2010-10-19')  # False

If you want to limit the granularity to a unit other than milliseconds, pass the units as the second parameter.

As the second parameter determines the precision, and not just a single value to check, using day will check for year, month and day.

> moment('2010-10-20').isBefore('2010-12-31', 'year')  # False
> 
> moment('2010-10-20').isBefore('2011-01-01', 'year')  # True

Like *moment.isAfter* and *moment.isSame*, any of the units of time that are supported for *moment.startOf* are supported for *moment.isBefore*.

> year month week isoWeek day hour minute second

If nothing is passed to moment#isBefore, it will default to the current time.

### Is Same or After

> moment().isSameOrAfter(moment|str|datetime|list)
> 
> moment().isSameOrAfter(moment|str|datetime|list, str)

Check if a moment is after or the same as another moment. The first argument will be parsed as a moment, if not already so.

> moment('2010-10-20').isSameOrAfter('2010-10-19')  # True
> 
> moment('2010-10-20').isSameOrAfter('2010-10-20')  # True
> 
> moment('2010-10-20').isSameOrAfter('2010-10-21')  # False

If you want to limit the granularity to a unit other than milliseconds, pass the units as the second parameter.

As the second parameter determines the precision, and not just a single value to check, using day will check for year, month and day.

> moment('2010-10-20').isSameOrAfter('2011-12-31', 'year')  # False
> 
> moment('2010-10-20').isSameOrAfter('2010-01-01', 'year')  # True
> 
> moment('2010-10-20').isSameOrAfter('2009-12-31', 'year')  # True

Like moment#isSame and moment#isBefore, any of the units of time that are supported for moment#startOf are supported for moment#isSameOrAfter:

> year month week isoWeek day hour minute second

###Is Between

> moment().isBetween(moment|str|datetime|list, moment|str|datetime|list)
> 
> moment().isBetween(moment|str|datetime|list, moment|str|datetime|list, str)

Check if a moment is between two other moments, optionally looking at unit scale (minutes, hours, days, etc). The match is exclusive. The first two arguments will be parsed as moments, if not already so.

> moment('2010-10-20').isBetween('2010-10-19', '2010-10-25')  # True

Note that the order of the two arguments **do not** matter.

> moment('2010-10-20').isBetween('2010-10-19', '2010-10-25')  # True

> moment('2010-10-20').isBetween('2010-10-25', '2010-10-19')  # True

If you want to limit the granularity to a unit other than milliseconds, pass the units as the third parameter.

> moment('2010-10-20').isBetween('2010-01-01', '2012-01-01', 'year')  # False
> 
> moment('2010-10-20').isBetween('2009-12-31', '2012-01-01', 'year')  # True

Like *moment.isSame*, *moment.isBefore*, *moment.isAfter* any of the units of time that are supported for *moment.startOf* are supported for *moment.isBetween*.

> year month week isoWeek day hour minute second

### Is Leap Year

> moment().isLeapYear()
> 
> moment().isLeap()
 
*moment.isLeapYear* and *moment.isLeap* return true if that year is a leap year, and false if it is not.

> moment([2020]).isLeapYear()  # True
> 
> moment([2020]).isLeap()  # True
> 
> moment([2021]).isLeap()  # False


## Customize

### First Day of Week and First Week of Year

> week = { 'dow': int, 'doy': int }
> 
> moment().locale(week)

*week['dow']* should be an integer representing the first day of the week, 0 is Sunday, 1 is Monday, ..., 6 is Saturday. Default is 0.

*week['doy']* should be an integer. *doy* is used together with *dow* to determine the first week of the year. *doy* is calculated as *7 + dow - janX*, where *janX* is the first day of January that must belong to the first week of the year. Default is 6.
