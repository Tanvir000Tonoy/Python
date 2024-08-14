x = 10
def local():
    x = 11
    return x
print(x)
print(local())
print(x)
# you can see x value is 10 and the something() value is 11 that means both x is different
# x inside the functionis a local variable and outside x is a global variable
# lets comment out the x inside the function
print("New process")
y = 10
def nothing():
    return y
print(y)
print(nothing())
# now the function has the access of global y
# but what if we do it like this
print("new code")
def xyz():
    global a
    a = 10
    return a
print(xyz())
print(a)
# we have an error that a is not defined that means we do not have the access to call a variable from outside of a function
# we can do that

# another instance
def func1():
    x ="fuck"
    def innerFunc():
        nonlocal x
        x = "Love"
        return x
    innerFunc()
    def innerFunc2():
        nonlocal x
        x = "sex"
        return x
    innerFunc2()
    return x


print(func1())

