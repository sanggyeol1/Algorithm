def prstar(n):
    if n == 0:
        return
    
    prstar(n-1)
    print("*" * n)


n = int(input())
prstar(n)