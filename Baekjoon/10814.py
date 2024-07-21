T = int(input())

lista = []

for _ in range(T):
    age, name = input().split()
    age = int(age)
    lista.append([age, name])

#람다식으로 정렬 기준 정함
lista.sort(key = lambda x: x[0])

for i in lista:
    print(i[0], i[1])

