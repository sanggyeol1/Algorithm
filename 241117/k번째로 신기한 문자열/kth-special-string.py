n, k, t = map(str, input().split())
n = int(n)
k = int(k)

lista = []
for _ in range(n):
    word = input()


    if word[:len(t)] == t:
        lista.append(word)

lista.sort()
print(lista[k-1])

