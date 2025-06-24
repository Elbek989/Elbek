from random import randint
n=randint(1,100)
print("n=",n)
a=list(range(n))
l=0
s=0
for i in range(n-1):
    if a[l]>a[l+1]:
        s+=1
        l+=1
    else:
        l+=1
print(s)