from collections import deque

N = int(input())
an = []
ns = deque()
for a in range(1, int(N**0.5)+1):
    if N%a==0:
        an.append(a-1)
        if a != N//a:
            ns.appendleft(N//a-1)
print(" ".join(map(str, an))," ".join(map(str, ns)))