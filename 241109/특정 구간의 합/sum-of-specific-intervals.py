n, m = map(int, input().split())

lista = list(map(int, input().split()))

for _ in range(m):
    sum = 0
    start, end = map(int, input().split())
    for i in range(start-1, end):
        sum+=lista[i]

    print(sum)