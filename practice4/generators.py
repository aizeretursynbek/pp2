mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
#strings are also iterable objects
print(next(myit))
print(next(myit))
print(next(myit))



class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
#The __iter__() method acts similar as init, you can do operations (initializing etc.), but must always return the iterator object itself.
  def __next__(self):
    x = self.a
    self.a += 1
    return x
#The __next__() method also allows you to do operations, and must return the next item in the sequence.
myclass = MyNumbers()
myiter = iter(myclass)
# for loop do the same as iter and next methods
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))



class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
#To prevent the iteration from going on forever, we can use the StopIteration statement.
#the iteration will proceed forever if for loop was used.
myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)



def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt 
        cnt += 1
#Yield: is used in generator functions to provide a sequence of values over time.
ctr = fun(5)
for n in ctr:
    print(n)



def fun():
    yield 1            
    yield 2            
    yield 3            
#A generator function is a special type of function that returns an iterator object.(the function above is the generator function it uses yield to produce series)
# Driver code to check above generator function
for val in fun(): 
    print(val)



sq = (x*x for x in range(1, 6)) #generator object
for i in sq:
    print(i)