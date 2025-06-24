from random import randint
n=randint(1,100)
print("n=",n)
a=list(range(n))
if a[2]/a[1]==a[3]/a[2]==a[4]/a[3]:
    print(a[2]/a[1])
else:
    print(0)