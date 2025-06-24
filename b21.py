f=open("file","r")
s=f.readlines()
f.close()
a=[list(map(int, item.split())) for item in s]
a=[item for sublist in a for item in sublist]
g=[]
for i in range(1, len(a)-1):
    if a[i+1]<a[i]>a[i-1]:
        print(a[i])
        g.append(a[i])
g=g.sort()
print(g)
