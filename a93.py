from random import randint

n=randint(1,100)
a=list(range(n))
print(a)
for i in a[0::2]:
    a.remove(i)
print(a)
