from random import randint
n=randint(1,100)
print("n=",n)
a=list(range(n))
b=[]
for i in a:
    if i%2==0:
        b.append(i)
b.reverse()
print(b)