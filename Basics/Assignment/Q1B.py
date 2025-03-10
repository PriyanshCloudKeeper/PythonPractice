#Validate a given email address to check if it’s a valid Gmail address, considering:
    # It should contain "@gmail.com".
    # The username before "@gmail.com" should contain only lowercase letters , numbers and permitted symbols.

import re
def email_check(email):
    regex = r"^[a-zA-Z0-9.%_+-]+@gmail.com$"

    if re.search(regex, email):
        print("The email is valid")
    else:
        print("The email is not valid")

email1 = "priyanshcchoudhary@gmail.com"
email2 = "priyanshcchoudhary+1@gmail.com"
email3 = "priyanshcchoudhary@okla.com"
email4 = "98Likho@gmail.com"

email_check(email1)