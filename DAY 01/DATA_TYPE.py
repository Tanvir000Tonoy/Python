"""
Author Name : Tanvir Rahman Tonoy
Reference : https://www.w3schools.com/python/default.asp
Date 01/08/2024 : My aim is to master the concepts of Python so that I can achieve my milstone of Machine learning
Motivation : তুমি কিছু পারো না। পারবে ও না ।
"""
# type String
msg = "Hello I'm Learning Python Data Types"
print(type(msg))
print(msg)

# type Number
num1 = 1
num2 = 1.1
num3 = 1j
print(type(num1), type(num2), type(num3))
print(num1, num2, num3)

# type sequence
li = ["Tania", "Jannati", "Sinthiya"]
tup = ("Ador", "shimul", "tasrif")
rang = range(5)
print(type(li), type(tup), type(rang))
print(li, tup, rang)

# Type mapping
dic = {
    "name": "Tanvir Rahman Tonoy",
    "Age": 21,
    "mail": "tat.developer.io@gmail.com"
    }
print(type(dic))
print(dic)

# Type : set
set1 = {"10", "20", "32", "11"}
set2 = frozenset(set1)
print(type(set1), type(set2))
print(set1, set2)

# Type : Boolean
x = True
y = False
print(type(x), type(y))
print(x, y)

# Type : Binary
var1 = b"Hello"
var2 = bytearray(5)
var3 = memoryview(bytes(5))
print(type(var1), type(var2), type(var3))
print(var1, var2, var3)

# Type : none
a = None
print(type(a))
print(a)
