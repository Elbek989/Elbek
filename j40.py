with open("file.txt", "r") as f:
    s = f.readlines()


a = [int(item) for line in s for item in line.split()]
b=[]
print(a)
for i in range(1,len(a)):
    if i%2==0:
        a[i]=0
    b.append(a[i])

print(a)