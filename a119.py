

a = [5,6,6, 4, 4, 44, 6, 6, 7, 0, 0, 0, 0, 0, 1, 1, 1]
b=[]
count=0
b.append(a[0])
b.append(a[0])
for i in range(1,len(a)):
    b.append(a[i])
    if a[i]!=a[i-1]:
        b.append(a[i])

print(b)


