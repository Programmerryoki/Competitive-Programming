from collections import deque
from bisect import bisect_right

t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i)&1 for i in input().split()]
    SA = sum(A)
    check = 1 if SA > n//2 else 0
    # print("need", check)
    need = deque()
    addn = 0
    extra = []
    available = []
    total = 0
    i = 0
    while i < n:
        print(A)
        # print(i, need, extra, total)
        if A[i] == check:
            if i < n-1 and A[i] == A[i+1]:
                if extra:
                    ind = extra.pop()
                    A[i], A[ind] = A[ind], A[i]
                    total += i - ind - (len(available) - bisect_right(available, ind))
                    i += 1
                    continue
                else:
                    need.append(i+1)
            elif extra:
                ind = extra.pop()
                A[i], A[ind] = A[ind], A[i]
                total += i - ind
        elif A[i] != check:
            if need:
                ind = need.popleft()
                A[i], A[ind] = A[ind], A[i]
                total += i - ind - addn
                addn += 1
                continue
            elif i < n-1 and A[i] == A[i+1]:
                extra.append(i+1)
                available.append(i+1)
        print(i, need, extra, total)
        i += 1
    print(total if not need and not extra else -1)