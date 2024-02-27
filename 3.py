def func(b):
    count = 0
    for i in range (1, b, 2):
      if b % i == 0 and i % 2 == 1:
        count+=1
    return count

l = 45000000
r = 50000000
res = []

for i in range (l, r+1):
  if func(i) == 5:
    print(i)


