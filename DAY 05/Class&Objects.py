class Hello:
    def __init__(self):
        print("class : hello")
    def DoSomething(self,Hi):
        return f"Hello {Hi}"
it = Hello()
x = it.DoSomething("Hello")
print(x)
