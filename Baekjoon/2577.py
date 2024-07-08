A = int(input())
B = int(input())
C = int(input())

mul = A*B*C

list = [0,0,0,0,0,0,0,0,0,0]

for i in str(mul):
    list[int(i)]+=1
    
for i in list:
    print(i)