"""
Day 02 : 02/08/2024
This is morning 6:00 I just woke up around 5 . I'm trying to cover the concepts of python
Author : Tanvir Rahman Tonoy
"""
# This is also known as array to me in javascript

myDevices = ["Computer", "Laptop", "Phone"]
print(myDevices)
print(type(myDevices))



"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

"List" is a collection which is ordered and changeable. Allows duplicate members.
"Tuple" is a collection which is ordered and unchangeable. Allows duplicate members.
"Set" is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
"Dictionary" is a collection which is ordered** and changeable. No duplicate members.
"""

print(len(myDevices))

# list item data types
list1 = ["String", 1, 1.1, 1j, True,[1, 2, 3]]
print(list1)

# creating list with a constructor
list2 = list(("Hello", "hi", "bye bye"))
print(list2)
print(type(list2))

# access a item from the list with the index number
print(list1[0])
# range of items
print(list1[0:4]) # last item will not be included
print(list1[:4])
print(list1[0:])

# Negative indexing
print(list1[-4:-1])

# check if its there
print(True in list1)

# inset method in list
list1.insert(6,"Hi Tonoy")
print(list1)
# append method
list1.append("Honey")
print(list1)

# adding two list together will be done by extend method
li1 = [1, 2, 3, 4, 5, 6]
li2 = ["hello", "hi", "bye"]
li1.extend(li2)
li2.extend(li1)
print(li1)
print(li2)
# we can add any iterable in this way to concatenate two objects
tuple1 = ("tania", "jannati", "sinthia")
list0 = ["tonoy", "rong", "modhu"]
list0.extend(tuple1)
print(list0)

# removing items from a list
# remove()
# pop()
# del
# clear()
x = [1,2,3,4,5]
print(x)
x.remove(3) # it will remove 3 from the list
print(x)
x.pop(2) # it will banish the 2nd index of the list
print(x)
del x[0] # it will delete the 1st index
print(x)
x.clear() # clear the list ;)
print(x)