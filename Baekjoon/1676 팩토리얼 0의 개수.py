def factorial(n):
    value = 1
    for i in range(1, n+1):
        value *= i
    return value

n = int(input())

num = str(factorial(n))
zero = 0

for i in num[::-1]:
    if i == "0":
        zero+=1
    else:
        break

print(zero)