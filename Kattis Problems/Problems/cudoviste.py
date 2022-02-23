R,C = [int(i) for i in input().split()]
grid = [input() for i in range(R)]
no = [0]*5
for i in range(R-1):
    for j in range(C-1):
        park = grid[i][j:j+2] + grid[i+1][j:j+2]
        if "#" in park:
            continue
        no[park.count("X")] += 1
print("\n".join(map(str, no)))