def my_function(a, b, c):
  return a + b + c
#The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.
numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)


def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")


def my_function(fruits):
  for fruit in fruits:
    print(fruit)
#Sending a list as an argument
my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)


def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])
#Sending a dictionary as an argument
my_person = {"name": "Emil", "age": 25}
my_function(my_person)


def my_function():
  return (10, 20)
#A function that returns a tuple:
x, y = my_function()
print("x:", x)
print("y:", y)


def my_function():
  return ["apple", "banana", "cherry"]
#A function that returns a list:
fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])