#중복을 허용하지 않는 set을 활용하여 시간 단축 가능하다.
a, b = map(int, input().split())

unheard = set()
for _ in range(a):
    unheard.add(input())

unseen = set()
for _ in range(b):
    unseen.add(input())


count = 0
result = []
for i in unheard:
    if i in unseen:
        count+=1
        result.append(i)
print(count)
for i in sorted(result):
    print(i)


