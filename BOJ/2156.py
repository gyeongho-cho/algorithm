'''
Dynamic Programming을 이용하여 해결하려고 합니다.
i번째 포도주를 마시는 경우와 마시지 않는 경우를 체크하고, i번째 잔까지 탐색했을 때의 최댓값을 메모이제이션하려고 합니다.
이 방식으로 진행해도 괜찮을까요?

1. i번째 포도주를 마시는 경우
1-a) i-1번째를 마신 경우 최댓값
dp[i-3] + arr[i-1] + arr[i]
1-b) i-1번째를 마시지 않은 경우 최댓값
dp[i-2] + arr[i]

2. i번째 포도주를 마시지 않는 경우 최댓값 -> i-1번째 최댓값이랑 동일
dp[i-1]

3. 3개 중에 최댓값 찾기
dp[i] = max([dp[i-3] + arr[i-1] + arr[i],
             dp[i-2] + arr[i],
             dp[i-1]])
'''

### Bottom-Up 방식 ###
import sys

input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

dp = [0]*N

# def solution(n):
#     dp[0] = arr[0]
#     if n==1:
#         return dp[-1]
#     dp[1] = arr[0]+arr[1]
#     if n==2:
#         return dp[-1]
#     dp[2] = max([arr[0]+arr[2],
#                  arr[1]+arr[2],
#                  arr[0]+arr[1]])
#     if n==3:
#         return dp[-1]

#     for i in range(3, n):
#         dp[i] = max([
#             dp[i-3] + arr[i-1] + arr[i],
#             dp[i-2] + arr[i],
#             dp[i-1]
#         ])
#     return dp[-1]

# print(solution(N))
sys.setrecursionlimit(100000)

### Top-Down 방식 ###
dp = [0]*N
visit = [False]*N
def solution2(i):
    if visit[i]:
        return dp[i]
    visit[i] = True
    
    if i == 0:
        dp[i] = arr[0]
    elif i == 1:
        dp[i]=arr[0]+arr[1]
    elif i == 2:
        dp[i]=max([arr[0]+arr[1],
                    arr[1]+arr[2],
                    arr[0]+arr[2]])
    else:
        dp[i] = max([
                solution2(i-3) + arr[i-1] + arr[i],
                solution2(i-2) + arr[i],
                solution2(i-1)
            ])
    
    return dp[i]


print(solution2(N-1))
    
