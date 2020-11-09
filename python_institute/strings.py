# sting on double line

d = ''' the name of
jesus '''

print(d)

# concatenation
print('tucker' + '   ' + 'serwadda')

# reprecation
print(('a' + '  ')*3)

# using the += and *= operation
# + is used to join strings together
a = 'dana'
a += 'sasira'
print(a)
# * is used to ruplicate the string a given number of times 
b = a *3
print(b)

# finding the character's AScII / Unicode code point value

print(ord('a'))

# given the unicode code point value to find the character

print(chr(97))

# string indexing
a = 'serwadda'
for i in range(len(a)):
    print(a[i], end = ',')

print('\n', a[ :4])

# string slicing
string = "abcdefg" 
slice1 = string[::2] # write the first character then jump one and write the next
print(slice1)
slice2 = string[2::] # write from index 2 to the end
print(slice2)
slice3 = string[:2]
print(slice3) # write from index 0 to index 1
slice4 = string[2:] # smae as 2::
print(slice4)

# in and not in operators
name = "serwadda"
characterIn = "r" in name # returns true if character exists otherwise false
print(characterIn)

characterNotIn = "z" not in name
print(characterNotIn) # returns true if character does not exit otherwise false

# * note*
# the del function is used to delet a string as a whole

# minimum and maximum character in the string
firstName = "tucker"
print(min(firstName)) # minimum element
print(max(firstName)) # maximum element

# index method
# finds the index of the first specified element 
lastName = "serwadda"
print(lastName.index("w"))

# List function
# changes a string into a list
carType = "toyota"
carTypeList = list(carType)
print(carTypeList)

# count() method
# counts the number of occerrences of element in a string
word = "maximum"
print(word.count("m"))

# capitalize method
# captalizes the element at index 0 of the string if its a letter
vission = "vission"
capVission = vission.capitalize()
print(capVission)
# center method
# centers the word in a given number of characters
centerVission = vission.center(11, "*")
print(centerVission)
# endswith method
# checks if the string ends with
vissionEnds = vission.endswith("sion") # returns true or false
print(vissionEnds)
# find method
# looks for the substring and returns the index of the first occurrence of the substring
findVis = vission.find("vis")
print(findVis)
findSion = vission.find("sion", 2) # 2 specifies the index from which the search should start
print(findSion)
# find can also be used to find all the occurrences of the substring
text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""
textfind = text.find("the")
while text.find != -1:
    print(textfind)
    textfind = text.find("the", textfind +1)
    if textfind == -1:
        break

# when find is used with 3 arguments, the third argument points to the first index which wont be taken into consideration 
words = "serwaddaserwadda"
wordsfind = words.find("wa", 2, 3)
print(wordsfind)

# the isalnum() method
# checks wether the string contains only digits or alphabetical characters
myfriend = "allan"
print(myfriend.isalnum()) # returns true  
myfriend2 = "kigozi_allan"
print(myfriend2.isalnum()) # returns false

# isalpha() method
# checks whether they are characters only
alpha = "allan2"
print(alpha.isalpha()) # returns false

# isdigit() method
# checks whether they are digits only
number = "13568"
print(number.isdigit())

# other methods
# islower()- lowercase letters
# isupper() - upper-case letter
# isspace() - identifies while space only without characters
names = "serwadda"
print(names.isspace())
print("mooo mooo mooo".isspace())
print(' \n '.isspace())

# the join method
# joins a string with a list of strings
# the string becomes the seperator
joinstring = ","
joinlist = ["tucker", "serwadda"]
stringListjoined = joinstring.join(joinlist)
print(stringListjoined)
# example 2 of join
print("good".join(["omicron", "pi", "rho"]))

# lower() method
# converts upper-case to lower case
print("TuCKer".lower())
# upper() method
# converts lower to upper case
print("serwadda".upper())
# lstrip()- removes leading white space
print("   tucker serwadda".lstrip())
# can also be used to remove leading characters
print("www.cisco.com".lstrip("w."))

# replace method()
# The two-parameter replace() method returns a copy of the original string in which all occurrences 
# of the first argument have been replaced by the second argument.
wording = """ the same place that the girls used to go is 
same place that am going"""
print(wording.replace(" ", ""))
replaceTheWithThat = wording.replace("the", "that")
print(replaceTheWithThat)
print("Apple juice".replace("juice", ""))
print("serwadda tucker".replace(" ", "")) # removes all white spaces in the string

# when the third argument is used, it i dentifies the number of replacements
replaceTheWithThat = wording.replace("the", "that", 1)
print(replaceTheWithThat)

# rfind() - works a find but it starts the search from the end of the string
# it can also take on 2 , 3 arguments
print("sedenne".rfind("e"))
# rstrip() - removes white space at the end and string at the end.
print("tucker serwadda".rstrip("da"))
print("cisco.com".rstrip(".com"))

# split() method - splits the string and builds a list of all detected substrings.The method assumes that the substrings are delimited by whitespaces - the spaces don't take part in the 
# operation, and aren't copied into the resulting list.
print("tucker serwadda".split())

# startswith()- checks if a given string starts with
# strip()- it makes a new string lacking all the leading and trailing whitespaces.
print("[" + " serwadda ".strip() + "]")

# swapcase() method 
# The swapcase() method makes a new string by swapping the case of all letters within the source string: 
# lower-case characters become upper-case, and vice versa.
print("SeRwaDDa".swapcase())

# title()method
#The title() method performs a somewhat similar function - it changes every word's 
#first letter to upper-case, turning all other ones to lower-case.