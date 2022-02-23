import heapq

while True:
    N,k = map(int, input().split())
    if N == 0 and k == 0:
        break
    vroom = [[int(i) for i in input().split()] for j in range(N)]
    que = []
    for i in range(len(vroom)):
        for j in range(len(vroom[0])):
            heapq.heappush(que, [vroom[i][j], (i,j)])
    box = [[1]*len(vroom[0]) for i in range(N)]
    close = 0
    pos = [[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
    while close < k:
        val,(i,j) = heapq.heappop(que)
        for dx,dy in pos:
            x,y = i+dx,j+dy
            if 0 <= x < len(vroom) and 0 <= y < len(vroom[0]):
                if box[x][y] == 1:
                    continue
                else:
                    break
        else:
            box[i][j] = 0
            close += 1
    print(sum([sum([vroom[j][i] for i in range(len(vroom[0])) if box[j][i]]) for j in range(len(vroom))]))
