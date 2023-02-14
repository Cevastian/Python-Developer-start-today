"""
datetime module exercise

import datetime
import time

current_date_time = datetime.datetime.now()
print(current_date_time)

time.sleep(5)

print(current_date_time)

current_date_time = datetime.datetime.now()

print(current_date_time)

"""

import datetime

current_date_time = datetime.datetime.now( )

print( current_date_time + datetime.timedelta(seconds = 75))
print( current_date_time - datetime.timedelta(minutes = 25))
print( current_date_time + datetime.timedelta(hours =7))
print( current_date_time - datetime.timedelta(days=100))
print( current_date_time + datetime.timedelta(weeks = 8))