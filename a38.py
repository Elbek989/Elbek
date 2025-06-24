from random import randint
n=randint(1,100)
print("n=",n)
a=list(range(n))
b=[]
l=0
x=0
y=0
for i in range(n-2):
    if a[l]<=a[l+1]>a[l+2]:
        x+=1
    elif a[l]>=a[l+1]<a[l+2]:
        y+=1


