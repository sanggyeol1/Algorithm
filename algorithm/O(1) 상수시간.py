def check_first_element(myList):
    if myList:
        return myList[0]  # 항상 상수 시간 소요
    return None

print(check_first_element([1,2,3]))
print(check_first_element([1,2,3,4,5,6,7,8,9,10]))