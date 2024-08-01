print("Hello i'm Tanvir" + ' I Love "Computer"')
# will it work ?
# Yes :)
a = """
Hello I'm Tanvir Tonoy.
I love "Computer".
"""
print(a)

# looping through string
for x in a:
    print(x)

# string length
print(len(a))

# check if there is "this" in a string
print("tanvir" in a.lower())


#  check if not in the string
print("Sinthia" not in a)

# sliceing string
print(a[:10])
print(a[10:])
"""
we can use negative index too like x = "hello" -> print(x[-4:-1]) => ell
"""

#  modifying string
x = "   Amra korbo joy  "
y = x.upper()
z = x.lower()
print(x, y, z)

# removing white space || white space means space before and after the main string like '---hi---' will be cut off
# and print only 'hi'
a = x.strip()
print(a)

# replaceing strings
thisIsAString = "Good eveing Tonoy. How are you ?"
replacedString = thisIsAString.replace("Good", "Bad")
print(thisIsAString)
print(replacedString)

# The split() method returns a list where the text between the specified separator becomes the list items.
thisIsAString = thisIsAString.split(" ")
print(thisIsAString)
print(type(thisIsAString))
# this is a list now :)

# String concatenate
string1 = "First Name :"
stirng2 = "Tanvir"
print(string1 + stirng2)


# Formating string
"""
often we need to create string template . how we can do it on python ? this is done by string formating . 
use f"" <- this formate to do so. Here is an instance
"""
name = "Tanvir Rahman Tonoy"
country = "Bangladesh"
FatherName = "Ziarul Islam"
MotherName = "Taslima Akter"
SisterName = "Afifa Akter"
template = f"Hi My Name is {name} .I am from {country}. My father name is {FatherName} and my mother name is {MotherName} . I have one sister name {SisterName}"
print(template)
def countx():
    return "1,2,3,4,5,6,7,8,9,10"

count = f"I can count like {countx()}"
print(count)
#  { } this is called placeholder because it can hold python code inside it

# escape notation or character '\' followed by ',\, n,r,t,b,f,000,xhh
print("HI \n I'm \n \"tonoy\"")


"""
All string methods return new values. They do not change the original string.
"""

# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning