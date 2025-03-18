# Write a Python program that generates a password with the following conditions:
    # At least one uppercase letter.
    # At least one lowercase letter.
    # At least two numbers.
    # At least one special character (e.g., !@#$%&*).
    # The password should be exactly 16 characters long.
    # The password should contain no repeating characters.
    # The password should have a random order each time.


# random.choice() gives a random element from the given sequence (can include repetition, No repetition = random.sample())

import random
import string

def generate_passwd():

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_char = string.punctuation

    password = [random.choice(uppercase),
                random.choice(lowercase),
                random.choice(digits),
                random.choice(special_char) ]
    
    all_characters = uppercase + lowercase + digits + special_char
    passwd_len = 12
    password += random.sample(all_characters, k=passwd_len)
    random.shuffle(password)
    return ''.join(password)


print("Do you want a strong pasword hehe? ")
yourchoice = input("(Y)es or (N)O: ")
yourchoice = yourchoice.upper()
match yourchoice:
    case "Y":
        print("")
        print(generate_passwd())
    case "N":
        print("Bad Choice")
    
