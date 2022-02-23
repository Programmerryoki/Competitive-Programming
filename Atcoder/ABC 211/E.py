N = int(input())
K = int(input())
S = [input() for i in range(N)]
moves = [(0,1),(0,-1),(1,0),(-1,0)]
allpos = set()
seen = set()
SEEN = set()
neigh = {}

def dfs(i,j,k):
    global allpos, seen, neigh
    if k == K:
        su = tuple(sorted(seen))
        if su not in allpos:
            allpos.add(su)
        return

    nei = set()
    for dx,dy in moves:
        x,y = i+dx,j+dy
        tup = (x,y)
        if 0 <= x < N and 0 <= y < N and S[x][y] == "." and tup not in seen and tup not in SEEN:
            nei.add(tup)
    for i in nei:
        if i in neigh:
            neigh[i] += 1
        else:
            neigh[i] = 1
    for i in tuple(neigh.keys()):
        if i in seen:
            continue
        seen.add(i)
        dfs(i[0], i[1], k+1)
        seen.remove(i)
    for i in nei:
        if i in neigh:
            neigh[i] -= 1
            if neigh[i] == 0:
                del neigh[i]

for i in range(N):
    for j in range(N):
        # print(i,j,allpos)
        if S[i][j] == ".":
            seen.add((i,j))
            dfs(i,j,1)
            seen.clear()
            neigh.clear()
        SEEN.add((i,j))

# print(allpos)
print(len(allpos))