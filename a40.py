from random import randint
n=randint(1,100)
print("n=",n)
a=list(range(n))
R=randint(1,n)
print("R=",R)
l=0
s=n-1
for i in range(n-1):
    if a[l]<R :
        l+=1
    if a[s]>R:
        s-=1
if a[s]-R>R-a[l]:
    print(a[l])

else:
    print(a[s])




