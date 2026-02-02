fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)


for x in [0, 1, 2]:
  pass


words = ["hi", "hello", "cat", "elephant", "dog"]
for w in words:
    if len(w) > 4:
        continue
    print(w)
