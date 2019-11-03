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

