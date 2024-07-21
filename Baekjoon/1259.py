def isPel(num):
    for i in range(int(num)):
        if num[i] == num[len(num)-i-1]:
            if i == len(num)-1:
                print("yes")
                return True
            else:
                pass
        
        else:
            print("no")
            return False
            
while True:
    n = input()

    if n == '0':
        break
    
    isPel(n)

    