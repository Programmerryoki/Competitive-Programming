from itertools import permutations as perm
n,m = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
A.sort(reverse=True)
ans = perm(A,2)
t = 0
c = 0
for a in ans:
    print(a)
    t += sum(a)
    c += 1
    if c == m:
        break
print(t)