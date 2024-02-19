n = 0
for x in 'XYZ':
    for y in 'ABCD':
        for z in 'ABCD':
            for w in 'ABCD':
                s = x + y + z + w
                n+=1
print(n)