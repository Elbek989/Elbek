from random import randint

n = randint(1, 100)
print("n=", n)
a = list(range(n))


b = []
c=1
l=0
for i in range(0, n - 1, 2):
    p = a[i]
    a[i] = a[i + 1]
    b.append(a[i])
    a[i + 1] = p
    b.append(a[i + 1])
print(b)