from string import Template

tempStr = Template('Hello. My name is $name and my age is $age')
newStr = tempStr.substitute(name = 'Pushpa', age = 26)
print (newStr)