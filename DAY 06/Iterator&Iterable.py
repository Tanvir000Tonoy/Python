"""
Date : 15 August 2024
Author: Tanvir Tonoy
This is 15 august of 2024 and I'm learning about Iterator and Iterable in Python.
"""
tuple1 = ("a","b","c","d")
iterable1 = iter(tuple1)
print(next(iterable1))
print(next(iterable1))
print(next(iterable1))
print(next(iterable1))

for x in tuple1:
    print(x)


