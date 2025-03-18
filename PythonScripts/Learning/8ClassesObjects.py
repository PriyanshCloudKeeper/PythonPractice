class MyClass:
    def __init__(self):
        self.x = 10

obj = MyClass()
print(obj.x)  # Output: 10
obj.x = 20
print(obj.x)  # Output: 20
del obj.x
print(obj.x)  # Output: 10? as when we delete the x only 20 deleted but x is still 10 as we have updated the x to 20 but the original value of 10 exists.