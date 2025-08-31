from datetime import timedelta
delta = timedelta(
   days=100,
   seconds=27,
   microseconds=10,
   milliseconds=29000,
   minutes=5,
   hours=12,
   weeks=2
)
# Only days, seconds, and microseconds remain
print (delta)