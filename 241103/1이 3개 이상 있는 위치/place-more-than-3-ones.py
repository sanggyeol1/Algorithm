n = int(input())

lista = []

for _ in range(n):
    row = list(map(int, input().split()))
    lista.append(row)



answer = 0
for i in range(len(lista)):
    for j in range(len(lista[i])):
        oneCount = 0
        if i == 0 and j == 0:
            oneCount = lista[i+1][j] + lista[i][j+1]
        elif i == 0 and j > 0 and j < n-1:
            oneCount = lista[i+1][j] + lista[i][j-1] + lista[i][j+1]
        elif i == 0 and j == n-1:
            oneCount = lista[i+1][j] + lista[i][j-1]

        elif i > 0 and i < n-1 and j == 0:
            oneCount = lista[i+1][j] + lista[i-1][j] + lista[i][j+1]
        elif i > 0 and i < n-1 and j > 0 and j < n-1:
            oneCount = lista[i+1][j] + lista[i-1][j] + lista[i][j+1] + lista[i][j-1]
        elif i > 0 and i < n-1 and j == n-1:
            oneCount = lista[i+1][j] + lista[i-1][j] + lista[i][j-1]

        elif i == n-1 and j == 0:
            oneCount = lista[i-1][j] + lista[i][j+1]
        elif i == n-1 and j > 0 and j < n-1:
            oneCount = lista[i-1][j] + lista[i][j+1] + lista[i][j-1]
        elif i == n-1 and j == n-1:
            oneCount = lista[i-1][j] + lista[i][j-1]
        
    
        if oneCount >= 3:
            answer+=1

print(answer)