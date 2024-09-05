import sys
input = sys.stdin.readline

t = int(input())

S = set()
#추가
# S.add(4)
#삭제
# S.remove(4)

for _ in range(t):
    command = list(input().split())
    
    if command[0] == "add":
        if command[1] in S:
            continue
        else:
            S.add(command[1])
    elif command[0] == "remove":
        if command[1] not in S:
            continue
        else:
            S.remove(command[1])
        
    elif command[0] == "check":
        if command[1] in S:
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        if command[1] in S:
            S.remove(command[1])
        else:
            S.add(command[1])
    elif command[0] == "all":
        S.update({"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"})
    elif command[0] == "empty":
        S.clear()
