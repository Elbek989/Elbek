with open("file1", "r") as f:
    s = f.readlines()


a = [int(item) for line in s for item in line.split()]

for i in a:
    if len(a)<10:
        a.append(0)
a.reverse()
print(a)