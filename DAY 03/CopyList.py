list1 = [1,2,3,4]
list2 = list1
print(list1)
print(list2)
list1[3] = "changed"
print(list2)
# so we cann't actually created a new list it's simple the reference of the list1 thats why changing list1 will affect the list2

# some methods and operator to copy list items in a new item is :
# copy()
# list()
# (:)

list2 = list1.copy()
print(list2)
# if we change list 1 it will not affect list1
list1.append("BadBoy")
print(list1)
print(list2)

# this is method 1
# we can do it with list method too
list2 = list(list1)
list1.append(100)
print(list1)
print(list2)

# last but not least -> : operator slice
list2 = list1[:]
list1.append(":")
print(list1)
print(list2)
