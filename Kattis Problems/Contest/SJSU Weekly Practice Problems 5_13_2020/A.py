N,L = [int(i) for i in input().split()]
t = 0
for _ in range(N):
    D,R,G = [int(i) for i in input().split()]
    n = (t + D)%(R+G)
    if n <= R:
        t += R - n
print(t + L)