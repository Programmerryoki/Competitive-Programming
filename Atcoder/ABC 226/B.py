N = int(input())
seen = set()
for _ in range(N):
    L,*a = [int(i) for i in input().split()]
    seen.add(tuple(a))
print(len(seen))