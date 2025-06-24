from random import randint

n=randint(1,100)
a=list(range(n))
print(a)
l=1

for i in range(len(a)-1):

    a[l]=a[l+1]
    l+=1
a.pop(-1)


print(a)
