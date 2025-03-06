# D = {'P': 'PYTHON', 'F': 'FEES', 'M': 'MATHS', 'E': 'ENGLISH'}
# Student = {'ROLL NO': 123, 'NAME': 'ABC', 'GENDER': 'M'}
# print(D)
# print(Student)


D = {'P': 'PYTHON', 'F': 'FEES', 'M': 'MATHS', 'E': 'ENGLISH'}
Student = {'ROLL NO': 123, 'NAME': 'ABC', 'GENDER': 'M'}
name = Student.get('NAME')
print("Student's name is:",name)
Student['AGE'] = 20
Student['NAME'] = 'XYZ'
Student.pop('GENDER')
print(Student)
