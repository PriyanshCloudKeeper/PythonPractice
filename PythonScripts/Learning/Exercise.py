previous_num = 0
for i in range(0, 10):
    sum = previous_num + i
    print(sum)
    previous_num = i


str = input("Enter a string: ")
num = len(str)

for i in range (0, num-1, 2):
    print(str[i])

print("\n")

def remove_char(str, n):
    return str[n:]

word = input("Enter a word: ")
num = int(input("Enter the first n characters from a string: "))
print(remove_char(word, num))

def checknum(numberlist):
    first = numberlist[0]
    last = numberlist[-1]

    if first == last:
        return True
    else:
        return False


print("\n")

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

print(checknum(numbers_x), checknum(numbers_y))

print("\n")

def reciprocal(num):
    return 1/num

lambda_reciprocal = lambda num: 1/num

print( "Def keyword: ", reciprocal(6) )  
   
print( "Lambda keyword: ", lambda_reciprocal(6) )  


