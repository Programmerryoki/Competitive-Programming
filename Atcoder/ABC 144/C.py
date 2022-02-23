N = int(input())
m = float("inf")
for n in range(1, int(N**0.5)+1):
    if N%n == 0:
        m = min(m, n + N//n - 2)
print(m)