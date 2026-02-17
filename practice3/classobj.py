class MyClass:
  x = 5
p1 = MyClass() #object
print(p1.x)
del p1 #You can delete objects by using the del keyword:


class Person:
  def __init__(self, name, age): #The __init__() method is used to assign values to object properties
    self.name = name
    self.age = age
#The __init__() method is called automatically every time the class is being used to create a new object.
p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)



class Person:
  def __init__(self, name, age=18): #It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any method in the class.
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()



class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome()
del Person.greet #if you want to delete the method.
#why it is called "method"? Because all methods like len(),sorted() and etc is given by base Class of python.
#in short class contains methods(not just functions) which we can use while coding outside by objects as we do it to all methods.


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tobias", 25)
print(p1.age)

p1.age = 26
print(p1.age)
del p1.age
print(p1.name) # This works
# print(p1.age) # This would cause an error



class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)
Person.species="Male" #you can change the class property and it will be changed.
Person.age=12 #also you can add new property to the class
print(p1.age, p2.age)


class Person:
  def __init__(self, name, age): #without __str__() there would be no outputs
    self.name = name
    self.age = age

  def __str__(self): #The __str__() method is a special method that controls what is returned when the object is printed
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1) 
#without __str__ there output of print(p1) will be <__main__.Person object at 0x000001B117AF86E0>
#str allows execute certain command when u will print the object.



