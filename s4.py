from random import randint
n=randint(1,26)
a=list(range(n))
s=""
for i in a:
    s+=chr(i+65)
print(s)
