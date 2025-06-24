from random import randint
n=randint(1,100)
print("n=",n)
a=list(range(n))
for i in a:
    if i>a[1] and i<a[-1]:
        print(i)
    else:
        print(0)
