from random import randint
n=randint(1,100)
print("n=",n)
a=list(range(n))
b=[]
l=0
for i in range(n):
    if a[l]%3==0:
        b.append(a[l])
        l+=1
    else:
        l+=1
print(b)
print(len(b))