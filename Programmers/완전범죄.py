def solution(s):
    answer = 0
    n = len(s)
    
    for i in range(n):
        for j in range(i+1, n+1):
            sub = s[i:j]
            if len(sub) < 2:
                continue
                
            if sub == sub[::-1]:
                answer += 1
                
    return answer 