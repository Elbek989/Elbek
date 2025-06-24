with open("file1", "r") as f:
    s = f.readlines()


a = [int(item) for line in s for item in line.split()]

for i in a:
    if i>4 and i<11:
        a.remove(i)
        i=i*2
        a.append(i)



print(a)