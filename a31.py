from random import randint
n=randint(1,100)
print("n=",n)
a=list(range(n))
l=0
b=[]
for i in range(n-1):
    if a[l+1]>a[l]:
        c=a[l+1]
        b.append(c)
        l+=1
b.reverse()
print(b)