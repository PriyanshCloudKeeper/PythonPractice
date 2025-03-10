temprature = 35
if temprature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temprature > 20:
    print("It's not a nice day")

weight = float(input("Enter your weight: "))
ans = input("Is your weight in:\n(K)g or (L)bs: ")
if ans.upper() == "K":
    print("Weight in Kg(s): " + str(weight))
elif ans.upper() == "L":
    print("Weight in Lbs(s): " + str(weight/0.45))
else:
    print("Invalid Input")

price = 5
print(not price > 10, price > 3 or price < 4, price < 5 and price > 4)