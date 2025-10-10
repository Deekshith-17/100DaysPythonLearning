import pprint
class player:
   def __init__(self, name, formats=[], runs=[]):
      self.name=name
      self.formats=formats
      self.runs=runs
   def __repr__(self):
      dct={}
      dct[self.name]=dict(zip(self.formats,self.runs))
      return (repr(dct))

l1=['Tests','ODI','T20']
l2=[[140, 45, 39],[15,122,36,67, 100, 49],[78,44, 12, 0, 23, 75]]
p1=player("virat",l1,l2)
pp=pprint.PrettyPrinter()
pp.pprint(p1)