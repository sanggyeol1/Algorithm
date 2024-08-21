#최대공약수 : 24 와 18일때
# 24 % 18 은 6
# 18 % 6 은 0 --> 최대공약수는 6

#최소공배수 : 24 * 18 / 최대공약수

nums = list(map(int, input().split()))

a = max(nums)
b = min(nums)

maxDiv = a*b

while True:
    extra = a % b
    if extra == 0:
        print(b)
        break

    a = b
    b = extra


print(maxDiv//b)


