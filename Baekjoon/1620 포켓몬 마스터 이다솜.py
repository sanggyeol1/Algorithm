#key : value 와 value : key 2개의 딕셔너리를 저장하고 푸는 문제
# 2배의 저장공간을 사용하는 단점이 있지만 속도가 빠름

n,m = map(int, input().split())

#딕셔내리 선언
keyfirstpedia = {}
valuefirstpedia = {}

for i in range(1, n+1):
    pokemon = input()
    keyfirstpedia[str(i)] = pokemon
    valuefirstpedia[pokemon] = str(i)
    
    
for _ in range(m):
    keyword = input()
    
    #문자열이 모두 숫자로 이루어졌는지 확인
    if keyword.isdigit() == True:
        print(keyfirstpedia[keyword])
    else:
        print(valuefirstpedia[keyword])


