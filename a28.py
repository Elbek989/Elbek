from random import randint
n=randint(1,100)
print("n=",n)
a=list(range(n))
l=0
for i in a:
    if a[l]<a[2]:
        s=a[l]
        l+=2
print(s)