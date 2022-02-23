N,K = map(int, input().split())
friend = [[int(i) for i in input().split()] for j in range(N)]
friend.sort()
cur = 0
i = 0
while True:
    if i >= N:
        print(cur + K)
        exit()
    if cur + K < friend[i][0]:
        print(cur + K)
        exit()

    K -= friend[i][0] - cur
    K += friend[i][1]
    cur = friend[i][0]
    i += 1