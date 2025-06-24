from random import randint
n=randint(1,100)
print("n=",n)
k=randint(1,n)
l=randint(1,k)
g=k-l
a=list(range(n))
b=0
for d in range(1,n):
    if a[k]>a[l]:
        b+=a[l]
        l+=1
s=b//g
print(s)
