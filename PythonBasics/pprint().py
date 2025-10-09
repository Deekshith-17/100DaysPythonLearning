from pprint import pprint
students={"Dilip":["English", "Maths", "Science"],
   "Raju":{"English":50,"Maths":60, "Science":70},
      "Kalpana":(50,60,70)}
print ("normal print output")
print (students)
print ("----")
print ("pprint output")
pprint (students)