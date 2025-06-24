from random import randint
n=randint(1,100)
print("n=",n)
a=list(range(n))
R=randint(1,n)
b=list(range(R))
a.append(b)
l=0
for i in range(n-1):
    if a[l]==a[l+1]:
        print(a[l],a[l+1])
    else:
        l+=1




