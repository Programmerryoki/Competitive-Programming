N,Q = [int(i) for i in input().split()]
follow = [[0]*N for i in range(N)]
for _ in range(Q):
    line = input().split()
    if line[0] == "1":
        a,b = int(line[1])-1, int(line[2])-1
        follow[a][b] = 1
    elif line[0] == "2":
        a = int(line[1])-1
        for i in range(N):
            if follow[i][a]:
                follow[a][i] = 1
    else:
        a = int(line[1])-1
        ppl = [i for i in range(N) if follow[a][i]]
        for x in ppl:
            for i in range(N):
                if follow[x][i] and i != a:
                    follow[a][i] = 1
print("\n".join("".join(["Y" if i else "N" for i in j]) for j in follow))