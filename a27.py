from random import randint
n=randint(1,100)
print("n=",n)
a=list(range(n))
l=0
if a[l]/(-1)==(-a[l]) and a[l+1]/(-1)==(a[l+1]) or a[l]/(-1)==(a[l]) and a[l+1]/(-1)==(-a[l+1]):
    print(0)
    l+=1
else:
    print(a[l])