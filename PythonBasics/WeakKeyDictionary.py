import weakref

class Person:
   def __init__(self, person_id, name, age):
      self.emp_id = person_id
      self.name = name
      self.age = age

   def __repr__(self):
      return "{} : {} : {}".format(self.person_id, self.name, self.age)
Person1 = Person(101, "Jeevan", 30)
Person2 = Person(102, "Ramanna", 35)
Person3 = Person(103, "Simran", 28)
weak_dict = weakref.WeakKeyDictionary({Person1: Person1.name, Person2: Person2.name, Person3: Person3.name})
print("Weak Key Dictionary : {}\n".format(weak_dict.data))
print("Dictionary Keys : {}\n".format([key().name for key in weak_dict.keyrefs()]))
del Person1
print("Dictionary Keys : {}\n".format([key().name for key in weak_dict.keyrefs()]))
Person4 = Person(104, "Partho", 32)
weak_dict.update({Person4: Person4.name})

print("Dictionary Keys : {}\n".format([key().name for key in weak_dict.keyrefs()]))