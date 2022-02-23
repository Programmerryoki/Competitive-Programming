from collections import deque

n = int(input())
A = [int(i) for i in input().split()]
b = deque()
rev = False
for a in A:
    if rev:
        b.appendleft(a)
    else:
        b.append(a)
    rev = not rev
print(" ".join(map(str, b if not rev else list(b)[::-1])))