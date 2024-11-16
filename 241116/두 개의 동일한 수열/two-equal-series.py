n = int(input())

lista = list(map(int, input().split()))
listb = list(map(int, input().split()))

lista.sort()
listb.sort()

if lista == listb:
    print("Yes")
else:
    print("No")