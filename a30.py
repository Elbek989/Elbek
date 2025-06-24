from random import randint
n=randint(1,100)
print("n=",n)
a=list(range(n))
l=0
b=[]
for i in a:
    if a[l]>a[l+1] :
        b.append(a[l])
        l+=1
print(b)