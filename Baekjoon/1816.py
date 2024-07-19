T = int(input())

for _ in range(T):
    n = int(input())
    #2부터 100만까지
    for i in range(2, 1000001):
        #i로 나눠떨어지면 NO후 종료
        if n%i == 0:
            print("NO")
            break
        
        #끝까지 다 돌았다면
        if i == 1000000:
            print("YES")
            
    