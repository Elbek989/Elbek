from random import randint

n=randint(4,100)
a=list(range(n))
print(a)
k=randint(1,4)

n = len(a)
k = k % n

for _ in range(k):
    last = a[-1]
    for i in range(n - 1, 0, -1):
        a[i] = a[i - 1]
    a[0] = last

print(a)