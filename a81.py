from random import randint

n=randint(1,100)
a=list(range(n))
print(a)
l=0
k=randint(1,n)
for i in range(len(a)-k):

    a[l]=a[l+k]
    l+=1
a=a[:-k]



print(a)
