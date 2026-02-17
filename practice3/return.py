def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil") #TypeError because func expected 2 argumenrs but got only 1 argument


def privet(x):
 x+5
print(privet(6)) # without return statement it will return "None" value


def my_function():
  return ["apple", "banana", "cherry"]
fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])


def my_function():
  return (10, 20)
x, y = my_function()
print("x:", x)
print("y:", y)


def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)
#You can use both *args and **kwargs in the same function
#The order must be: regular parameters, *args, **kwargs
my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")