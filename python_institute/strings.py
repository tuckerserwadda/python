# sting on double line

d = ''' the name of
jesus '''

print(d)

# concatenation
print('tucker' + '   ' + 'serwadda')

# reprecation
print(('a' + '  ')*3)

# using the += and *= operation

a = 'dana'
a += 'sasira'
print(a)

# finding the character's AScII / Unicode code point value

print(ord('a'))

# given the unicode code point value to find the character

print(chr(97))

# string indexing
a = 'serwadda'
for i in range(len(a)):
    print(a[i], end = ',')

print('\n', a[ :4])
