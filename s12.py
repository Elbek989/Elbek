from random import randint
n=randint(1,10)
s="aedjfnv"
d=""
for i in s:
    d+=i
    for g in range(n):
        d+="*"
print(d)