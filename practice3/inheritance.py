class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person): #this is a "child" class while Person is "parent"
  pass #use pass when you don't want to modify anything with the parent class

x = Student("Mike", "Olsen")
x.printname()



class Student(Person):
  def __init__(self, fname, lname): #child init OVERRIDES parents init
    Person.__init__(self, fname, lname) #if you want to leave parents init then write this



class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
#super() will keep both parents init and childs init
# without super there in child class will be only childs own init not parents init.
x = Student("Mike", "Olsen", 2019)



class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
ax=Student("Aizere","Tursynbek","2025")
ax.welcome()