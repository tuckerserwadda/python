
# capturing student marks
math_class = {}
count = 0
n = int(input(" enter the total number of students:"))
while count < n:
    name = input("enter student name:")
    score = int(input("enter score:"))
    math_class[name] = score
    count += 1
    if count == n:
        break

print(math_class )
total = 0
for i in math_class.values():
    total += i
print(f'{total / n} is the average score')

math_tup = tuple(math_class.values())
print(math_tup)

math_copy = math_class.copy()
print(math_copy)
