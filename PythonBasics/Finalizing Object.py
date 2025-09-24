import weakref
class Myclass:
   def __del__(self):
      print('(Deleting {})'.format(self))

def finalizer(*args):
   print('Finalizer{!r})'.format(args))

obj = Myclass()
r = weakref.finalize(obj, finalizer, "Call to finalizer")

print('object:', obj)
print('reference:', r)
print('call r():', r())

print('deleting obj')
del obj
print('r():', r())