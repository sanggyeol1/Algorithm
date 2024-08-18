#포인트 : pop(), append()는 O(1)의 시간복잡도를 가진다 
#insert는 O(n)이다.(빈 공간을 채우려고 남은 요소들을 옮기기 때문)

import sys

l_arr = list(sys.stdin.readline().strip())
r_arr = []

# l_arr = [a, b,]    r_arr = [d c]

t = int(sys.stdin.readline())
for _ in range(t):
    command = list(sys.stdin.readline().split())

    if command[0] == "L":
        if len(l_arr) != 0:
            r_arr.append(l_arr.pop())
    
    elif command[0] == "D":
        if len(r_arr) != 0:
            l_arr.append(r_arr.pop())
    
    elif command[0] == "B":
        if len(l_arr) != 0:
            l_arr.pop()
        
    elif command[0] == "P":
        l_arr.append(command[1])


l_arr = "".join(l_arr)
r_arr.reverse()
r_arr = "".join(r_arr)

print(l_arr + r_arr)
            