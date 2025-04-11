import sys 

input = sys.stdin.readline

D, K = map(int, input().split())

ca = [1, 0]
cb = [0, 1]
for d in range(D-2):
    ca.append(sum(ca))
    cb.append(sum(cb))

    ca.pop(0)
    cb.pop(0)

ca = ca[-1]
cb = cb[-1]
print(ca,'i +',cb,'j')
for i in range(1,K//2):
    for j in range(i,K//2):
        v = ca*i+cb*j
        # print(v)
        if v>K:break
        if v==K:break

    if v==K:
        break
print(i,j)
print(v,K)