x = "awesome"

def myfunc():
  global x
  x = "fantastic"
  #we changed the value of global x to "fantastic" by declaring it global inside of the func

myfunc()

print("Python is " + x)