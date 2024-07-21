import sys
T = int(sys.stdin.readline())

stack = []

for _ in range(T):
    command = list(sys.stdin.readline().split())

    #push
    if command[0] == "push":
        stack.append(command[1])

    #pop
    elif command[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    #size
    elif command[0] == "size":
        print(len(stack))
    
    #empty
    elif command[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    #top
    elif command[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])

        
        

