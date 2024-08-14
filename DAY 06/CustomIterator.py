class NaturalNumber:
    def __iter__(self):
        self.x = 0
        return self
    def __next__(self):
        a = self.x
        self.x +=1
        return a

xyz = NaturalNumber()
iter(xyz)
print(next(xyz))
print(next(xyz))
print(next(xyz))
print(next(xyz))
print(next(xyz))
print(next(xyz))
print(next(xyz))

