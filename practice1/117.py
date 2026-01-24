def myfunc():
  global x
  x = "fantastic"
  print(x)

myfunc()

print("Python is " + x)
#if we will not declare x as global inside of the function, then for Python "x" is not defined