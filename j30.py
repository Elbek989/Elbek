with open("file.txt", "r") as f:
    s = f.readlines()


a = [int(item) for line in s for item in line.split()]
g=[]
for i in a:
    if len(g)<len(a)//2:
        g.append(i)
print(g)

