N = int(input())
A = [int(i) for i in input().split()]
AT = [(A[i], i) for i in range(N)]
AT.sort(reverse=True)
checked = set()
s = 0
avmd = [-float("inf"), -float("inf")]
for i, (v, ind) in enumerate(AT, 1):
    checked.add(ind)
    if ind > 0:
        checked.add(ind-1)
    s += v
    if len(checked) == N:
        avmd[0] = max(avmd[0], s / i)
        avmd[1] = max(avmd[1], AT[i//2][0])
print(avmd[0])
print(avmd[1])