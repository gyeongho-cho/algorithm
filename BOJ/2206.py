#-----------------
import heapq
import sys
sys.setrecursionlimit(10**6)


move_dict = {
             'down':[1,0],
             'right':[0,1]}
chance_move_dict = {
             'up':[-1,0],
             'left':[0,-1]
             }

def dfs(loc, life, chance, depth):
    r,c = loc
    if visited[r*M+c]:
        return -1
    
    visited[r*M+c] = True
    # print(loc, life)
    if (r == (N-1)) and (c == (M-1)):
        return depth

    output = []
    for k, dloc in move_dict.items():
        dr, dc = dloc        
        nr = r+dr
        nc = c+dc
        if nr<0 or nr>=N or nc<0 or nc>=M:
            continue

        next_loc = [nr, nc]
        if board[nr][nc]==1 and life:
            out = dfs(next_loc, 0, chance, depth+1)
        elif board[nr][nc]==1:
            continue
        else:
            out = dfs(next_loc, life, chance, depth+1)

        if out >= 0:
            output.append(out)

    if chance>0:
        for k, dloc in chance_move_dict.items():
            dr, dc = dloc        
            nr = r+dr
            nc = c+dc
            if nr<0 or nr>=N or nc<0 or nc>=M:
                continue

            next_loc = [nr, nc]
            if board[nr][nc]==1 and life:
                out = dfs(next_loc, 0, chance-1, depth+1)
            elif board[nr][nc]==1:
                continue
            else:
                out = dfs(next_loc, life, chance-1, depth+1)

            if out >= 0:
                output.append(out)

    visited[r*M+c] = False
    # print(loc,output)
    if len(output):
        # print(loc, min(output))
        return min(output)
    else:
        # print(loc, -1)
        return -1
    

N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(map(int, input().strip())))

visited=[False]*N*M
loc = [0,0]
life=1
depth=1

chance = 0
while True:
    result = dfs(loc, life, chance, depth) 
    if result>-1:
        print(result)
        break
    chance+=1
    if chance>(10):
        print(-1)
        break
'''
# visit = [False]*N*M # visit[m*(n-1) + m-1]
def bfs(r=0,c=0, visit=[False]*N*M, crash=False, dist=0):
    
    
    if visit[M*r+c]:
        return
    visit[M*r+c] = True

    if table[r][c]:
        if crash:
            return 
        else:
            crash = True

    dist += 1

    print(dist, r, c, sum(visit), crash)

    if r == N-1 and c ==M-1:
        heapq.heappush(result, dist)

    else:
        if r+1<N: #down
            bfs(r+1, c, visit, crash, dist)
        if r-1>=0: #up
            bfs(r-1, c, visit, crash, dist)
        if c+1<M: #right
            bfs(r, c+1, visit, crash, dist)
        if c-1>=0: #left
            bfs(r, c-1, visit, crash, dist)

    visit[M*r+c] = False
    return

bfs()

if len(result):
    if result[0] != 1:
        print(result[0])
    else:
        print(-1)
else:
    print(-1)
'''

#---------------