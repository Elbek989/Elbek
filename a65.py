from random import randint
n=randint(1,100)
print("n=",n)
a=list(range(n))
k=randint(1,n)
print("k=",k)
b=[]
l=0
for i in range(n-1):
    p=a[l]+a[k]
    b.append(p)
    l+=1
print(b)

    