f = open("sonlar.txt", "w")
f.write("1 4 7 8 3\n")
f.write("2 9 10 5\n")
f.write("6 11 14 15\n")
f.close()

f = open("sonlar.txt", "r")
qatorlar = f.readlines()
f.close()

juft_qatorlar = []
toq_qatorlar = []

for qator in qatorlar:
    sonlar = list(map(int, qator.strip().split()))
    juftlar = [str(son) for son in sonlar if son % 2 == 0]
    toqlar = [str(son) for son in sonlar if son % 2 == 1]
    juft_qatorlar.append(" ".join(juftlar))
    toq_qatorlar.append(" ".join(toqlar))

f = open("juft.txt", "w")
for qator in juft_qatorlar:
    f.write(qator + "\n")
f.close()

f = open("toq.txt", "w")
for qator in toq_qatorlar:
    f.write(qator + "\n")
f.close()