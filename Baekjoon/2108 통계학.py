import sys
input = sys.stdin.readline
t = int(input())

lista = []
for _ in range(t):
    lista.append(int(input()))

#산술평균
print(round(sum(lista)/len(lista))) #//은 내림 round()는 반올림

lista.sort()
#중앙값
middle = lista[len(lista)//2]
print(middle)

#최빈값
count = {}
for i in lista:
    if i in count:
        count[i] +=1
    else:
        count[i] = 1

max_value = max(count.values()) #count딕셔너리 값 중 최댓값 구하기
max_list = []
for i in count:
    if count[i] == max_value:
        max_list.append(i)

if len(max_list) > 1: #최빈값이 여러개면
    print(max_list[1]) #정렬은 앞에서 이미 했음
else:
    print(max_list[0])




#범위
total_range = max(lista) - min(lista)
print(total_range)