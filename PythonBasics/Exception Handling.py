def generator(num):
   for x in range(1, num+1):
      yield x
   return
   
it = generator(5)
while True:
   try:
      print (next(it))
   except StopIteration:
      break