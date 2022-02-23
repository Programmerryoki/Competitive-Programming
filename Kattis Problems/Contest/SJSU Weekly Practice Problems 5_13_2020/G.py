C, X, M = [float(i) for i in input().split()]
C = C/2
S = 0
for _ in range(6):
    s, fe = [float(i) for i in input().split()]
    h = M/s
    rem = C - h*X
    if rem*fe >= M:
        S = s
if S == 0:
    print("NO")
else:
    print("YES",int(S))