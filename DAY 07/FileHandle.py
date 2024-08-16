anObject = open("onumate.txt", "a")
anObject.write("Hello Tonoye")
anObject = open("onumate.txt", "r")
print(anObject.read())
try:
    x = open("onumate.txt", "x")
except:
    print("File already exists")
import os
os.remove("onumate.txt")
try:
    x = open("onumate.txt", "r")
except:
    print("File does not exist")

try:
    x = open("onumate.txt", "x")
    print("File has been created")
except:
    print("File already exists")

if os.path.exists("onumate.txt"):
    os.remove("onumate.txt")
# :) Happy coding