n,m = map(int, input().split())

lista = []
for i in range(n):
    listb = list(map(int, input().split()))
    lista.append(listb)

listc = []
for i in range(n):
    listd = list(map(int, input().split()))
    listc.append(listd)

for i in range(n):
    for j in range(m):
        lista[i][j] += listc[i][j]

    for k in lista[i]:
        print(k, end=" ")

    print("")






