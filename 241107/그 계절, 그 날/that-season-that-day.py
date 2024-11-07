thirtyOneMonth = [1, 3, 5, 7, 8, 10, 12]
thirtyMonth = [4, 6, 9, 11]

def isYoon(Y):
    if Y % 4 == 0 and Y % 100 != 0:
        return True
    elif Y % 400 == 0:
        return True
    else:
        return False


def isExistDay(Y, M, D):

    if M in thirtyOneMonth:
        if D <= 31:
            return True
        else:
            return False
    
    elif M in thirtyMonth:
        if D <= 30:
            return True
        else:
            return False
    

    #윤년일 때
    elif isYoon(Y) == True and M == 2:
        if D <= 29:
            return True
        else:
            return False
    

    elif isYoon(Y) == False and M ==2:
        if D <= 28:
            return True
        else:
            return False



def weather(Y, M, D):
    if isExistDay(Y, M, D) == False:
        print(-1)
    else:
        if 2 < M and M <= 5:
            print("Spring")
        elif 5 < M and M <= 8:
            print("Summer")
        elif 8 < M and M <= 11:
            print("Fall")
        elif 11 < M or M <= 2:
            print("Winter")


Y, M, D = map(int, input().split())



weather(Y, M, D)