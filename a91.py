from random import randint

n=randint(1,100)
a=list(range(n))
print(a)
k=randint(1,n)
b=[]
for i in range(k):
    b.append(i)
for i in range(k+1,n):
    b.append(i)
print(b)