#241-250
import datetime

now = datetime.datetime.now();
print(now, type(now));

for day in range(7, 0, -1):
    prew = datetime.timedelta(days=day);
    week = now - prew;
    print(week);

#244 strftime
