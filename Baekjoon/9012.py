T = int(input())

#vps판별함수
def isVps(vpsrange):
    stack = []
    for i in vpsrange:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack:
                stack.pop()
            else:
                return False
    #스택이 비었으면 
    if not stack:
        return True
    else:
        return False


for _ in range(T):
    vpsrange = input()
    if isVps(vpsrange) == True:
        print("YES")
    else:
        print("NO")
