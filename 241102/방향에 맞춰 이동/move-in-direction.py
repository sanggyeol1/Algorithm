n = int(input())

x, y = 0, 0

#동서남북
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    direction, distance = map(str, input().split())
    distance = int(distance)

    if direction == "E":
        move_dir = 0
    elif direction == "W":
        move_dir = 1
    elif direction == "S":
        move_dir = 2
    elif direction == "N":
        move_dir = 3

    x = x + dx[move_dir] * distance
    y = y + dy[move_dir] * distance

print(x, y)