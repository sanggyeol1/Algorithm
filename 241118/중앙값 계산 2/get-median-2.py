n = int(input())

nums = list(map(int, input().split()))


lista = []
for i in range(len(nums)):
    lista.append(nums[i])
    #홀수번째면
    if i % 2 == 0:
        lista.sort()
        print(lista[i//2], end=" ")


