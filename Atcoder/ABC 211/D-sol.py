# 入力の読み込み
N,M=map(int,input().split())
G=[[] for i in range(N)]
for i in range(M):
    A,B=map(int,input().split())
    A-=1
    B-=1
    G[A].append(B)
    G[B].append(A)

# 初期化
que=[0]
dist=[None]*N
cnt=[0]*N
dist[0]=0
cnt[0]=1

# BFS
for v in que:
    for vv in G[v]:
        if dist[vv] is None:
            dist[vv]=dist[v]+1
            que.append(vv)
            cnt[vv]=cnt[v]
        elif dist[vv]==dist[v]+1:
            cnt[vv]+=cnt[v]
            cnt[vv]%=10**9+7

print(cnt[N-1])
