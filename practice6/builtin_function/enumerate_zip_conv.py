n=int(input())
m=list(map(str, input().split()))
for i,b in enumerate(m):
    print(f"{i}:{b}",end=" ")


fruits = ["apple", "banana", "orange"]

for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)


n=int(input())
m=list(map(int, input().split()))
l=list(map(int, input().split()))
sum=0
for i,b in zip(m,l):
    c=i*b
    sum+=c
print(sum)


a = [1, 2, 3]
b = ["x", "y"]
for x, y in zip(a, b):
    print(x, y) # 1 x and 2 y


names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
zipped = zip(names, scores)
print(list(zipped))

for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(i, name, score)
    # 1 Alice 85
    # 2 Bob 92
    # 3 Charlie 78


student_dict = dict(zip(names, scores))
print(student_dict)
# {'Alice': 85, 'Bob': 92, 'Charlie': 78}
    

x = 10
y = "hello"
z = [1, 2, 3]
print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
print(type(z))  # <class 'list'>


if isinstance(x, int):
    print("x is an integer")
if isinstance(y, str):
    print("y is a string")
if isinstance(z, list):
    print("z is a list")
#checking particular type


s = "hello world"
lst = list(s)
print(lst, type(lst))  
# ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']


lst = [1, 2, 3]
s = str(lst)
print(s, type(s)) 


n = 10
f = float(n)
print(f, type(f))


s = "123"
num = int(s)   # преобразуем строку в int
print(num, type(num))


n = 456
s = str(n)
print(s, type(s))