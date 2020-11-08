# working with strings

fruit = "mangoes"
# identifying characters by indicies
print(fruit[0])
print(fruit[1])
print(fruit[2])
print(fruit[3])
print(fruit[4])
print(fruit[5])
print(fruit[6]) # string characters are identified by indicies
fruit2 = "oranges"
print((fruit) + (fruit2)) #concatenating strings

# slicing strings
print(fruit[:2]) #slicing from indice 2
print(fruit[1:5]) # slicing from indice 1 to 5
print(fruit[4:]) #slicing from 4 to the end

# more string methods
print("...".join(["one", "two", "three"])) # joins strings together using the specified string in between tucker
print("lowell, boston, waltham, woburn".split(", ")) # splits the string in a list with the argument in between them


#more methods
print("hello world".rjust(15))  # ads spaces to the left and counts 15 characters and
                                       #  the space can be filled with a character
print("hello world".ljust(15) + "today") # adds space to the left

print("hello world".rjust(15, "*"))
print("hello world".ljust(15, "*") + "today")
print("hello world".center(15, "*")) #centres the string

print("   hello world".strip()) # removes all spaces in both sides in the string
print("22222hello world22222".strip("2")) # finds and removes spaces or characters in both sides of the string
print("2222222hello world2222".rstrip("2"))
print("22222hello world222222".lstrip("2"))


print("hello world".replace("hello", "sex")) # finds and replaces strings
print(len("hello world")) # returns the length og the string including spaces









