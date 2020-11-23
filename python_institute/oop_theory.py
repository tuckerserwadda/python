# the the using oop.
# define the the class stack
class stack:
# define the instructor function - used to construct a new object
    def __init__(self): # __init__ is always the instructor name followed by parameters
# add a property
        self.__stackList = [] # accessing the property(stackList is the property name)
        # the two underscores before stackList makes the property private. it can only be accessed in that class.
        # it is called implemeting the encapsulation concept
# add methods(functions). that is class activities
    # the push method to append values to the stackList
    def push(self, val):
        self.__stackList.append(val)
    # the pop method to remove the last list element
    def pop(self):
        val = self.__stackList[-1] # assign the last element to variable val
        del self.__stackList[-1] # delete the last element of the stack list
        return val # returns the last element of the stack after method performed
# create objects from the stack class
stackObject1 = stack()
stackObject2 = stack()
# use the methods for implementation
stackObject1.push(3)
stackObject1.push(4)
stackObject2.push(stackObject1.pop())
print(stackObject2.pop())
# add a new class(subclass) to handle the stacks
# the new class should evaluate the sum of all elements in the stack 
# define the new sub class pointing to the class which will be used as the supperclass
class addingStack(stack):
    def __init__(self): # instruct function
        stack.__init__(self) # call the stack class
        self.__sum = 0 # add the sum property 
