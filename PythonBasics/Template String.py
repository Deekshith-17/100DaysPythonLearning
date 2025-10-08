from string import Template

temp_str = "My name is $name and I am $age years old"
tempobj = Template(temp_str)
ret = tempobj.substitute(name='Rajesh', age=23)
print (ret)