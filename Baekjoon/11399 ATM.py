n = int(input())

time = list(map(int, input().split()))
time.sort()
    
total = 0
totalList = []

for i in range(len(time)):
    total = total + time[i]
    totalList.append(total)

print(sum(totalList[:]))