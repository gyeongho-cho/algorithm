import heapq

N = int(input())

num_list = list(map(int, input().split()))

max_heap=[]
min_heap=[]

for idx in range(N):
    n = num_list[idx]
    heapq.heappush(max_heap,-n)
    heapq.heappush(min_heap,n)

print(min_heap[0], -max_heap[0])
