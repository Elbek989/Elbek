f=open("file","r")
s=f.readlines()
f.close()
a=[list(map(int, item.split())) for item in s]
a=[item for sublist in a for item in sublist]
lokal_max=None
for i in range(1, len(a)-1):
    if a[i+1]<a[i]>a[i-1]:
        print(a[i])
        lokal_max=a[i]
        break
print(lokal_max)
