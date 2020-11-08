city = ["masaka", "jinja", "mubende"]
for check_city in city:

     print("it exists")



     break

# using the range function one argument or input
number = range(10)
for odd in number:
    odd_num = odd%2
    if odd_num == 1:
        print(odd)

 # range with 2 inputs
ranges = range(10, 15)
for num_range in ranges:
    print(num_range)


# range with inputs
three_arg = range(2, 10, 2) # increases the first by the last till the second
for three in three_arg:
    print(three)

# prime numbers
for i in range(2, 10):
     if i > 1:
          for j in range(2, i):
               if i % j == o:
                    break
          else:
               print(i)


# first n prime numbers
def prime(n):
    count = 0
    i = 1
    n_prime = []
    while count < n:
        if i >= 1:
            i += 1
            for j in range(2, i):
                if i%j == 0:
                    break
            else:
                count += 1
                n_prime.append(i)
    print(n_prime)
                
prime(10)
