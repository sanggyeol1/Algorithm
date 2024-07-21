T = int(input())

for _ in range(T):
    sentence = list(input().split())

    for i in sentence:
        word = list(i)
        word.reverse()
        word = "".join(word)
        print(word, end=" ")

