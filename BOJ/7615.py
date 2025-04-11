# BOJ 7615 Hashing

'''
INPUT:
2
2 3 1 3 0 1 7
1 0 0 8 0 8 9

OUTPUT:
1
9
'''
def hash1_fun(x, a, b, m):
    return (a*x + b)%m

def hash2_fun(x,c,d):
    return max((x-(c-1))*(d+1-x),0)/max((x-(c-1))*(d+1-x),1)
 
t = int(input())
for _ in range(t):

    result=0
    a, b, x, n, c, d, m = map(int, input().split())

    for y in range(x,x+n+1):

        key = hash1_fun(y, a, b, m)
        key2 = hash2_fun(key, c, d)
        result += key2

        
    print('%d' % result)

'''
2
2 3 1 3 0 1 7
1 0 0 8 0 8 9
'''