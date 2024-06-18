word = str(input())
word = word.split(" ")
count = 0
for i in word:
    if(i != ""):
        count+=1
print(count)
