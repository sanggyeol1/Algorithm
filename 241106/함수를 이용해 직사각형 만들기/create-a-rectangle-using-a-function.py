n, m = map(int, input().split())

def printOne(n, m):
    for _ in range(n):
        for _ in range(m):
            print("1", end="")
        print("")

printOne(n, m)