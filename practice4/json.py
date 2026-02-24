import json
# Convert from JSON to Python
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# notice that this is a json string
# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])



# Convert from Python to JSON
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON STRING:
print(y)



import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))



import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
json.dumps(x, indent=4)
# Use the indent parameter to define the numbers of indents
# индент это своего рода отступ
json.dumps(x, indent=4, separators=(". ", " = "))

json.dumps(x, indent=4, sort_keys=True)
# Use the sort_keys parameter to specify if the result should be sorted or not


with open("data.json", "w") as f:
    # f is our file parameter
    json.dump(data, f, indent=4)
# notice that json.dump writes to file whereas json.dumps converts python obj to json string
# or we can write like this:

f = open("data.json", "w")
json.dump(data, f)
f.close()
# notice that with automatically opens the file and closes.


# read from the file
with open("data.json", "r") as f:
    data = json.load(f)
# loads() works with a string whereas just load() works with files.