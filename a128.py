from random import randint
k=randint(2,5)
print("k=",k)
a = [5,6,6, 4, 4, 44, 6, 6, 7, 0, 0, 0, 0, 0, 1, 1, 1]
b=[]
count=0
l=0
for i in a:
    if a[l]!=a[l-1]:
        count+=1
    l+=1
        if count<k:
            a.pop(a[l])
print(a)




