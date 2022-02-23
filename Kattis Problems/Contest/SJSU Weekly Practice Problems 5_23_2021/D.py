grid = [input() for i in range(4)]
empty = []
for i in range(4):
    for j in range(4):
        if grid[i][j] == "W":
            empty.append((i,j))
moves = [(1,0),(-1,0),(0,1),(0,-1)]

color_pair = {}
for i in range(4):
    for j in range(4):
        if grid[i][j] != "W":
            if grid[i][j] in color_pair:
                color_pair[grid[i][j]].append((i,j))
            else:
                color_pair[grid[i][j]] = [(i,j)]

def search(color, start, end, dic):
    que = [start]
    while que:
        i,j = que.pop()
        for dx,dy in moves:
            x,y = i+dx,j+dy
            if 0 <= x < 4 and 0 <= y < 4:
                if dic[(x,y)] == color:
                    que.append((x,y))
                if (x,y) == end:
                    return True
    return False

def recur(i,loc):
    if i < len(empty):
        for color in "RGBY":
            rec = loc.copy()
            rec.update({empty[i]: color})
            recur(i+1, rec)
    else:
        ans = True
        for key in color_pair:
            if not search(key, color_pair[key][0], color_pair[key][1], loc):
                ans = False
                break
        return ans

loc = {}
for key in color_pair:
    for i in range(2):
        loc[color_pair[key][i]] = key
print("solvable" if recur(0, loc) else "not solvable")