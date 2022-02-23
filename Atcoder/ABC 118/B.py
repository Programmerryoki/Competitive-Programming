N,M = [int(i) for i in input().split()]
s = [0]*M
for _ in range(N):
    K,*A = [int(i) for i in input().split()]
    for i in A:
        s[i-1] += 1
print(s.count(N))