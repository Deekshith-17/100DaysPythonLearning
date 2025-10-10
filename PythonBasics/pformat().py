import pprint
students={"Dilip":["English", "Maths", "Science"],
   "Raju":{"English":50,"Maths":60, "Science":70},
      "Kalpana":(50,60,70)}
print ("using pformat method")
pp=pprint.PrettyPrinter()
string=pp.pformat(students)
print (string)
print ('------')
print ("using pformat function")
string=pprint.pformat(students)
print (string)