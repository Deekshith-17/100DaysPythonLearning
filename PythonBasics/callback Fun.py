import weakref
class Myclass:
   def __del__(self):
      print('(Deleting {})'.format(self))
def mycallback(rfr):
   """called when referenced object is deleted"""
   print('calling ({})'.format(rfr))
obj = Myclass()
r = weakref.ref(obj, mycallback)

print('object:', obj)
print('reference:', r)
print('call r():', r())

print('deleting obj')
del obj
print('r():', r())