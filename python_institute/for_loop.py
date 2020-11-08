

x = [1, 2, 3]
for i in x:
    print(i *i)


for j in range(1, 10, 2):
    if j % 2 == 1:
        print(j)

# prime numbers
for i in range(2, 10):
     if i > 1:
          for j in range(2, i):
               if  i % j == 0:
                    break
          else:
               print(i)
