def xor(B):
    a = B[0]
    for b in B[1:]:
        a ^= b
    return a

N = int(input())
A = [[int(i) for i in input().split()] for _ in range(2*N-1)]
used = set()
mv = 0
def dfs(B):
    global mv, used
    if len(B) == N:
        mv = max(mv, xor(B))
        return
    for i in range(2*N-1):
        if i not in used:
            used.add(i)
            for j in range(2*N-i-1):
                if j+i+1 not in used:
                    used.add(j+i+1)
                    dfs(B + [A[i][j]])
                    used.remove(j+i+1)
            used.remove(i)

dfs([])
print(mv)