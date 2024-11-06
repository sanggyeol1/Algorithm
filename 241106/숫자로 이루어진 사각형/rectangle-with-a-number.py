def func(num):
    val = 1
    for _ in range(num):
        for _ in range(num):
            print(val, end=" ")
            if val == 9:
                val=1
            else:
                val+=1
        print("")


n = int(input())

func(n)