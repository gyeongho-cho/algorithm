import heapq

N = int(input())

heap = []
for _ in range(N):
    heapq.heappush(heap, int(input()) )


answer = 0
while True:

    n_card = len(heap)
    if n_card==1:
        break
    new_card = heapq.heappop(heap)
    new_card += heapq.heappop(heap)
    
    heapq.heappush(heap, new_card)
    answer+=new_card
    
print(answer)