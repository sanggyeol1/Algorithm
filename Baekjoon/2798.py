N, M = map(int, input().split())
lst = list(map(int, input().split()))

answer = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if lst[i]+lst[j]+lst[k] >= answer and lst[i]+lst[j]+lst[k] <= M:
                answer = lst[i]+lst[j]+lst[k]

print(answer)
                
                
                

    