from random import randint
n=randint(1,100)
print("n=",n)
k=randint(1,n)
print("k=",k)
a=list(range(n))
b=[]
for i in a:
    if i%k==0:
        b.append(i)

print(b)