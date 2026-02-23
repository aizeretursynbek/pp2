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

json.dumps(x, indent=4, separators=(". ", " = "))

json.dumps(x, indent=4, sort_keys=True)
# Use the sort_keys parameter to specify if the result should be sorted or not


