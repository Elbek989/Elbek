f=open("file","r")
s=f.readlines()
f.close()
a=[list(map(int, item.split())) for item in s]
a=[item for sublist in a for item in sublist]
p=[]
print(a)
p.append(a[0])
for i in range(1, len(a)-2):
    a[i+1]=(a[i+2]+a[i])//2
    p.append(a[i+1])
p.append(a[-1])
print(p)