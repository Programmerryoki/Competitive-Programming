N,L = [int(i) for i in input().split()]
K = int(input())
A = [0]+[int(i) for i in input().split()]+[L]
A.sort()
dif = [A[i+1] - A[i] for i in range(len(A)-1)]

def possible(val):
    cur = 0
    groups = 0
    for a in dif:
        if a + cur < val:
            cur += a
        elif a + cur >= val:
            cur = 0
            groups += 1
    return groups <= K

left = min(dif)
right = L
while left < right - 1:
    mid = (left + right) // 2
    if possible(mid):
        right = mid
    else:
        left = mid
print(left)