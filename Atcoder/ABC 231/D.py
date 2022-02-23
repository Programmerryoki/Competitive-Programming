N,M = [int(i) for i in input().split()]
count = {i:set() for i in range(N)}
for _ in range(M):
    A,B = [int(i)-1 for i in input().split()]
    if A in count[B] and B in count[A]:
        continue
    elif len(count[A]) >= 2 or len(count[B]) >= 2:
        print("No")
        break
    else:
        count[A].add(B)
        count[B].add(A)
else:
    # print(count)
    seen = set()
    for key in count:
        if key in seen:
            continue
        if len(count[key]) == 2:
            continue
        elif len(count[key]) == 0:
            seen.add(key)
            continue
        # print(key)
        tmp = key
        seen.add(tmp)
        while True:
            s = (count[tmp] - seen)
            if not s:
                break
            nxt = s.pop()
            if nxt in seen:
                print("No")
                exit()
            tmp = nxt
            seen.add(tmp)
    # print(seen)
    print("Yes" if len(seen) == N else "No")