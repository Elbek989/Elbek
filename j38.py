with open("file.txt", "r") as f:
    s = f.readlines()


a = [int(item) for line in s for item in line.split()]
b=[]
print(a)
for i in range(1,len(a)):
    if i%2==1:
        a[i]=a[i]*2
    b.append(a[i])

print(a)