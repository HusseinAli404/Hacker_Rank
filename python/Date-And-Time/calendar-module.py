# https://www.hackerrank.com
# https://github.com/hussein-ali-mc

import datetime

month, date, year = map(int, input().split())
date = datetime.datetime(year=year, month=month, day=date)
print(date.strftime('%A').upper())
