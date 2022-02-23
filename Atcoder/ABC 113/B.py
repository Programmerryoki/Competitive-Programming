N = int(input())
T,A = [int(i) for i in input().split()]
H = [int(i) for i in input().split()]
m = -float("inf")
p = -1
for i,h in enumerate(H,1):
    t = T - (h * 6 / 1000)
    if abs(A - t) < abs(A - m):
        m = t
        p = i
print(p)