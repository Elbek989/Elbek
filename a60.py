from random import randint
n=randint(1,100)
print("n=",n)
a=list(range(n))
b=[]
l=0
for i in range(n):
    s=((a[l]+a[-1])/2)*n
    b.append(s)
    l+=1
print(b)
print(len(b))