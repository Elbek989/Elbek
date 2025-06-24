from random import randint

n=randint(1,100)
a=list(range(n))
print(a)

l = a[-1]
for i in range(len(a) - 1, 0, -1):
    a[i] = a[i - 1]
a[0] = l
print(a)
