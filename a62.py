from random import randint
n=randint(1,100)
print("n=",n)
a=list(range(n))
b=[]
l=0
c=[]
for i in range(n):
    if a[l]>0:
        b.append(a[l])
        l+=1
    else:
        c.append(a[l])
        l+=1
print(b)
print(len(b))
print(c)
print(len(c))