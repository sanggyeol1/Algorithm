n, k = map(int, input().split())

#테이블 [1, 2, 3, 4, 5, 6, 7]
table = []
for i in range(1, n+1):
    table.append(i)


#순열 []
lista = []
index = k-1
while True:
    lista.append(table.pop(index))
    if len(table) == 0:
        break
    index = (index + k - 1)%len(table)



print("<", end="")

for i in range(len(lista)):
    if i == len(lista) - 1:
        print(lista[i], end="")
    else:
        print(lista[i], end=", ")

print(">", end="")
