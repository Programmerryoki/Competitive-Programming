n = int(input())
T = 0
H = 0
for _ in range(n):
    t,h = input().split()
    if t < h:
        H += 3
    elif t > h:
        T += 3
    else:
        T += 1
        H += 1
print(T,H)