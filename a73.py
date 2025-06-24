from random import randint

n = randint(1, 100)
print("n=", n)
a = list(range(n))
k=randint(1,n)
h=randint(1,k)
b = []
c=a[k-1]
l=
for i in range(k//2):
    b.append(a[c])
    c-=1
for i in range(n//2):
    b.append(a[l])
    l-=1
print(b)