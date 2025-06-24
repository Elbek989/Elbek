s="adfefefW234"
y=64
d=""
for i in s:

    if ord(i)>64 and ord(i)<91:
        i=chr(ord(i)+32)
    d+=i
print(d)