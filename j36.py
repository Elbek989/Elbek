with open("file.txt", "r") as f:
    s = f.readlines()


a = [int(item) for line in s for item in line.split()]
b=len(a)*2
for i in a:
    if len(a)<b:
        a.append(i)
print(a)