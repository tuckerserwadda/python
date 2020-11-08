# declare and create a list
example_list1 = ["masaka", "mukono", "jinja", "kampala"] # list of strings
example_list2 = [1, 2, 3, 4, 5] # list of integers
examples_list3 = ["wakiso", 5, 3.6, "bukoto"] # list of floats, integers and string
example_list4 = [[2, 5, 7, "sex"], ["joan", "dana", "nouvel"]] # list of lists

#list methods
print(list("tucker")) #returns a list of characters in the string
check_item = [1, 4, 6, 0]
print(4 in check_item)  # returns true if the item is in the list
print(10 not in check_item) #returns true if the item does not exist in the list

# accessing using index numbers
print(example_list1[1])
print(example_list2[3])
print(example_list4[0][3]) # accessing an item in a list of lists [0]. list index [3] item index
print(examples_list3[-1]) # accessing using a negative index i.e starts from the end of the list

# using items accessed in expressions
print(example_list1[0] + ", " + examples_list3[3]) # concatenation of lists
print(str(example_list2[2]) + example_list4[1][1]) # concatenated items must be of the same data type
print(example_list1[:2]) #sclicing a list from 0 to index 2 (not included)
print(example_list1[2:]) #sclicing a list from index 2(included) to the end of the list
print(example_list1[0:2]) #sclicing a list between index 0 (included) to index 2

# chnaging value of an item in a list
example_list1[3] = "seguku"
print(example_list1)
example_list2[0:3] = [6, 8, 9] # changing values of a sclice
print(example_list2)

# del and remove methods
del example_list1[2]
print(example_list2)
examples_list3.remove("bukoto")
print(examples_list3)

# append & insert methods
examples_list3.append("mukono")
print(examples_list3)
examples_list3.insert(1, "kampala")
print(examples_list3)

# sort from small to big or arrange in aphabetical order

num = [2, 7.5, 6, 4.57, 23]
num.sort() # sort from the smallest to bigest
print(num)
num.reverse()
print(num)
names = ["piggs", "pigeon", "piglet"]
names.sort()
print(names)
names.reverse()  # returns from the  bigest to the smallest
print(names)
print(names.index("piggs")) # returns the index number of the item
popped_item = names.pop(1) # getts an item of index 1 and a signs it to popped_item variable
print(popped_item)






















