from random import randint
k=randint(2,5)
print("k=",k)
a = [5,6,6, 4, 4, 44, 6, 6, 7, 0, 0, 0, 0, 0, 1, 1, 1]
b=[]
count=0
for i in range(len(a)-1):
    if a[i]!=a[i+1]:
        count+=1
        if count==k:
            a.pop(i)
print(a)




