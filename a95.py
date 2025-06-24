from random import randint

n=randint(1,100)
a=list(range(n))
print(a)
for i in a:
    if a[i]==[i+1]:
        a.remove(i)
print(a)
