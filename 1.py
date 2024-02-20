from itertools import product

n =  0
for s in product('XYZ', 'ABCD', 'ABCD', 'ABCD'):
    n +=  1
print(n)
