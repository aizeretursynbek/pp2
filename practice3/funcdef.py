def my_function(): #my_fuction is the name of the function
  print("Hello from a function")


def my_function():
  print("Hello from a function")
my_function()
my_function()
my_function()


def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))
#if we use return in the func then to receive the result we have to use print()


def get_greeting():
  return "Hello from a function"
message = get_greeting() #or we can obtain the RETURN value to the parametre
print(message)


def my_function():
  pass