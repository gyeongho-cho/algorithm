move_dict = {
             'up':[-1,0],
             'down':[1,0],
             'right':[0,1],
             'left':[0,-1]}

def str2bool(x):
    if x=='1':
        return True
    else:
        return False
N, M = map(int, input().split())

board = []

for _ in range(N):
    # board.append(list(map(str2bool, input().strip())))
    board.append(input())
depth = 0
state = [[0,0,1]] # r,c,l
done=False
visited = [False]*N*M*2
while True:
    depth+=1

    next_state = []
    for s in state:
        r, c, l = s

        if visited[l*N*M+r*M+c]:
            continue
        visited[l*N*M+r*M+c] = True

        for k, d_loc in move_dict.items():
            dr, dc = d_loc
            nr = r+dr
            nc = c+dc
            if nr==(N-1) and nc==(M-1):
                done=True
            if nr<0 or nr>=N or nc<0 or nc>=M:
                continue

            if board[nr][nc]=='1' and l:
                next_state.append([nr,nc,0])
            elif board[nr][nc]=='1':
                continue
            else:
                next_state.append([nr,nc,l])

    state = next_state
    if done or len(state)==0:
        break
if N==1 and M==1:
    print(1)
elif done:
    print(depth+1)
else:
    print(-1)