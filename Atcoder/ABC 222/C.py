hand = {"G":"C", "C":"P", "P":"G"}

N,M = [int(i) for i in input().split()]
A = [input() for _ in range(2*N)]
rank = [[0,i] for i in range(2*N)]
for round in range(M):
    for i in range(0,2*N,2):
        if hand[A[rank[i][1]][round]] == A[rank[i+1][1]][round]:
            rank[i][0] += 1
        elif hand[A[rank[i+1][1]][round]] == A[rank[i][1]][round]:
            rank[i+1][0] += 1
    rank.sort(key=lambda x: (x[0], -x[1]), reverse=True)
print("\n".join(map(str, [i[1]+1 for i in rank])))