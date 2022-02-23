perm = [1]
for i in range(1, 14):
    perm.append(perm[-1] * i)

N,M,K = [int(i) for i in input().split()]

arr = [-1]*14
for i in range(1, 13):
    arr[i] = (K % perm[i+1]) // perm[i]
    K -= K % perm[i+1]
used = set(arr)
ans = [i if i > 0 else -1 for i in arr]
for i in range(len(ans)):
    if ans[i] != -1:
        continue
    for j in range(1, max(N+1, 15)):
        if j in used:
            continue
        ans[i] = j
        used.add(j)
        break
if N < 14:
    print("\n".join(str(i) for i in ans[:N]))
else:
    M -= (N - 1) * N // 2
    print("\n".join(str(i) for i in ans[:N]+[j for j in range(15, N)]+[M]))