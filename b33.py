with open("file.txt", "r") as f:
    s = f.readlines()


a = [int(item) for line in s for item in line.split()]
l=0
for i in a:
    if len(a)>10:
        a.remove(a[l])
        l+=2

print(a)