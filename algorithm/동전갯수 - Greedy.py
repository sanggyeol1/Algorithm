#그리디 알고리즘 동전문제

price = 4321

A = price // 500
price %= 500
B = price // 100
price %= 100
C = price // 50
price %= 50
D = price // 10
price %= 10
E = price // 1
price %= 1

print(A, B, C, D)


