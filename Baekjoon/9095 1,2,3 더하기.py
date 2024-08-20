t = int(input())

lista = { 1: 1, 2 : 2, 3 : 4 }

for _ in range(t):
    num = int(input())
    for i in range(4, num+1):
        lista[i] = lista[i-1] + lista[i-2] + lista[i-3]
    print(lista[num])
