x, y = 0, 0

n = int(input())

for _ in range(n):
    direction, length = map(str, input().split())
    if direction == "N":
        y = y + int(length)
    
    if direction == "E":
        x = x + int(length)
    
    if direction == "S":
        y = y - int(length)
    
    if direction == "W":
        x = x - int(length)

print(x, y)