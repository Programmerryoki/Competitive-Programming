N = int(input())
w = set()
for _ in range(N):
    n = int(input())
    w.add(n) if not n in w else w.remove(n)
print(len(w))