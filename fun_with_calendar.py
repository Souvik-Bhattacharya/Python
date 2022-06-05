# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 14:03:04 2022

@author: Souvik Bhattacharya
"""

import datetime
import pytz
import calendar

time_zone = pytz.timezone('HongKong')
print(datetime.datetime.now(time_zone))
time_zones = pytz.all_timezones
print(time_zones)

print(calendar.prcal(2022))
print(calendar.leapdays(1947, 2022))
print(calendar.isleap(2022))
print(calendar.weekday(2003,6,7))
print(calendar.weekday(2022,6,7))

dd = datetime.date(2022,4,23)
day_of_year = dd.timetuple().tm_yday
print(day_of_year)
print(datetime.date.today())
print(datetime.date.today().strftime("%Y"))
print(datetime.date.today().strftime("%B"))
print(datetime.date.today().strftime("%d"))
print(datetime.date.today().strftime("%j"))
print(datetime.date.today().strftime("%A"))
print(datetime.date.today().strftime("%W"))
print(datetime.date.today().strftime("%w"))
print(datetime.datetime.now())

for i in range(len(time_zones)):
    zone = time_zones[i]
    tz = pytz.timezone(zone)
    print('current time at zone',zone,'is',datetime.datetime.now(tz))