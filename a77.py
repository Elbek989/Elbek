from random import randint

n=randint(1,100)
a=list(range(n))
print(a)


l=0
for i in a:
    if a[l]>a[l+1]<a[l+2]:

        a.append((a[l+1])**2)
        a.remove(a[l + 1])
        l+=1
print(a)

