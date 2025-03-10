import re
# findall - returns all matches
# search = Returns the match object if there is a match
#  - If there is more than one match, only the first occurrence of the match will be returned:
# split - returns a list where the string has been split at eash mach
# sub - replaces one or many matches with a string
# match - Match objects contain information about a particular regex match — the position in the string where the match was found, the contents of any capture groups for the match, and so on.

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt, re.IGNORECASE) #IGNORECASE
if x:
  print("YES! We have a match!")
else:
  print("No match")


str = ['catihavea', 'mycatisacatbigcat', 'mycatgetangrycatacat']
pattern = ['ttt$','cats$', 'cat$','at$']
lst=[]
for string in str:
    for pat in pattern:
        match = re.search(pat, string)
        if match:
            print(match.group()) 
            lst.append(match.group())
            break
        else:
            lst.append("None")


# Metacharacters:

# [] - A set of characters

#Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-m]", txt)
print(x)


# \ - Signals a special sequence (can also be used to escape special characters)

txt = "That will be 1000 Rupees"
# #Find all digit characters:
x = re.findall("\d", txt)
print(x)


# . - Any character (except newline character)

txt = "hello heaao heooo Hie Horse he__o"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x = re.findall("he..o", txt)
print(x)

txt = "hie hea heooo hoo hie ho huu hi h"
#Search for a sequence that starts with "h", followed by two (any) characters even whitespaces:
x = re.findall("h..", txt)
print(x)


# ^ Starts with

txt = "hello planet"
#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")


# $ Ends with

txt = "hello planet"
#Check if the string ends with 'hello':

x = re.findall("hello$", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")


# * Zero or more occurances

txt = "hie hea heooo hoo hie ho huu hi h"
x = re.findall("h.*", txt)
print(x)
x = re.findall("he.*", txt)
print(x)

# + One or more occurences

txt = "hie heeea heooo hoo heeii hehe ehe eh heuu hi h"
x = re.findall("he.+", txt)
print(x)
# he+ matches a string where h is followed by one or more es.
# he.+ matches any string that starts with he and is followed by at least one character of any kind (except newlines).


# ? Zero or one occurrences

# Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "e":
txt = "hie heeea heooo hoo heeii hehe ehe eh heuu hi h"
x = re.findall("he.?e", txt)
print(x)


# {} Exactly the specified number of occurrences

txt = "hello planet"
#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
x = re.findall("he.{2}o", txt)
print(x)

x = re.findall("he.{1}o", txt)
print(x)


# | Either or

txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("falls|stays", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# Special Sequences
# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

# \A - Returns a match if the specified characters are at the beginning of the string


# \b - Returns a match where the specified characters are at the beginning or at the end of a word

txt = "The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"\bain", txt)
print(x)

#Check if "ain" is present at the end of a WORD:
x = re.findall(r"ain\b", txt)
print(x)


# \B - Returns a match where the specified characters are present but not at the beginning or at the end of a word

#Check if "ain" is present, but NOT at the end of a word:
x = re.findall(r"ain\B", txt)
print(x)

#Check if "ain" is present, but NOT at the end of a word:
x = re.findall(r"ain\B", txt)
print(x)


# \d - Returns a match if a string contains digits

txt = "Please lend me 1,00,00,000 Rs"
x = re.findall("\d", txt)
print(x)

print(re.search("\d", txt))


# \D - Returns a match if a string contains digits
txt = "97219837982163021389218"
x = re.findall("\D", txt)
print(x)

txt = "The rain in Spain"
print(re.findall("\D", txt))


# \s - Returns a match where the string contains a white space character

txt = "The rain in Spain"
print(re.search("\s", txt))


# \S - Returns a match where the string DOES NOT contain a white space character

txt = "HiMyNameIsPriyansh"
print(re.findall("\s", txt))

# \w - Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

txt = "The rain in Spain"
x = re.findall("\w", txt)
print(x)

# \W - Returns a match where the string DOES NOT contain any word characters


# \Z - Returns a match if the specified characters are at the end of the string

x = re.findall("spain\Z", txt, re.IGNORECASE)
print(x)


# Sets

# [arn]	Returns a match where one of the specified characters (a, r, or n) is present	
# [a-n]	Returns a match for any lower case character, alphabetically between a and n	
# [^arn]	Returns a match for any character EXCEPT a, r, and n	
# [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
# [0-9]	Returns a match for any digit between 0 and 9	
# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
# [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
# [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string	


# split()

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
print(re.split("\s", txt, 1))


# sub()

import re

x = re.sub("\s", "9", txt)
print(x)
print(re.sub("\s", "9", txt, 2))


# Match object
# A Match Object is an object containing information about the search and the result.
# The Match object has properties and methods used to retrieve information about the search, and the result:
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

x = re.search(r"\bS\w+", txt)
print(x.string)

x = re.search(r"\bS\w+", txt)
print(x.group())



