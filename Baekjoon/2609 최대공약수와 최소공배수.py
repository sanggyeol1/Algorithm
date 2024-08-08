#최소공배수 : 24 와 18
# 24 % 18 은 6
# 18 % 6 은 0 --> 최소공배수는 6

#최대공약수 : 24 * 18 / 최소공배수

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


