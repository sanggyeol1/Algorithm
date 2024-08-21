import sys
input = sys.stdin.readline

computer = int(input())
link = int(input())
start = 1

#행렬만들기
graph = [[0]*(computer + 1) for _ in range(computer + 1)]
for _ in range(link):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

#방문여부
visited = [0]*(computer+1)

#탐색
def dfs(start):
    visited[start] = 1
    for i in range(1, computer + 1):
        if visited[i] == 0 and graph[start][i] == 1:
            dfs(i)

dfs(start)
answer = visited.count(1)
print(answer - 1)



