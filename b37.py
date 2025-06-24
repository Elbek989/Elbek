with open("file1", "r") as f:
    s = f.readlines()


a = [int(item) for line in s for item in line.split()]

for i in a:
    a.append(i)

print(a)