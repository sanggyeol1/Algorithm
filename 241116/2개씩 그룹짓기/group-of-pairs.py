#숫자들을 받고 정렬, 그 후 k, n-k번째 수들을 더해서 array를 만듬, 최댓값을 출력

n = int(input())
lista = list(map(int, input().split()))
lista.sort()
maxlist = []
for i in range(len(lista)//2):
    groupsum = lista[i] + lista[len(lista)-i-1]
    maxlist.append(groupsum)

print(max(maxlist))
