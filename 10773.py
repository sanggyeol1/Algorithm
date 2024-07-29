T = int(input())

lista = []

for _ in range(T):
    n = int(input())
    if n != 0: 
        lista.append(n)
    elif n == 0:
        lista.pop()

print(sum(lista))


