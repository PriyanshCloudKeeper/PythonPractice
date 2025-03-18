name = 'John Smith'
age = 20
status = 'New Patient'

name = input("What is your name? ")
print("Hello "+ name)

birth_year = int(input("Enter your birth year: "))
age = 2025 - birth_year
print(age)

# Types
int(), float(), bool(), str(), list(), tuple(), dict(), set(), complex()

int1 = float(input("Enter first number: "))
int2 = float(input("Enter second number: "))
sum = int1 + int2
print("Sum: "+ str(sum))

course = 'Hello World'
# 'Hello World' here is a object, there are many things we can do to it, so there many capabilites available for a string object. Function for objects = methods
print(course.upper())
print(course.strip())
print(course.find('W'))

# Operators
print(10+3, 10-3, 10*3, 10**3, 10/3, 10//3, 10%3)

# f-string and formating
result = 100000
print(f'Results for the 2020 quater are: {result}')

import math
print(f'The value of pi is approx: {math.pi:.3f}.')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')


