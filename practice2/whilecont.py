i = 0
while i < 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i)


while True:
    text = input()
    if text == "":
        continue
    if text == "stop":
        break
    print("You typed:", text)


i = 1
while i <= 10:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1


arr = [5, -2, 3, -1, 7]
i = 0

while i < len(arr):
    if arr[i] < 0:
        i += 1
        continue
    print(arr[i])
    i += 1


i = 1
while i <= 10:
    if i % 2 != 0:
        i += 1
        continue
    print("First even:", i)
    break
