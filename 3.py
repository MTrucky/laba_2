def f1(x):
     while x%2==0:
          x=x//2
     if (x**0.25) == int(x**0.25):return True
     else:return False
def f(x):
     k=2
     deliteli=set()
     if x%2!=0:deliteli.add(x)
     deliteli.add(1)
     while k*k<=x:
          if x%k==0:
               if k%2!=0:deliteli.add(k)
               if x//k<x:
                    if (x//k)%2!=0:deliteli.add(x//k)
          k=k+1
     return sorted(deliteli)
start=45000000
end=50000000
numbers=[int(x) for x in range(start,end+1) if f1(x)==True]
for i in numbers:
     if len(f(i))==5:
          print(i)