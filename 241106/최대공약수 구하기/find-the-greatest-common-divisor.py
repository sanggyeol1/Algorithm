def commonDiv(n, m):
    listn = []
    listm = []
    for i in range(1, n+1):
        if n % i == 0:
            listn.append(i)

    for i in range(1, m+1):
        if m % i == 0 and i in listn:
            listm.append(i)

    print(max(listm))


n, m  = map(int, input().split())
commonDiv(n, m)