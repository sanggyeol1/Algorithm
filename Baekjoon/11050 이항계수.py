n, k = map(int, input().split())

upper = 1
for _ in range(k):
    upper *= n
    n-=1

lower = 1
for i in range(1, k+1):
    lower *= i

print(upper // lower)


