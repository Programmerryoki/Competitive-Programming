N,K = [int(i) for i in input().split()]
node = []
for _ in range(N):
    node.append([int(i) for i in input().split()])

node.sort()
mia = float("INF")
for i in range(N-K+1):
    y = [i[1] for i in node[i:i+K]]
    print(y,node[i][0],node[i+K-1][0])
    a = abs(node[i][0] - node[i+K-1][0])*abs(max(y) - min(y))
    if a < mia:
        mia = a

node.sort(key = lambda x:x[1])
for i in range(N-K+1):
    x = [i[0] for i in node[i:i+K]]
    print(x)
    a = abs(node[i][1] - node[i+K-1][1])*abs(max(x) - min(x))
    if a < mia:
        mia = a

print(mia)