t = int(input())

for _ in range(t):
    sentence = input()
    sentence = list(sentence.split(" "))
    
    for i in sentence:
        for j in i[::-1]:
            print(j, end="")
        print("", end=" ")
        
    print("")