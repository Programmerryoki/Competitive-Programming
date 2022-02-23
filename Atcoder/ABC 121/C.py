N,M = [int(i) for i in input().split()]
store = [[int(i) for i in input().split()] for j in range(N)]
store.sort()
tc = 0
for i in range(N):
    tc += min(store[i][1], M) * store[i][0]
    M -= store[i][1]
    if M <= 0:
        break
print(tc)