from datetime import datetime, date, time, timezone

# Using datetime.combine()
d = date(2022, 4, 20)
t = time(12, 30)
datetime.combine(d, t)

# Using datetime.now()
d = datetime.now()
print (d)

# Using datetime.strptime()
dt = datetime.strptime("23/04/20 16:30", "%d/%m/%y %H:%M")

# Using datetime.timetuple() to get tuple of all attributes
tt = dt.timetuple()
for it in tt:
   print(it)

# Date in ISO format
ic = dt.isocalendar()
for it in ic:
   print(it)