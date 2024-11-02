x, y = 0, 0

command = input()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

direction = 0

for i in command:
    if i == "R":
        direction = (direction + 1)% 4
    elif i == "L":
        direction = (direction - 1 + 4)% 4

    elif i == "F":
        x = x + dx[direction]
        y = y + dy[direction]

print(x, y)