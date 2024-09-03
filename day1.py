import sys
import pip
# ####################### VARIABLE DATATYPE ###############

print("hello py")

# for checking the editor python version
print(sys.version)
print(pip.List)
# condition checking with indentation
var1 = 4
var2 = 3
if var1 < var2:
    print(1)
else:
    print("false")

# many value to multiple variables
x, y, z = "Orange", 2, "Cherry"
print(x)
print(y)
print(z)

# one value to multiple variables
x = y = z = "xoxo"
print(x)
print(y)
print(z)

# type checking
value = str(5)
print(type(value))

# casting
p = '34'
print(type(p))
m = int(p)
print(type(m))

# string
name = 'beginner'
print(name[2])  # res : g
print(len(name))

# check a part of string
quote = "honesty is the best policy"
if "are" in quote:
    print("are is present")
else:
    print("Not present")
if 'are' not in quote:
    print("that ok !!!!!!!!")

# slicing]
b = "Hello, World!"
print(b[2:8])
print(b.upper())

# remove whitespace
print(b.strip())

# ALL STRING METHODS

