# if statement

veg = raw_input("enter name of vegetable:  ")
veg2 = raw_input("enter second vegitable:  ")
if veg == "mango":
    print("deliciouse")
    if veg == "mango" and veg2 == "orange":
        print("sweet")
    else:
        print("its not a good combination")

        # nested if and else statements
GPA = 3.7
student = raw_input("enter student gpa:  ")
instute = raw_input("is student approved?: ")
aproved = "yes"

if student >= GPA:
  if instute == aproved:
     print("qualifies for loan")
  else:
          print("not qualified")
else:
    print("not qualified")

    #elif function in python 3










