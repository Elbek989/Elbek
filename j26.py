f=open("file","r")
s=f.readlines()
f.close()

a=[list(map(int, item.split())) for item in s]
a=[item for sublist in a for item in sublist]
print(a)
k=a[0]
l=a[0]
p=[]
d=0
for i in range(1, len(a)-1):
    if k<a[i]:
       k=a[i]

    if l>a[i]:
        l=a[i]
for o in range(1,len()-1):

print(a)

