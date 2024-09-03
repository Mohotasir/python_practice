# ######################### LIST ######################
list1 = ["abc", 34, True, 40, "male"]
print(list1[2:4])

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# add value in list
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist1 = ["apple", "banana", "cherry"]
thislist1[1:3] = ["watermelon"]
print(thislist1)

#insert items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# append() , insert() , extend()
thislist.append("orange")
print(thislist)
thislist.extend(thislist1)
print(thislist)

# looping in list
for i in range(len(thislist)):
  print(thislist[i])
for i in thislist:
    print(i)

# while loop
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# A short hand for loop that will print all items in a list
[print(x) for x in thislist]

# create new list / list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

##################################
newlists = [x for x in fruits if "a" in x]
print(newlists)
##################################

# sort in descending order
newlists.sort(reverse=True)
print(newlists)
# case-insensitive sort
newlists.sort(key = str.lower)
print(newlists)


