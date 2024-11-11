def prnuma(n):
    if n == 0:
        return

    else:
        prnuma(n-1)
        print(n, end=" ")

def prnumd(n):
    if n == 0:
        return

    else:
        print(n, end=" ")
        prnumd(n-1)
       

n = int(input())

prnuma(n)
print("")
prnumd(n)