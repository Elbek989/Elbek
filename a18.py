from random import randint
n=randint(1,100)
print("n=",n)
a=list(range(n))
t=n-1
s=a[t]
a.reverse()
for i in a:
    if s>i:
        print(i)
        break
    else:
        print(0)
