from random import randint
n=randint(1,100)
print("n=",n)
a=list(range(n))
l=0
if a[l]%2==1 and a[l+1]%2==0 or a[l]%2==0 and a[l+1]%2==1:
    print(0)
    l+=1
else:
    print(a[l])