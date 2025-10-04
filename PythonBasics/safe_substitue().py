from string import Template
tempStr = Template('Hello. My name is $name and my age is $age')
dct = {'name' : 'Pushpalata'}
newStr = tempStr.safe_substitute(dct)
print (newStr)