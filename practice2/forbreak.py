fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


for x in range(6):
  print(x)
else:
  print("Finally finished!")
  #The else block will NOT be executed if the loop is stopped by a break statement


for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")