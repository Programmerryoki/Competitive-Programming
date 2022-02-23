from collections import deque

T = int(input())
for case in range(T):
    S = input()
    F = input()
    md = [float("inf")] * 26
    que = deque()
    for f in F:
        md[ord(f) - ord("a")] = 0
        que.append(ord(f) - ord("a"))
    seen = set()
    while que:
        cur = que.popleft()
        for dx in [-1,1]:
            nxt = (cur + dx)%26
            if md[nxt] > md[cur] + 1:
                md[nxt] = md[cur] + 1
                que.append(nxt)

    total = 0
    for s in S:
        total += md[ord(s) - ord("a")]
    print(f"Case #{case+1}: {total}")