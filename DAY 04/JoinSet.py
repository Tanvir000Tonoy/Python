"""
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.

"""
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}
set3 = set1.union(set2) # or set1 | set2
print(set3)
set4 = {2, 4, 6, 8}
set5 = set3.intersection(set4) # we can use set3 & set5
print(set5)
set3.intersection_update(set4)
print(set3)

setA = {'a', 'b', 'c', 'd'}
setB = {'c', 'f', 'g', 'h'}
setX = setA.difference(setB) # we could have used setA - setB
print(setX)
setA.difference_update(setB)
print(setA)
seta = {0,1,2,3}
setb = {2,3,4,5}
setc = seta.symmetric_difference(setb) # we could have used seta ^ setb
print(setc)
# symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
print(seta.isdisjoint(setb))
print(seta.issubset(setb))
# write a set in python that contains 0-20 in number
# Create a set that contains numbers from 0 to 20
number_set = set(range(21))
print(number_set)
print(seta.issubset(number_set))
print(number_set.issuperset(seta))