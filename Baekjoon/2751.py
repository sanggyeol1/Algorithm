import sys

T = int(sys.stdin.readline())

lista = []

for _ in range(T):
    n = int(sys.stdin.readline())
    lista.append(n)

lista.sort()
for i in lista:
    print(i)