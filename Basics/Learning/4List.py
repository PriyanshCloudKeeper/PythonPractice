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

