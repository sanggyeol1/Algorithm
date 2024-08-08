n = int(input())

#3kg 5kg
five = n // 5
extra = n % 5
three = extra // 3

while five != -1:
    #5kg최대인 경우
    if extra % 3 == 0:
        print(five+three)
        break
    #5kg최대에서 하나 뺀 경우
    elif extra % 3 != 0:
        five = five - 1
        extra += 5
        three = extra // 3

if five == -1:
    print(-1)