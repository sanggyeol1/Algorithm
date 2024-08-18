t = int(input())

dequeue = []

for _ in range(t):
    command = list(input().split())
    
    if command[0] == "push_front":
        dequeue.insert(0, command[1])
    
    elif command[0] == "push_back":
        dequeue.append(command[1])

    elif command[0] == "pop_front":
        if len(dequeue) == 0:
            print(-1)
        else:
            print(dequeue.pop(0))
    
    elif command[0] == "pop_back":
        if len(dequeue) == 0:
            print(-1)
        else:
            print(dequeue.pop())
    
    elif command[0] == "size":
        print(len(dequeue))
    
    elif command[0] == "empty":
        if len(dequeue) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == "front":
        if len(dequeue) == 0:
            print(-1)
        else:
            print(dequeue[0])
    
    elif command[0] == "back":
        if len(dequeue) == 0:
            print(-1)
        else:
            print(dequeue[len(dequeue)-1])