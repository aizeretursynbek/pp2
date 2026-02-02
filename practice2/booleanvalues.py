a =True
b=False


print(10 > 9)
print(10 == 9)
print(10 < 9)


class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))


def is_even(x):
    return x % 2 == 0
is_even(4)   # True
is_even(7)   # False


def myFunction() :
  return True
print(myFunction())


