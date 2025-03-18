i = 1
while i <= 10:
    print(i * '*')
    i += 1

print("\n")

numbers = [1,2,3,4,5]
for i in numbers:
    print(i)
    i +=1

print("\n")

for i in range(len(numbers)):
    print("Hi")
    print(numbers[i])
    i = i+1

print("\n")

num = [1,2,3,4,5,6,7]

for i in num:
    print(i)
    if i == 7:
        break