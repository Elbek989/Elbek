from random import randint
n=randint(1,100)
print("n=",n)
a=randint(1,10)
d=randint(1,10)
print("d=",d)
b=[]
i=0
for g in range(2,n+1):
    if i<=n:
        b.append(a)
        a*=d
        i+=1
print(b)
