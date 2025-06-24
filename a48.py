from random import randint
n=randint(1,100)
print("n=",n)
a=list(range(n))
R=randint(1,n)
print("R=",R)
l=False
for i in range(n):
    for j in range(i+1,n):
        if a[i]==a[j]:
            print(f"{a[i]} {a[j]}")
            l=True
            break
            if l:
                break
else:
    print("bunaqa elementlae yoq")




