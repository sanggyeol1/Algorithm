lista = []

for _ in range(4):
    row = list(map(int, input().split()))
    lista.append(row)


sum = 0
for i in range(1, 5):
    for j in range(i):
        sum+=lista[i-1][j]

print(sum)