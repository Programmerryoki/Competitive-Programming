N = int(input())
A = [int(i) for i in input().split()]
val = [0]*(10**5)
for a in A:
    val[a-1] += 1

t = 0
for i,n in enumerate(val):
    t += (i + 1)*n

ans = []
Q = int(input())
for _ in range(Q):
    B,C = [int(i) for i in input().split()]
    t += (C - B)*val[B-1]
    val[C-1] += val[B-1]
    val[B-1] = 0
    ans.append(str(t))
print("\n".join(map(str, ans)))