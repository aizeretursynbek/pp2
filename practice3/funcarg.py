def my_function(name): # name is a parameter
  print("Hello", name)
my_function("Emil") # "Emil" is an argument


def my_function(name = "friend"):
  print("Hello", name)
#You can assign default values to parameters. If the function is called without an argument, it uses the default value
my_function("Tobias")
my_function()


def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function(animal = "dog", name = "Buddy")
#key = value syntax.(keywords arg = kwargs)
#This way, with keyword arguments, the order of the arguments does not matter.


def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function("dog", "Buddy")
#without keywords they are called POSITIONAL arguments.
#the order of arguments matters with positional arguments


def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)
#we can mix positional and kw arguments. However, positional arguments must come before keyword arguments
my_function("dog", name = "Buddy", age = 5)


def my_function(name, /):
  print("Hello", name)
#"/" means pos args only if you try to use keywords it will return an error
my_function("Emil")


def my_function(*, name):
  print("Hello", name)
# "*" before parameter means kwargs only
my_function(name = "Emil")


def my_function(a, b, /, *, c, d): ## to mix pos and kwargs
  return a + b + c + d
#Arguments before / are positional-only, and arguments after * are keyword-only
result = my_function(5, 10, c = 15, d = 20)
print(result)


def my_function(*args): # arbitrary arguments
  #The *args parameter allows a function to accept any number of positional arguments
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)
my_function("Emil", "Tobias", "Linus")


def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total
#A function that calculates the sum of any number of values
print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))


def my_function(username, **details): #arbitrary keyword arguments
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)
#
my_function("emil123", age = 25, city = "Oslo", hobby = "coding")