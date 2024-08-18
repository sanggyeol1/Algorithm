import sys

n = int(sys.stdin.readline())
lista = [0]*10001

for _ in range(n):
    k = int(sys.stdin.readline())
    lista[k]+=1

for idx, k in enumerate(lista):
    if k!=0:
        for _ in range(k):
            print(idx)