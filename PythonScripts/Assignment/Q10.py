# You have to modify a tuple item without converting it into a list. Provide an example of any case where this exactly can happen. 

my_tuple = (1, 2, 3, 4)
print(my_tuple)


# This will raise TypeError: 'tuple' object does not support item assignment
try:    
    my_tuple[1] = 5
except TypeError as e:
    print(f"{e}")

# The only ways to "modify" a tuple are:
# Creating a new tuple with the modified values (re-assign the values)
# my_tuple = (1,5,3,4)

# Converting to a mutable type like a list, making changes, then converting back - Cannot Use

# Using tuple concatenation to create a new tuple
my_tuple = (1, 2, 3, 4)
# Creating a new tuple with modified values
my_tuple = my_tuple[:1] + (5,) + my_tuple[2:]  # my_tuple 0th element + (5, ) What we want to add + my_tuple 2nd till last elment
print(my_tuple)


