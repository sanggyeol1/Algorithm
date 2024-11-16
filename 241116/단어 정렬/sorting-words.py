n = int(input())

lista = []

for _ in range(n):
    s = input()
    lista.append(s)

lista.sort()

for i in lista:
    print(i)
