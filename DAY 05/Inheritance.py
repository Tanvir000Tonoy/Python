class Class1:
    def __init__(self):
        self.property1 = "Tonoy"
        self.property2 = "Mia"

class Class2(Class1):
    def __init__(self):
        super().__init__()
C2 = Class2()
print(C2.property1)
print(C2.property2)