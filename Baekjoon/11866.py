N, k = map(int, input().split())
index = k-1
lista = []
for i in range(N):
    lista.append(i+1)

listb = []
for i in range(len(lista)):
    listb.append(lista.pop(index))
    if len(lista) == 0:
        break
    index = (index + k - 1)%len(lista)

print("<", end="")
for i in range(len(listb) - 1):
    
    print(listb[i], end=", ")
print(listb[len(listb) - 1], end="")
print(">")

