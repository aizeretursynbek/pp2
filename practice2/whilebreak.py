i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


arr = [2, 5, 8, 10]
target = 8
i = 0
while i < len(arr):
    if arr[i] == target:
        print("Found!")
        break
    i += 1


while True:
    word = input()
    if word == "stop":
        break
    print("You typed:", word)


i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
        break
    i += 1
