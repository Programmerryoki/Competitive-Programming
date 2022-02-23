N,Q = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
shift = 0
ans = []
for _ in range(Q):
    T,x,y = [int(i)-1 for i in input().split()]
    if T == 0:
        A[x-shift], A[y-shift] = A[y-shift], A[x-shift]
    elif T == 1:
        shift += 1
        shift %= len(A)
    elif T == 2:
        # print(A, shift)
        ans.append(A[x - shift])
print("\n".join(str(a) for a in ans))