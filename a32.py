from random import randint
n=randint(1,100)
print("n=",n)
a=list(range(n))
l=0
b=[]
for i in range(n-2):
    if a[l]>a[l+1]<a[l+2]  :
        b.append(a[l+1])
        l+=1
print(b)

