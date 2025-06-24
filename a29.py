from random import randint
n=randint(1,100)
print("n=",n)
a=list(range(n))
l=1
s=1
for i in range(1,n):
    if a[l]<a[s]:
        s=l
        l+=2
print(a[l])