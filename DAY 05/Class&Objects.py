class elts:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Excuse me"
    def info(self):
        print(f"Hi my Name is {self.name} and I'm {self.age} year's old")
newObj = elts("Tanvir","20")
# print(newObj)
print(newObj.info())
del elts
# so if we call print inside a print function it will return a none value
