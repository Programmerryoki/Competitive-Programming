N,P,K = [int(i) for i in input().split()]
A = [[int(i) for i in input().split()] for j in range(N)]

def count(num):
    dist = [[i if i != -1 else num for i in j] for j in A]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    c = 0
    for i in range(N):
        for j in range(i+1, N):
            if dist[i][j] <= P:
                c += 1
    return c

def border(cnt):
    left = 1; right = 10**11
    minx = 10**11
    for i in range(40):
        mid = (left + right) // 2
        pos = count(mid)
        if pos <= cnt:
            right = mid
            minx = min(minx, mid)
        else:
            left = mid
    return minx

left = border(K)
right = border(K-1)
# print(left, right)
if right - left >= 10**10:
    print("Infinity")
else:
    print(right - left)