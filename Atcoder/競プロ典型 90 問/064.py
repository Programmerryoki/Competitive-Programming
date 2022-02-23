N,Q = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
height = [A[i+1]-A[i] for i in range(len(A)-1)]
sh = sum(abs(h) for h in height)
ans = [0]*Q
for q in range(Q):
    L,R,V = [int(i) for i in input().split()]
    L -= 2; R -= 1
    for val in [L,R]:
        if val < 0 or len(height) <= val:
            V *= -1
            continue
        sh -= abs(height[val])
        height[val] += V
        sh += abs(height[val])
        V *= -1
    ans[q] = sh
print("\n".join(str(a) for a in ans))