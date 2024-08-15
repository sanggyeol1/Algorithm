import sys
t = int(sys.stdin.readline())

lista = []
for _ in range(t):
    dot = list(map(int, sys.stdin.readline().split()))
    lista.append(dot)

lista.sort()
for i in lista:
    print(i[0], i[1])

