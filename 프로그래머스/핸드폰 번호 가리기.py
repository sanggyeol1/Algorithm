def solution(phone_number):
    list1 = list(phone_number)
    for i in range(0, len(list1)-4, 1):
        list1[i] = '*'
    return ("".join(list1))
    