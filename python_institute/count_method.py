list1 = [1, 2, 2, 4, 2, 3]
print(list1.count(2))

d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)
