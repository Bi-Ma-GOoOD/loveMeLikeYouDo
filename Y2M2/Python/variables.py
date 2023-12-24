## Python Variables
# create variables
x = 5
y = "john"
print("x = ", x)
print("y = ", y)

x = 4
x = "Sally"
print("x = ", x)

# casting
x = str(3)
y = int(3)
z = float(3)
print(x+x)
print(y+y)
print(z)

# get the type
x = 5
y = "John"
print(type(x))
print(type(y))

# case sensitive
a = 4
A = "Sally"
print("a = ", a)
print("A = ", A)

## Assign Multiple Values
# many values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# one value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# unpack a collection
fruits = ['apple', "banana", "cherry"]
print(fruits[0])