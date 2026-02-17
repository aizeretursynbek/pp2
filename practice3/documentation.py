def changecase(func):
  def myinner():
    return func().upper()
  return myinner
#Define the decorator first, then apply it with @decorator_name above the function.
@changecase
def myfunction():
  return "Hello Sally"
#The function changecase is the decorator.
# The function myfunction is the function that gets decorated.
print(myfunction())


def changecase(func):
  def myinner():
    return func().upper()
  return myinner
@changecase
def myfunction():
  return "Hello Sally"
@changecase
def otherfunction():
  return "I am speed!"
print(myfunction())
print(otherfunction())


def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner
@changecase
def myfunction(nam):
  return "Hello " + nam
print(myfunction("John"))


def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase
@changecase(1)
def myfunction():
  return "Hello Linus"
print(myfunction())


def changecase(func):
  def myinner():
    return func().upper()
  return myinner
def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner
@changecase
@addgreeting
def myfunction():
  return "Tobias"
print(myfunction())


def changecase(func):
  def myinner():
    return func().upper()
  return myinner
@changecase
def myfunction():
  return "Have a great day!"
print(myfunction.__name__)


import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)
