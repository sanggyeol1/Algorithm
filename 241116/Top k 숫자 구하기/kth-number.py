n, k = map(int, input().split())

lista = list(map(int, input().split()))
lista.sort()

print(lista[k-1])