R,S = map(int, input().split())
seats = [[int(j=="o") for j in input()] for i in range(R)]
empty = [[0]*S for i in range(R)]
checking = [(1,0),(-1,0),(0,1),(0,-1),(1,-1),(1,1),(-1,1),(-1,-1)]
for i in range(R):
    for j in range(S):
        for dx,dy in checking:
            x,y = i+dx,j+dy
            if 0 <= x < R and 0 <= y < S:
                if seats[x][y] == 1:
                    empty[i][j] += 1
maxm = [0,0]
for i in range(R):
    for j in range(S):
        if empty[i][j] > empty[maxm[0]][maxm[1]] and seats[i][j] != 1:
            maxm = [i,j]
seats[maxm[0]][maxm[1]] = 1

checks = [(1,0),(0,1),(1,1),(1,-1)]

total = 0
for i in range(R):
    for j in range(S):
        if seats[i][j] != 1:
            continue
        for dx,dy in checks:
            x,y = i+dx,j+dy
            if 0 <= x < R and 0 <= y < S:
                if seats[x][y] == 1:
                    total += 1
print(total)