# Ctrl + / to comment out the line
# Shift + Alt + A to comment out a block of code
# Shift + Alt + Up/Down to use multi cursor editing
# Type Annotation- a: int = 5, So if a hacker comes he just can't manipulate the code and put any value and break the code. we can specify the type of the variable
# inf() - Denotes an infinite number
# package ka naam sa kabhi file ka naam maat rakhna

'''
This is a multi-line comment
'''

print("Hello World")

# year = int(input(("Enter your birth year: ")))

a = "Hello, World"
print(a.split(",")) # ['Hello', 'World']
print(a.split(",")[-1]) # World
print(a[::-1]) # dlroW ,olleH

b = 10%1
c = 1%10
print(b, c)

# or gives precedence to the first expression, and and gives precedence to the second expression

print("Hello") or print("World") # Hello Prints as Hello is the first expression, prints or is then none(False Basically) so as in or, there is one Flase, still World prints
print("Hello" and "World")  # World Prints as World is the last expression, prints and is then none(False Basically) so as in and, there is one False so Hello does not prints
print(print("Hello")) # Phele Hello print huega, phir None print hoga, None type boolen expression None hota hai

# else can be used without if

for z in range(2,6,2):
    print(z) # 2 4

d = {True:"A", 1:"B", 1.0:"C"} # There can be no duplicate keys in a dictionary, so True, 1 and 1.0 are same
print(len(d)) # 1 
print(d) # {True: 'C'} Value gets replaced, as it can keep the value but not the key

def my_funP(x, /):
    print(x)

my_funP(3) #my_fun(3) will give an error as using / we have set a Position-Only Argument

def my_funA(*, x):
    print(x)

my_funA(x=3) #my_fun(3) will give an error as using * we have set a Keyword-Only Argument

# Object and Classes
# Static Methods

class MyClass:
    def __init__(self):
        self.x = 10

obj = MyClass()
print(obj.x)  # Output: 10
obj.x = 20
print(obj.x)  # Output: 20
del obj.x
print(obj.x)  # Output: 10? as when we delete the x only 20 deleted but x is still 10 as we have updated the x to 20 but the original value of 10 exists.

# Multiprocessing - CPU dependent - Run Multiple Process at he same time (parallely:)
# Multithreading - OS dependent - Allows a program to run multiple tasks at the same time (concurrently:)
# Process - a running program 
# Threads - process ka sabse chota tukda
# Practical Example: 
# GIL - Ek hee tread ka control leta hai python, ie it allows only one thread to run at a time, preventing multithreading inherently. Can use multithreading using threading module