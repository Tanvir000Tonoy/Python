import datetime
x = datetime.datetime.now()
print(x)

y = datetime.datetime(2003,9, 17)
print(y.strftime("%a")) # day
print(y.strftime("%A")) # day full name
print(y.strftime("%w")) # week as a number
print(y.strftime("%d")) # date
print(y.strftime("%C"))

