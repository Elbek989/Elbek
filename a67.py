from random import randint

n = randint(1, 100)
print("n=", n)
a = list(range(n))
k = n-1

b = []
l = 0
for i in range(n - 1):
    if i%2==1:
        p = i + a[-1]
        b.append(p)
    
print(b)

