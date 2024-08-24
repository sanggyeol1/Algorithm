import heapq
import sys
input = sys.stdin.readline
t = int(input())

heap = []
#heapq.heapify(heap) 이미 완성된 리스트를 힙으로 변환

for _ in range(t):
    num = int(input())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num) #heap리스트에 heappush