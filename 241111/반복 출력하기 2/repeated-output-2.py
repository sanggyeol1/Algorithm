def printHello(n):
    if n == 0: 
        return

    else:
        printHello(n-1)
        print("HelloWorld")


n = int(input())

printHello(n)