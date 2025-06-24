from random import randint
n=randint(1,100)
print("n=",n)
f1=1
f2=2
a=[f1,f2]
i=0
for g in range(1,n+1):
    if i<n:
        f3=f1+f2
        a.append(f3)
        f1=f2
        f2=f3
print(a)