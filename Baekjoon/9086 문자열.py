t = int(input())

for _ in range(t):
    word = input()

    newWord = word[0]+word[len(word)-1]
    print(newWord)