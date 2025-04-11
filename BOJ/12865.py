import sys
import heapq 
import copy
N, K = map(int,input().split())

stuff = []
for _ in range(N):
    w, v = map(int, input().split())
    if w<=K:
        stuff.append((w, v))

stuff = sorted(stuff)
print(stuff)
result = []

weight = 0
for w, v in stuff:
    if weight+w>K:
        continue
    weight+=w


print(-result[0])