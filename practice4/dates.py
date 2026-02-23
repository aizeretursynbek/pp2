def greeting(name): #Save this code in a file named mymodule.py
#mymodule is the name of the module
#Consider a module to be the same as a code library.
#A file containing a set of functions you want to include in your application.
  print("Hello, " + name)

import mymodule
mymodule.greeting("Jonathan")
# When using a function from a module, use the syntax: module_name.function_name.


#The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
} #write it on your module file

import mymodule
a = mymodule.person1["age"]
print(a)



import mymodule as mx
#Create an alias for mymodule called mx
a = mx.person1["age"]
print(a)



import platform
#List all the defined names(list all the function names (or variable names)) belonging to the platform module using dir()
x = dir(platform)
print(x)
#The dir() function can be used on all modules, also the ones you create yourself.



def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}   #The module named mymodule has one function and one dictionary

from mymodule import person1
#Import only the person1 dictionary from the module
print (person1["age"])
#While using from keyword do not use module name when referring to elements in the module
# Example: person1["age"], NOT mymodule.person1["age"]



import datetime
# The datetime module has many methods to return information about the date object.
x = datetime.datetime.now()
print(x)
# the result: 2026-02-23 10:11:42.897725



import datetime

x = datetime.datetime.now()
# Return the year and name of weekday
print(x.year)
print(x.strftime("%A"))



import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))
# %a	Weekday, short version	Wed	
# %A	Weekday, full version	Wednesday	
# %w	Weekday as a number 0-6, 0 is Sunday	3	
# %d	Day of month 01-31	31	
# %b	Month name, short version	Dec	
# %B	Month name, full version	December	
# %m	Month as a number 01-12	12	
# %y	Year, short version, without century	18	
# %Y	Year, full version	2018	
# %H	Hour 00-23	17	
# %I	Hour 00-12	05	
# %p	AM/PM	PM
