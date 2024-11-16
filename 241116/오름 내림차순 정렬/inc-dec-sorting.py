n = int(input())

nums = list(map(int, input().split()))
nums.sort()
for i in nums:
    print(i,end=" ")
print()
nums.reverse()
for i in nums:
    print(i,end=" ")