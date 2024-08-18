t = int(input())
lista = []

for _ in range(t):
    point = list(map(int, input().split()))
    lista.append(point)

#y좌표로 정렬 후 동률은 x좌표로 정렬
lista.sort(key = lambda x : (x[1],x[0]))

for lst in lista:
    for i in range(len(lst)):
        if i == 0:
            print(lst[i], end=" ")
        else:
            print(lst[i])