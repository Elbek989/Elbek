from random import randint
n=randint(1,100)
print("n=",n)
a=list(range(n))
for i in a:
    if i%2==1:
        print(i)