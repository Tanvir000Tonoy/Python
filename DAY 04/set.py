thisIsASet = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(thisIsASet)

# unchangable , unordered , unindexed
# so we cann't actually add x[1] to access a particular item

thisIsASet.add(("tina", "mina", "sina"))
print(thisIsASet)

extra = ["item1", "item2"]
thisIsASet.update(extra)
print(thisIsASet)


#  learn how to delete or clear the set
thisIsASet.remove("item1")
print(thisIsASet)
# what if there is no element like we mentioned into the remove method ?
""" thisIsASet.remove("Ador") """
# it will generate an error
thisIsASet.discard("fuck")
# it did nothing even the item is not there
thisIsASet.clear()
print(thisIsASet)
thisIsASet.add(("ina", "mina", "tina", "dina"))
print(thisIsASet)
del thisIsASet
thisIsASet = {""}
print(thisIsASet)