def func(a, b):
    #a가 클때
    if a > b:
        a*=2
        b+=10

    elif a < b:
        b*=2
        a+=10
    return [a, b]


a, b = map(int, input().split())

for i in func(a, b):
    print(i, end=" ")