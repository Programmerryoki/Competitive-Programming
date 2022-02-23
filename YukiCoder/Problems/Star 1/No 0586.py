P1, P2 = int(input()), int(input())
N = int(input())
R = set()
ex = 0
for _ in range(N):
    n = int(input())
    if n in R:
        ex += 1
    R.add(n)
print(ex*(P1+P2))