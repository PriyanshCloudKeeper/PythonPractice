intlist = [1,2,3,4,5,6,7,8,9,10]
strlist = ["Hi", "My", "Name", "is", "Priyansh"]
print(strlist[::-1])
print(strlist[2:5])

print("\n")

intlist.append(11)
intlist.insert(0, 0)
print(intlist)
print(1 in intlist)
print(len(intlist))

print("\n")

users = {'Hans' : "Active", "DepressedSaint": 'Inactive', "Random": "Active"}
active_user = {}
for user, status in users.items():
    if status.lower() == "active":
        active_user[user] = status
print(active_user)

strlist = ["Hi", "My", "Name", "is", "Priyansh"]
for i in strlist:
    print(i)

for i in range(len(strlist)):
    print(strlist[i])

print(''.join(strlist))


users = {'Hans' : "Active", "DepressedSaint": 'Inactive', "Random": "Active"}
for counter, (user, status) in enumerate(users.items()):
    print(f"{counter}, {user}, {status}")


# List Comprehension - short way to create or a list. 
# Structure : [expression for item in iterable]
# Empression: value to add in new list, item: each item in a list, iterable: collectipon we are iterating.

print("\n"*15)

fruits = ['apple', 'banana', 'cherry']

# Create a new list that contains the lengths of each fruit name:
fruits_len = [len(fruit) for fruit in fruits]
print(fruits_len, fruits)

# Adding conditions
fruits_len2 = [len(fruit) for fruit in fruits if len(fruit) > 5]
fruits2 = [fruit for fruit in fruits if len(fruit) > 5]
print(fruits_len2, fruits2)


# Extracting Specific Attributes from Dictionaries
# This is a dictionary containing product details
product_details = {
    "apple": {'price': 1.5, 'quantity': 10},
    "banana": {'price': 0.5, 'quantity': 20},
    "cherry": {'price': 2.0, 'quantity': 15},
}

# In details.get() we can set a default value and if key does not exist it gives None
# But in details[] is the key does not exist it will throw error: KeyError

# quantities = [details["quantity"] for details in product_details.values()]
# print(quantities)

quantities = [details.get("quantity", 1) for details in product_details.values()]
print(quantities)

