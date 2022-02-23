n = int(input())
rc = [int(i) for i in input().split()]
bs = [int(i) for i in input().split()]
r = 0
b = 0
for a in range(n):
    if rc[a] > bs[a]:
        r += 1
    elif rc[a] < bs[a]:
        b += 1
if r == 0:
    print(-1)
else:
    print(b//r+1)