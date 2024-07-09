T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    
    floor = (N-1) %  H + 1
    num = (N-1) // H + 1
    room = floor * 100 + num
    
    print(room)

