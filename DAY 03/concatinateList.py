list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d"]
# extending the list1 via list2
list1.extend(list2)
print(list1)

# concatinate two list
list3 = [11, 22, 33, 44, 55]
list4 = ["aa", "bb", "cc", "dd", "ee"]
list3 = list3 + list4
print(list3)

#  using for loop
list5 = [1,2,3,4,5]
list6 = ["ax", "bx", "cx"]
for i in list5:
    list6.append(i)
print(list6)

"""
Python - Join Lists
Join Two Lists
There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator.

ExampleGet your own Python Server
Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
Another way to join two lists is by appending all the items from list2 into list1, one by one:

Example
Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
Or you can use the extend() method, where the purpose is to add elements from one list to another list:

Example
Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
"""