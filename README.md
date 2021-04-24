# pymoment

The python version of "moment" which is made with reference to "moment.js"

To install pymoment, please download the whl file, then install with the *pip* command:

> pip install pymoment-*.whl

Then import the package for your code:

> from moment import moment

|Parameter for Constructor|Code|Notes|
|---|---|---|
|None|moment()|Get the current date and time|
|moment|moment(m)|Create a new moment object with the moment object "m"|
|datetime.datetime|moment(datetime.datetime.now())|Create a moment object with the datetime object "d"|
|str|moment('2021-04-12')|Parsing the string to a moment object|

## Parse

### Now

> now = moment()
> 
> now = moment(datetime.datetime.now())

### String

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

## Display

Once parsing and manipulation are done, you need some way to display the moment.

### Format

This is the most robust display option. It takes a string of tokens and replaces them with their corresponding values.

> moment().format();
> 
> moment().format(String);

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

