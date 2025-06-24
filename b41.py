with open("file1", "r") as f:
    s = f.readlines()


a = [int(line) for line in s ]

for i in a:
    if i>0:
        a.remove(i)
        i=0
        a.append(i)



print(a)