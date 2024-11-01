lista = []

for i in range(5):
    
    row = list(map(str, input().split()))
    for j in range(len(row)):
        row[j] = row[j].upper()
    lista.append(row)


for i in lista:
    for j in i:
        print(j, end=" ")
    print("")