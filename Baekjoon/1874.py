T = int(input())


#1부터 T까지의 수를 오름차순으로 스택에 삽입, 팝
#입력한 순서대로 출력하려면 푸시와 팝을 어떻게 배치해야 하는지
stack = []
lista = []

for i in range(T):
    n = int(input())
    lista.append(n)

#스택의 상단값이 lista[i-1] 와 같은지?
#같으면 pop 다르면 push
c = 1
i = 1
while True:
    #T까지만
    if c == T:
        break

    #스택이 비어있다면
    if len(stack) == 0:
        stack.append(i)
        print("+")
        i += 1

    #스택의 상단값 == 리스트의 인덱스값
    elif lista[c-1] == stack[len(stack)-1]:
        stack.pop()
        print("-")
        i += 1
        c += 1
    #같지 않다면
    elif lista[c-1] != stack[len(stack)-1]:
        stack.append(i)
        print("+")
        i+=1
    


