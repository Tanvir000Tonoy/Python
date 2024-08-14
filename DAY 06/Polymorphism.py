class Dog:
    def Sounds(self):
        print("Bhaw! Bhaw!")
class Cat:
    def Sounds(self):
        print("Meaooo! Meaooo!")

class Cow:
    def Sounds(self):
        print("Hambaaaa!")
for x in (Dog(), Cat(),Cow()):
    x.Sounds()