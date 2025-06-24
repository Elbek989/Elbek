from random import randint
n=randint(1,100)
print("n=",n)
a=list(range(n))
d=randint(1,n)
b=list(range(d))
for i in range(n-1):
    if a[i]<5:
        b[i]=a[i]*2
        i+=1
    else:
        b[i]=a[i]/2
        i+=1
print(b)