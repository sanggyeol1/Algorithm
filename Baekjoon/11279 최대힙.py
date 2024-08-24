#최소힙에서 약간의 트릭 : -1을 곱해서 heappush한다, -1곱해서 heappop 한다
import sys
import heapq

input = sys.stdin.readline

#테스트 케이스의 수
t = int(input())

#힙 리스트 선언
max_heap = []

for _ in range(t):
    num = int(input())
    
    if num == 0:
        if len(max_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(max_heap)*-1)
    else:
        heapq.heappush(max_heap, num * -1)
        