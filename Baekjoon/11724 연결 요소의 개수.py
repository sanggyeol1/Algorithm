#시작은 1로 탐색을 하여 visited가 모두 1인지 확인
#아니면 방문하지 않은 노드 중 가장 작은 값을 가진 노드부터 재탐색
#탐색 횟수를 count하면 정답

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7) #재귀깊이 제한 늘림(기본 1000)을 통해서 런타임 에러 방지
node, edge = map(int, input().split())

#간선그래프
graph = [[0]*(node+1) for _ in range(node+1)]

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


#방문여부
visited = [0] * (node + 1)

#dfs함수
def dfs(start):
    visited[start] = 1
    for i in range(1, node + 1):
        if graph[start][i] == 1 and visited[i] == 0:
            dfs(i)

count = 1
dfs(1)
for i in range(1, node + 1):
    if visited[i] == 0:
        dfs(i)
        count+=1

print(count)