items = [1, 2, 3, 4, 5]
for i in items:
    print(i+2)

i = 0
while i < len(items):
    print(items[i])
    i = i+1

# list comprehension
[print(i-1) for i in items]
