N = int(input())
A = [int(input()) for i in range(N)]
seen = set()
p = 1
while True:
    if not p in seen:
        seen.add(p)
        if p == 2:
            print(len(seen) - 1)
            break
        p = A[p-1]
    else:
        print(-1)
        break