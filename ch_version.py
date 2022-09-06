from datetime import datetime as dt
import pytz

now = dt.now(pytz.timezone('Europe/Kiev'))
nowTupple = now.timetuple()
now_year = str(nowTupple[0])
now_month = str(nowTupple[1])
now_day = str(nowTupple[2])
now_hour = str(nowTupple[3])
now_min = str(nowTupple[4])
if len(now_min) == 1:
	now_min = str(now_min) + '0'
new_version = now_year[3] + now_month + '.' + now_day + now_hour + now_min
new_version = '__version__ = ' + "'" + new_version + "'"
new_version = str(new_version)
f = open('version.py', 'w')
f.write(new_version)
f.close()




