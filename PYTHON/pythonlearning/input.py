name = str(raw_input("my name: "))  # type: str
print("you entered" +name)
print(type(name))

# converting input into integer
age = int(raw_input("enter your current age: "))
print("age entered is : "+ str(age)) #convert to string for concatenation
print(type(age))
# changing the case for the in put

name = name.lower() # changing to lower case
print(name)

name = name.upper() # changing to upper case
print(name)

name = name.title() # converting the first character to upper case
print(name)

# other string methods
print(name.isalpha())   # returns true if all lettere
print(name.isalnum())   # returns true if letters and numbers
print(name.isdigit())   # returns true if all numbers
print(name.isspace())   # returns true if string contains space
print(name.istitle())   # returns true if the first character is capes
print(name.isupper())   # returns true if the string is upper case
print(name.islower())   # returns true if the string is lower case
print(name.startswith("T"))  # returns true if the string starts with the argument
print(name.endswith("r"))    # returns true if the string end with the argument







