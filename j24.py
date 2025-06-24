with open("file.tf", "r") as f:
    s = f.readlines()

a = [list(map(float, x.split())) for x in s]
a = [i for j in a for i in j]

r = []
c = 1

for i in range(1, len(a)):
    if a[i] < a[i-1]:
        c += 1
    else:
        if c > 1:
            r.append(c)
        c = 1

if c > 1:
    r.append(c)

print(r)