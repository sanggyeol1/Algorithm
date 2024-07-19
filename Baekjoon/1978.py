T = int(input())

numbers = list(map(int, input().split()))

count=0
#[1, 3, 5, 6]
for i in numbers:
    #1인경우 소수아님
    if i == 1:
        continue
        
    for j in range(2,i+1):
        #소수가 아닌경우
        if i%j==0 and i != j:
            break
        
        #끝까지 온 경우
        if i == j:
            count+=1
        
print(count)
            
            
        

    

    