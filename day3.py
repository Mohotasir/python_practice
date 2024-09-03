# ##########################  TUPLE  #################################

# AS Tuple are unchangeable , so to update tuple first of all
# it converts into list then update and after updating again change into tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#  The del keyword can delete the tuple completely:
del x
# pack tuple :
fruits = ("apple", "banana", "cherry")
# unpack tuple:
(green, yellow, red) = fruits
print(green)
# If the number of variables is less than the number of values, you can add an *
# to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, ye, *redd) = fruits
print(green)
print(yellow)
print(red)

# loop through the index number
for x in range(len(fruits)):
    print(fruits[x])

print(fruits.count("banana"))

# ####################################  SET  ##################################################################
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# To add items from another set into the current set, use the update() method.
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# remove items
thisset.remove("apple")
thisset.discard("mango")  # If the item to remove does not exist, discard() will NOT raise an error.
remain = thisset.pop()  # delete a random item
print(remain)

# set union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
set4 = set1 | set2
print(set3)

# #######################################  DICTIONARIES  #########################################################
dictionary = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}
print(dictionary)
print(len(dictionary))

dic = dictionary["brand"]  # method-1
dic1 = dictionary.get('brand')  # method-2
print(dic)

keys = dictionary.keys()   # return all keys...
values = dictionary.values()  # return all values
print(keys)
dictionary.update({"year": 1289})  # update value
print(dictionary)

dictionary.pop("model")  # delete items
dictionary.popitem()  # delete the last inserted item


for x in dictionary:
    print(x)  # show the key
    print(dictionary[x])  # show the value

for x in dictionary.values():
    print(x)  # return all values........................


for x, y in dictionary.items():
    print(x, y)  # show both keys and values

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])

# ########################################  IF ELSE  ELIF  #############################################################
a = 44
b = 35
if a > b:
    print("a big")
else:
    print("b big")


print("a is big") if a > b else print("b is big")  # shorthand of if...else
# if statements cannot be empty, but if you for some reason have an
# if statement with no content, put in the pass statement to avoid getting an error.
if b > a:
    pass

for x in range(6):   # range (3,6) also possible
    print(x)

''' The range() function defaults to increment the sequence by 1,
    however it is possible to specify 
    the increment value by adding a third parameter: range(2, 30, 3) '''
for x in range(2, 30, 3):
    print(x)

#  ########################### function ########################################
def tri_recursion(k):
    if(k > 0):
       result = k + tri_recursion(k - 1)
       print(result)
    else:
       result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)