import pprint
students={"Dilip":["English", "Maths", "Science"],"Raju":{"English":50,"Maths":60, "Science":70},"Kalpana":(50,60,70)}
pp=pprint.PrettyPrinter()
print ("normal print output")
print (students)
print ("----")
print ("pprint output")
pp.pprint(students)