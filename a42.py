from random import randint
n=randint(1,100)
print("n=",n)
a=list(range(n))
R=randint(1,n)
print("R=",R)
l=0
s=1
for i in range(n-1):
    if a[l]+a[s]<R :
        l+=1
        s+=1
if a[l]+a[s]-R<R-a[l-1]-a[s-1]:
    print(a[l],"va",a[s])
else:
    print(a[l-1],"va",a[s-1])



