n = int(input())

for i in range(n):
    creator = i
    for j in str(i):
        creator+=int(j)
    if int(n) == creator:
        print(i)
        break
    elif n == i+1:
        print(0)


    

