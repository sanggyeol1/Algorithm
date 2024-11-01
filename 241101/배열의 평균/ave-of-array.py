#이차원 배열 lista
lista = []


for _ in range(2):
    row = list(map(int, input().split()))
    lista.append(row)






print(sum(lista[0])/len(lista[0]), sum(lista[1])/len(lista[1]))

for i in range(4):
    print((lista[0][i] + lista[1][i]) / 2, end=" ")
print("")

sum = 0
for i in range(len(lista)):
    for j in range(len(lista[i])):
        sum+=lista[i][j]

print(sum / (len(lista) * len(lista[0])) )