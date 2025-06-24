from random import randint
n=randint(1,100)
print("n=",n)
a=randint(1,10)
b=randint(1,10)
d=[a,b]
h=0
for i in range(1,n):
    if h<n:
        m=sum(d)
        d.append(m)
        h+=1
print(d)
