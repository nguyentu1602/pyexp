import datetime as dt
import time as tm
import pytz as tz

# get current time - note that there is no timezone
now = dt.datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond, now.tzinfo)

# make new date objects and play date arithmetic with it
last    = dt.datetime(2020, 10, 31, 4, 20, 10)  # if we don't give any hour etc default is midnight
first   = dt.datetime(2019, 1, 1)
diff    = last - first
[i for i in dir(diff) if '__' not in i]   # what does this object has?
print("days and seconds are main units of the timedelta object: ", diff.days, diff.seconds)

diff.total_seconds()  # convert all days to seconds

delta = dt.timedelta(days=10, hours=20, minutes=35, seconds=10)  # timedelta object
future_date = last + delta; print( future_date )    # timedelta object could be added to dt object easily

# print in nice format (the f stands for format)
time_string = dt.datetime.strftime(future_date, '%Y-%m-%d %H:%M:%S') # be careful between month and minute

# convert back from string to datetime obj
date_obj = dt.datetime.strptime('2019-16-02', '%Y-%d-%m')   # p is for parse
print(date_obj)

# use the time module for unix time operation - e.g. return unix epoch and sleep. This is pretty much all it's good for
tm.time()  # seconds since beginning of time - useful when calculating how much time a function takes

# test features of the pytz package
utc = tz.utc
dir(utc)
utc.dst(dt.datetime.now())  # should be zero for me since im in LDN
now_with_tz = utc.localize(dt.datetime.now())
print(now_with_tz)

# print all timezones and get a few of them out:
for tzz in tz.all_timezones:
    print(tzz)
eastern  = tz.timezone('US/Eastern')
deutsche = tz.timezone('Europe/Berlin')
ams      = tz.timezone('Europe/Amsterdam')
chicago  = tz.timezone('US/Central')
cet  = tz.timezone('CET')

ldn      = tz.timezone('Europe/London')
hkg      = tz.timezone('Asia/Hong_Kong')

# midnight at ldn is AFTER midnight at hkg by x hours
hkg_ldn_diff = dt.datetime(2019, 11, 11, tzinfo=ldn) - dt.datetime(2019, 11, 11, tzinfo=hkg)
hkg_ldn_diff.total_seconds() / 60 / 60  # interesting that it returns 7.63 not 8!!!

fmt = '%Y-%m-%d %H:%M:%S %Z%z'
# localized times - 1st way: build from strings:
loc_dt = cet.localize(dt.datetime(2019, 11, 11, 6, 0, 0))

# tzinfo doesn't work for many timezones:
date_obj_ldn = dt.datetime(2019, 11, 11, 0, 0, 0, tzinfo=ldn)
date_obj_ldn.astimezone(hkg)

# The preferred way of dealing with times is to always work in UTC
# converting to localtime only when generating output to be read by humans.
utc_dt = dt.datetime(2002, 10, 27, 6, 0, 0, tzinfo=utc)
loc_dt_to_print = utc_dt.astimezone(eastern)  # DO NOT DO ANY ARITHMETIC with this obj

# read more here - it's a mess really - but no other way of dealing with it
# http://pytz.sourceforge.net/
