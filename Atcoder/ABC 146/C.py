A, B, X = [int(i) for i in input().split()]
pos = []

for a in range(1,18):
    pos.append((X - B * a)//A)

for a in range(len(pos)):
    if pos[a] * A + B * len(str(pos[a])) <= X:
        break
N = pos[a]
if 0 <= N <= 10**9:
    print(N)
elif N < 0:
    print(0)
else:
    print(10**9)