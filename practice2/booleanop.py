x = "Hello"
y = 15
print(bool(x)) #True
print(bool(y)) #True


bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
bool(None)
bool(0)
bool("")
bool(())


x = 5
isinstance(x, int)      # True
isinstance(x, float)    # False
isinstance(x, (int, float))  # True


x = 10
y = 5
x > y and y > 0     
x < y or y > 0     
not (x == y)  


3 in [1, 2, 3]       # True
"a" in "apple"      # True
"key" in {"key": 1} # True (checks keys)
4 not in [1, 2, 3]   # True


