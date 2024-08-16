n, k = map(int, input().split())

cash = []
for _ in range(n):
    cash.append(int(input()))

count = 0
for i in cash[::-1]:
    if k >= i:
        count += k // i
        k %= i
    else:
        continue
    
print(count)