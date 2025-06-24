a=[4,2,3,6,8,10]
l=a[0]
g=a[1:]
u=0
while u<len(g) and g[u]<l:
    u+=1
a=g[:u]+[l]+g[u:]
print(a)
